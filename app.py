import io
import streamlit as st
from gtts import gTTS
from aurora import app_header, footer, section

app_header()
with st.sidebar:
    st.subheader("De texto a audio")
    st.write("Elige la pronunciación del texto. La app no traduce entre idiomas.")

with st.expander("Texto de ejemplo · Una pequeña fábula"):
    st.write('¡Ay! —dijo el ratón—. El mundo se hace cada día más pequeño. Al principio era tan grande que le tenía miedo. Corría y corría y por cierto que me alegraba ver esos muros, a diestra y siniestra, en la distancia. Pero esas paredes se estrechan tan rápido que me encuentro en el último cuarto y ahí en el rincón está la trampa sobre la cual debo pasar. Todo lo que debes hacer es cambiar de rumbo, dijo el gato… y se lo comió.')
    st.caption("Franz Kafka · Una pequeña fábula")

text=st.text_area("Texto para escuchar",height=180,placeholder="Escribe o pega un texto…")
language=st.selectbox("Idioma de pronunciación",["Español","English"])
context=(text,language)
if st.session_state.get('audio_context') != context:
    st.session_state.pop('audio_result',None)
    st.session_state.audio_context=context
if st.button("Convertir a audio",type="primary"):
    if not text.strip():
        st.warning("Escribe un texto antes de generar el audio.")
    else:
        try:
            with st.spinner("Preparando tu audio…"):
                buffer=io.BytesIO()
                gTTS(text,lang='es' if language=='Español' else 'en').write_to_fp(buffer)
                st.session_state.audio_result=buffer.getvalue()
        except Exception:
            st.error("No se pudo generar el audio. Revisa la conexión y vuelve a intentarlo.")
if st.session_state.get('audio_result'):
    section("02","Escucha el resultado","Texto → Voz")
    st.audio(st.session_state.audio_result,format='audio/mp3')
    st.download_button("Descargar audio",st.session_state.audio_result,file_name='aurora-audio.mp3',mime='audio/mpeg')
footer("ESCRIBIR / ESCUCHAR / COMPARTIR")
