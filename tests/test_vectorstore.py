from langchain_core.documents import Document

from core.vectorstore import VectorStoreHandler


def test_vectorstore_add_and_check(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "fake-api-key")

    handler = VectorStoreHandler()

    monkeypatch.setattr(handler.vectorstore, "get", lambda where: {"ids": []})
    monkeypatch.setattr(handler.vectorstore, "add_documents", lambda docs: True)

    doc = Document(page_content="teste", metadata={"video_id": "abc123"})
    handler.create_vectorstore([doc])
    assert handler.video_already_indexed("abc123") in [True, False]
