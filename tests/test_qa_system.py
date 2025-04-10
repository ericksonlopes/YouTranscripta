from core.qa_system import QASystem


def test_qa_system_prompt(monkeypatch):
    class DummyVector:
        def as_retriever(self, **kwargs):
            return lambda x: x

    class DummyLLM:
        def __init__(self, *args, **kwargs): pass

    class DummyQAChain:
        def invoke(self, inputs):
            return {"result": "dummy answer"}

    monkeypatch.setattr("core.qa_system.ChatOpenAI", lambda *args, **kwargs: DummyLLM())
    monkeypatch.setattr("core.qa_system.RetrievalQA.from_chain_type", lambda *args, **kwargs: DummyQAChain())
    monkeypatch.setattr("core.qa_system.VideoMetadataExtractor.extract_metadata",
                        lambda self: {"title": "titulo", "channel": "canal", "tags": ["tag"]})

    system = QASystem(vectorstore=DummyVector(), video_id="abc123")
    answer = system.ask("O que foi falado?")
    assert answer == "dummy answer"
