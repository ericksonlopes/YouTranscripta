from core.you_transcripta import YouTranscripta


def test_full_pipeline(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "fake-api-key")

    # Mocka o fetch da transcrição
    monkeypatch.setattr("core.transcript.TranscriptProcessor._fetch_transcript", lambda self: [
        type("TranscriptSnippet", (), {"text": "Teste", "start": 0.0, "duration": 2.0})()
    ])

    # Mocka o verificador de vídeo indexado
    monkeypatch.setattr("core.vectorstore.VectorStoreHandler.video_already_indexed", lambda self, id: False)

    # Mocka a extração de metadados
    monkeypatch.setattr("core.qa_system.VideoMetadataExtractor.extract_metadata", lambda self: {
        "title": "titulo", "channel": "canal", "tags": ["teste"]
    })

    # Mocka o retriever esperado pelo LangChain
    class DummyRetriever:
        def invoke(self, x):
            return {"result": "mock"}

    class DummyVectorStore:
        def as_retriever(self, **kwargs):
            return DummyRetriever()

    monkeypatch.setattr("core.vectorstore.VectorStoreHandler.create_vectorstore", lambda self, docs: DummyVectorStore())

    # Mocka a QA chain com resposta pronta
    class DummyQAChain:
        def invoke(self, inputs):
            return {"result": "Resposta teste"}

    monkeypatch.setattr("core.qa_system.RetrievalQA.from_chain_type", lambda *args, **kwargs: DummyQAChain())
    monkeypatch.setattr("core.qa_system.ChatOpenAI", lambda *args, **kwargs: object())

    yt = YouTranscripta(video_id="abc123")
    assert yt.ask("Qual o assunto?") == "Resposta teste"
