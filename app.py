import streamlit as st
from groq import Groq

# Inicializa el cliente con tu API Key
client = Groq(api_key="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")

st.set_page_config(page_title="Chatbot J", page_icon="🤖")
st.title("💬 Chatbot de prueba")

# Inicializa el historial de la conversación
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes previos
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# Caja de entrada estilo chat
user_input = st.chat_input("Escribe tu mensaje...")

if user_input:
    # Guardar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    try:
        # Enviar todo el historial al modelo
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=st.session_state.messages
        )

        bot_reply = response.choices[0].message.content

        # Guardar respuesta del bot
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        st.chat_message("assistant").write(bot_reply)

    except Exception as e:
        st.error(f"Error: {e}")
