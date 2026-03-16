# 🤖 Chatbot J

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq_API-00A67E?style=for-the-badge&logo=groq&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**Chatbot interactivo impulsado por IA para conversaciones en tiempo real.**

[🌐 Demo en vivo](https://chatbotempresa-htjzzs8kemnhtytkguxf8q.streamlit.app/)

</div>

---

## 📋 Tabla de contenidos

- Descripción
- Funcionalidades
- Tecnologías utilizadas
- Instalación
- Configuración
- Uso
- Estructura del proyecto
- Contribuciones

---

## 📌 Descripción

**Chatbot J** es un chatbot interactivo desarrollado con **Python** y **Streamlit**, que permite a los usuarios conversar con una inteligencia artificial de manera sencilla y amigable. Utiliza la **API de Groq** como motor de respuestas, ofreciendo interacciones rápidas y fluidas directamente desde el navegador.

---

## 🚀 Funcionalidades

- 💬 **Conversación en tiempo real** con IA mediante la API de Groq.
- 🤖 **Selección de modelo** — elige el modelo de IA a utilizar (ej. `llama-3.3-70b-versatile`).
- 🌡️ **Control de temperatura** — ajusta la creatividad de las respuestas (0.00 – 1.00).
- 📝 **System prompt personalizable** — define el comportamiento y personalidad del chatbot.
- 🗑️ **Limpiar conversación** — reinicia el historial con un solo clic.
- 📊 **Contador de mensajes** en el historial de conversación.
- 🔑 **Integración segura con API Key** usando variables de entorno.
- 🌐 **Desplegado en la nube** — accesible desde cualquier dispositivo.

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Descripción |
|---|---|
| 🐍 **Python** | Lógica principal del chatbot |
| 🖥️ **Streamlit** | Interfaz de usuario web |
| ⚡ **Groq API** | Motor de respuestas de IA |
| 🔒 **python-dotenv** | Gestión segura de variables de entorno |

---

## 📦 Instalación

Sigue estos pasos para ejecutar el proyecto localmente:

**1. Clona el repositorio**
```bash
git clone https://github.com/JohanaQuispe/chatbot_empresa.git
cd chatbot_empresa
```

**2. Crea un entorno virtual (recomendado)**
```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

**3. Instala las dependencias**
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuración

**1. Crea un archivo `.env`** en la raíz del proyecto:
```
GROQ_API_KEY=tu_api_key_aqui
```

**2. Obtén tu API Key** de forma gratuita en [console.groq.com](https://console.groq.com).

> ⚠️ **Importante:** Nunca subas tu archivo `.env` al repositorio. Asegúrate de que esté incluido en el `.gitignore`.

---

## ▶️ Uso

Ejecuta la aplicación con:
```bash
streamlit run app.py
```

Luego abre tu navegador en `http://localhost:8501` y comienza a chatear. 🎉

También puedes usar la **[demo en vivo](https://chatbotempresa-htjzzs8kemnhtytkguxf8q.streamlit.app/)** sin necesidad de instalación.

---

## 📁 Estructura del proyecto

```
chatbot_empresa/
│
├── app.py               # Aplicación principal de Streamlit
├── .env                 # Variables de entorno (no incluir en git)
├── .gitignore           # Archivos ignorados por git
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación
```

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar el proyecto:

1. Haz un fork del repositorio.
2. Crea una rama nueva: `git checkout -b feature/nueva-funcionalidad`
3. Realiza tus cambios y haz commit: `git commit -m "Agrega nueva funcionalidad"`
4. Haz push a tu rama: `git push origin feature/nueva-funcionalidad`
5. Abre un **Pull Request**.

---

<div align="center">

Desarrollado con ❤️ por [Johana Quispe](https://github.com/JohanaQuispe)

</div>
