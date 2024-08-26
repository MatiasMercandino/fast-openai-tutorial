import streamlit as st
import json
import requests

# Definir el endpoint de la aplicación FastAPI
endpoint = "https://matiasmercandino--fastapi-openai-app-fastapi-app.modal.run"

# Establecer el título de la aplicación Streamlit
st.title("🎓 Evaluación Interactiva para Data Science")

# Introducción amigable
st.write(
    """
    ¡Bienvenido a la **Evaluación Interactiva para Data Science**! 🌟 
    Aquí podrás poner a prueba tus conocimientos en las asignaturas que has cursado durante tu magíster.
    Selecciona una asignatura, el nivel, y el número de preguntas que deseas responder. 
    ¡Vamos a aprender juntos! 🚀
    """
)

# Crear un selectbox para que el usuario seleccione la asignatura (tema)
topic = st.selectbox(
    "📝 Selecciona la asignatura que deseas explorar:",
    [
        "Data Driven Organizations",
        "Python para Data Science",
        "Estadística para Data Science",
        "Análisis de Datos",
        "Visualización de la Información",
        "Machine Learning",
        "Almacenamiento y Captura de Datos",
        "Ciencia de Redes",
        "Machine Learning Avanzado",
        "Seguridad y protección de datos",
        "Big Data y Cloud Computing",
        "Visión Computacional",
        "Desarrollo de Proyectos y Productos de Datos",
        "Análisis de Big Data",
        "Procesamiento de Lenguaje Natural"
    ]
)

# Crear un selectbox para que el usuario seleccione el nivel
level = st.selectbox("📚 Seleccione el nivel de las preguntas:", ["Básico", "Intermedio", "Avanzado"])

# Selección del número de preguntas
num_questions = st.slider("🔢 ¿Cuántas preguntas te gustaría responder?", 1, 5, 3)

# Preparar los datos de entrada para la solicitud de la API
input_data = {
    "topic": topic,
    "level": level,
    "num_questions": num_questions
}

# Generar las preguntas
if st.button("💡 Generar Preguntas"):
    st.write("🤔 Generando preguntas... ¡prepárate para pensar!")
    res = requests.post(url=f"{endpoint}/generate-questions", data=json.dumps(input_data), headers={"Content-Type": "application/json"})
    if res.status_code == 200:
        res_json = res.json()
        st.session_state['questions'] = res_json["questions"]
        st.session_state['responses'] = [""] * len(st.session_state['questions'])  # Inicializar respuestas vacías
    else:
        st.error(f"Error: {res.status_code} - {res.text}")

# Mostrar preguntas y capturar respuestas
if 'questions' in st.session_state:
    for idx, question in enumerate(st.session_state['questions'], start=1):
        st.subheader(f"🧠 Pregunta {idx}")
        st.markdown(question)  # Mostrar solo la pregunta
        st.session_state['responses'][idx-1] = st.text_area(f"✍️ Tu respuesta para la Pregunta {idx}:", value=st.session_state['responses'][idx-1], key=f"response_{idx}")

# Evaluar las respuestas y proporcionar retroalimentación
if st.button("🔍 Evaluar Respuestas"):
    if 'questions' in st.session_state:
        feedback_messages = []
        for idx, question in enumerate(st.session_state['questions'], start=1):
            student_response = st.session_state['responses'][idx-1]
            if student_response:
                eval_input_data = {
                    "student_response": student_response,
                    "correct_response": question
                }
                res = requests.post(url=f"{endpoint}/evaluate-answer", data=json.dumps(eval_input_data), headers={"Content-Type": "application/json"})
                if res.status_code == 200:
                    res_json = res.json()
                    st.subheader(f"📊 Retroalimentación para la Pregunta {idx}")
                    st.markdown(res_json["feedback"])
                else:
                    st.error(f"Error al evaluar la respuesta: {res.status_code} - {res.text}")
            else:
                st.warning(f"⚠️ No has respondido a la Pregunta {idx}.")
    else:
        st.warning("⚠️ Genera las preguntas antes de intentar evaluar tus respuestas.")

# Despedida motivadora
st.write("---")
st.write("🌟 **Sigue adelante!** Cada pregunta es una oportunidad para aprender algo nuevo. ¡No te rindas y sigue explorando! 🚀")
