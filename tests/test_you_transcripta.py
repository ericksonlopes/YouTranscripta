from core.you_transcripta import YouTranscripta


def test_full_pipeline(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "fake-api-key")

    # Mocks the transcript fetch
    monkeypatch.setattr("core.transcript.TranscriptProcessor._fetch_transcript", lambda self: [
        type("TranscriptSnippet", (), {"text": "Test", "start": 0.0, "duration": 2.0})()
    ])

    # Mocks the indexed video checker
    monkeypatch.setattr("core.vectorstore.VectorStoreHandler.video_already_indexed", lambda self, id: False)

    # Mocks metadata extraction
    monkeypatch.setattr("core.qa_system.VideoMetadataExtractor.extract_metadata", lambda self: {
        "title": "titulo", "channel": "canal", "tags": ["teste"]
    })

    # Mocks the retriever expected by LangChain
    class DummyRetriever:
        def invoke(self, x):
            return {"result": "mock"}

    class DummyVectorStore:
        def as_retriever(self, **kwargs):
            return DummyRetriever()

    monkeypatch.setattr("core.vectorstore.VectorStoreHandler.create_vectorstore", lambda self, docs: DummyVectorStore())

    # Mocks the QA chain with a ready response
    class DummyQAChain:
        def invoke(self, inputs):
            return {"result": "Resposta teste"}

    monkeypatch.setattr("core.qa_system.RetrievalQA.from_chain_type", lambda *args, **kwargs: DummyQAChain())
    monkeypatch.setattr("core.qa_system.ChatOpenAI", lambda *args, **kwargs: object())

    yt = YouTranscripta(video_id="abc123")
    assert yt.ask("Qual o assunto?") == "Resposta teste"
