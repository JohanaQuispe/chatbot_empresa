import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# ─── VALIDACIÓN API KEY ───────────────────────────────────────────
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("No se encontró GROQ_API_KEY en el archivo .env")
    st.stop()

client = Groq(api_key=api_key)

st.set_page_config(page_title="Chatbot J", page_icon="🤖", layout="centered")

# ─── CSS PERSONALIZADO ────────────────────────────────────────────
st.markdown("""
<style>
.stApp {
    background-color: #0f0f0f;
    font-family: 'Segoe UI', sans-serif;
}

[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
    background-color: #1e1e2e;
    border-radius: 18px 18px 4px 18px;
    padding: 12px 16px;
    margin: 8px 0;
    max-width: 80%;
    margin-left: auto;
    border: 1px solid #7c3aed33;
}

[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) {
    background-color: #1a1a2e;
    border-radius: 18px 18px 18px 4px;
    padding: 12px 16px;
    margin: 8px 0;
    max-width: 80%;
    border: 1px solid #3b82f633;
}

[data-testid="stChatInput"] textarea {
    background-color: #1e1e2e !important;
    border: 1px solid #7c3aed !important;
    border-radius: 12px !important;
    color: #ffffff !important;
}

h1 {
    color: #a78bfa !important;
    text-align: center;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #111111;
    border-right: 1px solid #7c3aed33;
}
</style>
""", unsafe_allow_html=True)

# ─── SYSTEM PROMPT por defecto ────────────────────────────────────
SYSTEM_PROMPT = "Eres un asistente útil y amigable que responde en español."
MAX_HISTORY = 20

AVATARS = {
    "user":      {"icon": "🧑‍💻", "name": "Tú"},
    "assistant": {"icon": "🤖", "name": "Chatbot J"},
}

# ─── INICIALIZAR HISTORIAL ────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

# ─── SIDEBAR ─────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Configuración")
    st.markdown("---")

    # Selector de modelo
    model = st.selectbox(
        "🧠 Modelo",
        ["llama-3.1-8b-instant", "llama-3.3-70b-versatile", "mixtral-8x7b-32768"],
        index=0
    )

    # Temperatura
    temperature = st.slider("🌡️ Temperatura", 0.0, 1.0, 0.7, 0.1,
                            help="Mayor valor = respuestas más creativas")

    # System prompt editable
    custom_system = st.text_area("📝 System prompt", value=SYSTEM_PROMPT, height=100)
    if st.button("💾 Aplicar prompt"):
        st.session_state.messages[0] = {"role": "system", "content": custom_system}
        st.success("¡Prompt actualizado!")

    st.markdown("---")

    # Contador de mensajes
    num_msgs = len(st.session_state.messages) - 1  # excluye system
    st.caption(f"💬 Mensajes en historial: {num_msgs}")

    # Botón limpiar
    if st.button("🗑️ Limpiar conversación"):
        st.session_state.messages = [st.session_state.messages[0]]  # conserva system
        st.rerun()

# ─── TÍTULO ──────────────────────────────────────────────────────
st.title("🤖 Chatbot J")

# ─── MOSTRAR HISTORIAL ────────────────────────────────────────────
for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    cfg = AVATARS[msg["role"]]
    with st.chat_message(msg["role"], avatar=cfg["icon"]):
        st.markdown(f"**{cfg['name']}**")
        st.write(msg["content"])

# ─── INPUT ────────────────────────────────────────────────────────
user_input = st.chat_input("Escribe tu mensaje...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar=AVATARS["user"]["icon"]):
        st.markdown(f"**{AVATARS['user']['name']}**")
        st.write(user_input)

    # ─── LIMITAR HISTORIAL ────────────────────────────────────────
    messages_to_send = [st.session_state.messages[0]] + st.session_state.messages[-MAX_HISTORY:]

    try:
        with st.spinner("Pensando..."):
            response = client.chat.completions.create(
                model=model,
                messages=messages_to_send,
                temperature=temperature
            )
        bot_reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})

        with st.chat_message("assistant", avatar=AVATARS["assistant"]["icon"]):
            st.markdown(f"**{AVATARS['assistant']['name']}**")
            st.write(bot_reply)

    except Exception as e:
        st.error(f"Error al conectar con Groq: {e}")
