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
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown('<div class="big-title">🎥 YouTranscripta</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Transcreva vídeos do YouTube e faça perguntas com IA usando LangChain + RAG.</div>', unsafe_allow_html=True)
st.markdown("---")

# Inputs centralizados
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    video_url = st.text_input("Insira a URL do vídeo do YouTube:")
    question = st.text_input("Digite sua pergunta sobre o conteúdo do vídeo:")

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
