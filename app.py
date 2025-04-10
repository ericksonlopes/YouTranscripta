import streamlit as st

from core.you_transcripta import YouTranscripta

st.set_page_config(page_title="YouTranscripta", layout="wide")

# Estilo
st.markdown("""
    <style>
        .stTextInput>div>div>input {
            border-radius: 10px;
            padding: 0.6rem;
        }
        .big-title {
            font-size: 2.5rem;
            font-weight: 700;
            text-align: center;
        }
        .subtitle {
            font-size: 1.2rem;
            color: #ccc;
            text-align: center;
        }
        .button-container {
            display: flex;
            justify-content: center;
            gap: 1rem;
            flex-wrap: nowrap; /* evita quebra */
            margin-bottom: 1.5rem;
        }
        .button-container .stButton > button {
            padding: 0.5rem 1rem;
            font-size: 0.85rem;
            width: 240px;
            white-space: nowrap; /* evita quebra de linha no texto */
            text-align: center;
            border-radius: 8px;
        }
        .question-label {
            text-align: center;
            font-weight: 600;
            font-size: 1.1rem;
            margin-top: 1.5rem;
            margin-bottom: 0.8rem;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown('<div class="big-title">🎥 YouTranscripta</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Transcreva vídeos do YouTube e faça perguntas com IA usando LangChain + RAG.</div>',
            unsafe_allow_html=True)
st.markdown("---")

# Inputs centralizados
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    video_url = st.text_input("Insira a URL do vídeo do YouTube:")
    question = st.text_input("Digite sua pergunta sobre o conteúdo do vídeo:")

    # Perguntas pré-prontas centralizadas e sem quebra
    st.markdown('<div class="question-label">🤖 Sugestões de perguntas:</div>', unsafe_allow_html=True)
    st.markdown('<div class="button-container">', unsafe_allow_html=True)

    col_btn1, col_btn2, col_btn3, col_btn4 = st.columns(4)

    with col_btn1:
        if st.button("📋 Faça um sumário do vídeo"):
            question = "Faça um sumário sobre o vídeo."

    with col_btn2:
        if st.button("🔍 Liste os principais pontos"):
            question = "Liste os principais pontos abordados no vídeo."

    with col_btn3:
        if st.button("❓ Qual a mensagem principal?"):
            question = "Qual é a mensagem principal do vídeo?"

    with col_btn4:
        if st.button("🧠 Quais aprendizados posso tirar?"):
            question = "Quais são os principais aprendizados do vídeo?"

    st.markdown('</div>', unsafe_allow_html=True)

# Execução
if video_url:
    try:
        video_id = video_url.split("v=")[-1].split("&")[0]
        yt = YouTranscripta(video_id=video_id)

        if question:
            with col2:
                with st.spinner("Consultando IA..."):
                    resposta = yt.ask(question)

                st.success("✅ Análise finalizada!")

            # Resposta em tela cheia
            st.markdown("### 💡 Resposta:")
            st.markdown(resposta)

    except Exception as e:
        st.error(f"Ocorreu um erro: {e}")
