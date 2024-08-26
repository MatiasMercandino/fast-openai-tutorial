# Data Sensei

## 1. Descripción del Proyecto
Este proyecto se enfoca en el desarrollo de un chatbot educativo diseñado para generar evaluaciones personalizadas, facilitando la consolidación y mejora de los conocimientos adquiridos en el Magíster en Data Science de la Universidad del Desarrollo (UDD). El chatbot genera preguntas basadas en las asignaturas cursadas durante el programa, como Machine Learning, Ciencia de Redes y Estadística para Data Science, entre otras. Las preguntas están clasificadas en tres niveles de dificultad: básico, intermedio y avanzado.

El objetivo principal es ofrecer un método práctico y continuo de autoevaluación que no solo refuerce las competencias técnicas, sino que también mejore las habilidades de comunicación y pensamiento crítico, a través de la generación automática de preguntas y la evaluación de respuestas (feedback).

## 2. Estructura del Proyecto
La estructura del proyecto está organizada de la siguiente manera:

fast-openai-tutorial/
├── backend/              # Contiene la lógica principal del chatbot
│   ├── __init__.py       # Inicialización del módulo
│   └── main.py           # FastAPI, integración con OpenAI, y despliegue en Modal
│
├── .env                  # Variables de entorno (clave de OpenAI)
├── .gitignore            # Archivos a excluir del control de versiones
├── README.md             # Documentación principal del proyecto
├── requirements.txt      # Dependencias del proyecto
├── st_app.py             # Aplicación Streamlit para la interfaz de usuario
└── .venv/                # Entorno virtual (no se incluye en el control de versiones)

