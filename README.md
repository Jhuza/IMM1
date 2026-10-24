# Texto a voz

Transforma un texto en voz en español o inglés y descarga el audio.

Adaptación académica de Juan José Hoyos (Jhuza), a partir del ejercicio compartido por Carlos Mario Correa. Interfaz basada en [Aurora](docs/guia-visual-aurora.md).

[Abrir app](https://cyep53ohwhhthv9sebnkrf.streamlit.app/) · [Portafolio](https://jhginterfacesmultimodalesportfolio.streamlit.app/)

## Ejecutar

```sh
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Uso y alcance

Escribe un texto, elige el idioma y pulsa Convertir a audio. Puedes reproducir o descargar el resultado.

Necesita conexión al servicio de síntesis. La selección de idioma cambia la pronunciación; no traduce el texto.

Consulta la [ficha de la experiencia](docs/EXPERIENCIA.md). Las credenciales se introducen en la sesión; no deben guardarse en el código.

## Verificación

Las pruebas de `tests/` comprueban controles, entradas vacías y resultados con servicios o modelos simulados. No certifican una respuesta de un servicio externo. Ejecutar con `python -m pytest tests -q` después de instalar pytest y las dependencias de la app.
