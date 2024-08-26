from fastapi import FastAPI
from pydantic import BaseModel
from modal import App, Image, asgi_app, Secret
from openai import OpenAI
from dotenv import load_dotenv
import os
import random

# Cargar variables de entorno desde .env
load_dotenv()

# Inicializar cliente de OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Crear la aplicación FastAPI
web_app = FastAPI()
app = App("fastapi-openai-app")

# Definir la imagen para el despliegue, instalando las bibliotecas necesarias
image = (
    Image.debian_slim()
    .pip_install(
        "fastapi",
        "openai",
        "pydantic",
        "python-dotenv",
    )
)

# Definir modelos Pydantic para los datos que recibirá la API
class QuestionRequest(BaseModel):
    topic: str
    level: str
    num_questions: int  # Campo para el número de preguntas

class EvaluationRequest(BaseModel):
    student_response: str
    correct_response: str

# Función para generar preguntas de OpenAI
def generate_questions_from_openai(topic, level, num_questions):
    questions = []
    try:
        # Definir diferentes tipos de preguntas
        question_types = [
            f"Genera una pregunta práctica sobre cómo aplicar {topic} en un caso de estudio real.",
            f"Plantea un escenario en el que {topic} podría ser utilizado para resolver un problema, y pregunta cómo lo abordaría el estudiante.",
            f"Haz una pregunta de análisis crítico sobre los desafíos y limitaciones de {topic} en su campo.",
            f"Formula una pregunta evaluativa sobre la eficacia de {topic} en un contexto práctico."
        ]

        for _ in range(num_questions):
            # Seleccionar un tipo de pregunta aleatoriamente
            selected_prompt = random.choice(question_types)

            # Crear el prompt final
            prompt = f"{selected_prompt} La pregunta debe ser adecuada para un nivel {level}."

            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Eres un experto en ciencia de datos y educación. Genera una pregunta reflexiva basada en el tema proporcionado."},
                    {"role": "user", "content": prompt},
                ],
            )
            questions.append(completion.choices[0].message.content)
        
        return questions
    except Exception as e:
        print(f"Error al generar las preguntas desde OpenAI: {str(e)}")
        return [f"Hubo un error al generar las preguntas: {str(e)}"]

# Función para generar retroalimentación personalizada basada en la respuesta del estudiante
def generate_feedback(student_response, correct_response):
    try:
        prompt = (
            f"Has respondido lo siguiente:\n"
            f"Tu respuesta: {student_response}\n\n"
            f"La respuesta correcta o esperada es: {correct_response}\n\n"
            "Proporciona una retroalimentación personalizada y constructiva, dirigida directamente al usuario. "
            "Debes indicar lo que hizo bien, en qué puede mejorar, y sugerir pasos o recursos adicionales para ayudarle a comprender mejor el tema."
        )

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un mentor que ayuda a los estudiantes a aprender y mejorar a través de la reflexión."},
                {"role": "user", "content": prompt},
            ],
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error al generar la retroalimentación desde OpenAI: {str(e)}")
        return f"Hubo un error al generar la retroalimentación: {str(e)}"

# Ruta para generar preguntas iniciales
@web_app.post("/generate-questions")
async def handle_questions(request: QuestionRequest):
    questions = generate_questions_from_openai(request.topic, request.level, request.num_questions)
    return {"questions": questions}

# Ruta para evaluar la respuesta del estudiante y generar retroalimentación
@web_app.post("/evaluate-answer")
async def evaluate_answer(request: EvaluationRequest):
    feedback = generate_feedback(request.student_response, request.correct_response)
    return {"feedback": feedback}

# Configurar los detalles del despliegue para la plataforma Modal
@app.function(image=image, secrets=[Secret.from_dotenv()])
@asgi_app()
def fastapi_app():
    return web_app
