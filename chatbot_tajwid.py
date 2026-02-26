import streamlit as st
from pytgpt.leo import LEO

st.set_page_config(
    page_title="Chatbot Ilmu Tajwid - GRATIS",
    page_icon="🕌",
    layout="centered"
)

st.title("🕌 Chatbot Ilmu Tajwid")
st.markdown("### GRATIS - Langsung Tanya!")
st.markdown("---")

with st.sidebar:
    st.header("📖 Info")
    st.markdown("""
    **Cara pakai:**
    1. Tanya di kolom chat
    2. Tunggu jawaban
    3. Selesai!
    
    **Provider:** Leo (Brave)
    """)
    
    st.markdown("**Contoh:**")
    st.markdown("- Apa itu idgham?")
    st.markdown("- Jelaskan mad jaiz munfasil")
    st.markdown("- Perbedaan qalqalah sugra dan kubra")

@st.cache_resource
def init_bot():
    try:
        return LEO()
    except Exception as e:
        st.error(f"Error: {e}")
        return None

bot = init_bot()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Tanya tentang tajwid..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    if bot:
        with st.chat_message("assistant"):
            with st.spinner("Mencari jawaban..."):
                try:
                    response = bot.chat(f"Jelaskan tentang {prompt} dalam ilmu tajwid dengan contoh")
                    st.write(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"Error: {e}")
    else:
        st.error("Bot tidak bisa diinisialisasi")

if st.sidebar.button("🔄 Reset Chat"):
    st.session_state.messages = []
    st.rerun()
