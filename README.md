# 🐾 Pets-streamlit – Clasificador de Mascotas con Machine Learning

**Pets-streamlit** es una aplicación web desarrollada con **Streamlit** que permite clasificar mascotas (gato, perro o conejo) a partir de características físicas básicas, utilizando un modelo de **Machine Learning previamente entrenado**.

El proyecto demuestra un flujo completo de ML aplicado: preprocesado de datos, modelo entrenado, serialización y despliegue en una interfaz interactiva.

---

## 🚀 Funcionalidades

- Interfaz web simple e intuitiva
- Entrada de datos de la mascota:
  - Peso (kg)
  - Altura (cm)
  - Color de ojos
  - Longitud del pelaje
- Codificación automática de variables categóricas
- Predicción en tiempo real usando un modelo entrenado
- Resultado traducido a lenguaje natural (Gato, Perro, Conejo)

---

## 📂 Estructura del proyecto

```text
Pets-streamlit/
│
├── streamlit_app.py
├── models/
│   └── pets_model.joblib
├── data/
│   └── category_mapping.json
├── img/
│   └── pets2.png
├── requirements.txt
└── README.md
```

---

## 🧪 Ejemplo de uso

- Introduce los datos de tu mascota

- Pulsa “Predecir clase de mascota”

- Obtén el resultado en tiempo real 🐶🐱🐰

## 👥 Creditos:

- [Elías Robles Ruiz](https://github.com/eliasrrobles)
