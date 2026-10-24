from pathlib import Path
from unittest.mock import patch
import sys
from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def test_audio_generation_language_and_stale_result():
    calls = []
    class Speech:
        def __init__(self, text, lang):
            calls.append((text, lang))
        def write_to_fp(self, output):
            output.write(b'ID3-test-audio')
    with patch('gtts.gTTS', Speech):
        app = AppTest.from_file(str(ROOT/'app.py')).run(timeout=30)
        app.button[0].click().run()
        assert app.warning and not calls
        app.text_area[0].input('Hello world').run()
        app.selectbox[0].select('English').run()
        app.button[0].click().run()
        assert not app.exception
        assert calls == [('Hello world', 'en')]
        assert app.session_state['audio_result'] == b'ID3-test-audio'
        app.run()
        assert len(app.get('audio')) == 1
        app.text_area[0].input('Otro texto').run()
        assert not app.get('audio')


def test_service_failure_is_explained():
    with patch('gtts.gTTS', side_effect=RuntimeError('offline')):
        app = AppTest.from_file(str(ROOT/'app.py')).run(timeout=30)
        app.text_area[0].input('Hola').run()
        app.button[0].click().run()
        assert not app.exception
        assert any('No se pudo' in item.value for item in app.error)
