import streamlit as st
import pandas as pd
import joblib
import json

st.title("Classypets")
st.write("Clasificador de mascotas, Introduzca los datos de su mascota y le diremos a qué clase pertenece.")
st.image("img/pets2.png", caption="Aplicación de mascotas")

# Carga el modelo entrenado y el json con los tipos
model = joblib.load("models/pets_model.joblib")

with open("data/category_mapping.json", "r") as f:
    category_mapping = json.load(f)

# Entrada de datos del usuario
st.header("Ingrese los datos de su mascota")
weight = st.number_input("Peso (kg)", min_value=0.1, max_value=200.0, value=10.0, step=0.1)
height = st.number_input("Altura (cm)", min_value=1.0, max_value=300.0, value=30.0, step=0.1)
eye_color = st.selectbox("Color de ojos", options=["Azul", "Marrón", "Gris", "Verde"])
fur_length = st.selectbox("Longitud del pelaje", options=["Largo", "Medio", "Corto"])

st.write("### Datos ingresados:")
st.write(f"- Peso: {weight} kg")
st.write(f"- Altura: {height} cm")
st.write(f"- Color de ojos: {eye_color}")
st.write(f"- Longitud del pelaje: {fur_length}")

eye_color_mapping = {"Azul": "blue", "Marrón": "brown", "Gris": "gray", "Verde": "green"}
fur_length_mapping = {"Largo": "long", "Medio": "medium", "Corto": "short"}

selected_eye_color = eye_color_mapping[eye_color]
selected_fur_length = fur_length_mapping[fur_length]

eye_color_binary = [(color == selected_eye_color) for color in eye_color_mapping.values()]
fur_length_binary = [(length == selected_fur_length) for length in fur_length_mapping.values()]

input_data = [weight, height] + eye_color_binary + fur_length_binary
columns = ["weight_kg", "height_cm"] + [f"eye_color_{color}" for color in eye_color_mapping.values()] + [f"fur_length_{length}" for length in fur_length_mapping.values()]

input_df = pd.DataFrame([input_data], columns=columns)

prediction_map = {"cat": "Gato", "dog": "Perro", "rabbit": "Conejo"}

# Botón para predecir
if st.button("Predecir clase de mascota"):
    prediction = model.predict(input_df)
    st.success(f"Su mascota es un {prediction_map[prediction[0]]}", icon="🐾")