# DataSensei
## Descripción del Proyecto
Este repositorio contiene DataSensei , un chatbot educativo impulsado por IA diseñado para generar evaluaciones personalizadas que ayuden a consolidar y mejorar el conocimiento adquirido durante el programa de Magister en Data Science de la Universidad del Desarrollo (UDD). La aplicación utiliza los modelos de OpenAI para generar preguntas basadas en varios temas cubiertos en el programa, como Machine Learning, Network Science y Statistics for Data Science. El backend está construido utilizando FastAPI e interactúa con la API de OpenAI, mientras que el frontend es una aplicación Streamlit que proporciona una interfaz de usuario interactiva. Las aplicaciones están diseñadas para su implementación en contenedores utilizando la plataforma Modal.

## Notas
Este repositorio alberga un proyecto de demostración para el proyecto final del Magiter en Data Science de la Universidad del Desarrollo (UDD). El propósito de este proyecto es demostrar la integración de varias tecnologías de vanguardia, incluidas Modal, Streamlit, FastAPI y OpenAI API.

La aplicación, DataSensei , funciona como una herramienta educativa impulsada por IA que genera preguntas y comentarios para la autoevaluación en áreas clave de la ciencia de datos. El backend se desarrolló utilizando FastAPI, un marco web moderno, rápido (de alto rendimiento) para crear API con Python. El frontend es una aplicación Streamlit, que proporciona una interfaz intuitiva para que los usuarios interactúen con el chatbot, seleccionen temas y reciban preguntas y comentarios generados por IA.

Toda la aplicación está contenedorizada para su implementación mediante la plataforma Modal, mostrando un ciclo de desarrollo de productos de datos de extremo a extremo, desde la integración del modelo de IA hasta el diseño y la implementación de la interfaz de usuario.

Este proyecto de demostración sirve como ejemplo práctico de creación e implementación de un producto de datos como parte del proyecto final del programa. Ilustra la aplicación de los conceptos y tecnologías aprendidos a lo largo del curso en un escenario del mundo real.

## Estructura del Proyecto   
   ```plaintext
   /fast-openai-tutorial/
   ├── backend/              # Contiene la lógica principal del chatbot
   │   ├── __init__.py       # Inicialización del módulo
   │   └── main.py           # FastAPI, integración con OpenAI y despliegue en Modal
   │
   ├── .env                  # Variables de entorno (clave de OpenAI)
   ├── .gitignore            # Archivos a excluir del control de versiones
   ├── README.md             # Documentación principal del proyecto
   ├── requirements.txt      # Dependencias del proyecto
   └── st_app.py             # Aplicación Streamlit para la interfaz de usuario
  ```
## Empezando
Antes de comenzar a ejecutar este proyecto, hay algunos requisitos previos que deberá tener en cuenta:

✅ Clave API de OpenAI: Para interactuar con la API de OpenAI, necesitarás una clave API. Puedes obtenerla creando una cuenta en el sitio web de OpenAI y siguiendo sus instrucciones para generar una clave API. 

✅ Cuenta Modal: la aplicación está en contenedores para su implementación mediante la plataforma Modal. Visite el sitio web de Modal para registrarse y obtener una cuenta si aún no tiene una.

✅ Cuenta Streamlit (opcional): si bien puedes ejecutar aplicaciones Streamlit localmente sin una cuenta, tener una cuenta Streamlit te permite implementar y compartir tus aplicaciones, lo que puede ser útil para mostrar tu proyecto a otras personas. Si deseas utilizar esta función, regístrate para obtener una cuenta Streamlit.

Recuerda siempre revisar la documentación de OpenAI, Modal y Streamlit en caso de que se haya modificado la manera de comunicarse con cada una. 

## Instalación
Para configurar el proyecto localmente, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/MatiasMercandino/fast-openai-tutorial.git
   cd fast-openai-tutorial

2. **Crear un nuevo entorno virtual:**
   ```bash
   python -m venv .venv

3. **Activar entorno virtual**
   ```bash
   .venv\Scripts\activate
   
4. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt

## Ejecutando el Backend y Frontend

1. **Para ejecutar el deploy en Modal, utiliza el siguiente comando:**
   ```bash
   modal deploy backend/main.py::app
2. **Para iniciar la interfaz de Streamlit, utiliza:**
    ```bash
    streamlit run st_app.py


