from unittest.mock import patch, MagicMock


# Simular execução como Streamlit (em modo de teste)
@patch("core.you_transcripta.YouTranscripta")
def test_app_execution(mock_transcripta, monkeypatch):
    # Mocks
    instance = MagicMock()
    instance.ask.return_value = "Sim, vale a pena!"
    mock_transcripta.return_value = instance

    # Simula valores de entrada
    monkeypatch.setattr("streamlit.text_input", lambda label, **kwargs: {
        "Insira a URL do vídeo do YouTube:": "https://www.youtube.com/watch?v=dummy123",
        "Digite sua pergunta sobre o conteúdo do vídeo:": "Vale a pena usar a caixinha turbo?"
    }[label])

    # Captura chamadas para Streamlit
    monkeypatch.setattr("streamlit.markdown", lambda *args, **kwargs: None)
    monkeypatch.setattr("streamlit.spinner", lambda *args, **kwargs: iter([None]))
    monkeypatch.setattr("streamlit.success", lambda *args, **kwargs: None)
    monkeypatch.setattr("streamlit.error", lambda *args, **kwargs: None)
    monkeypatch.setattr("streamlit.columns", lambda ratios: [None, MagicMock(), None])
    monkeypatch.setattr("streamlit.set_page_config", lambda *args, **kwargs: None)

    # Importa e executa o app

