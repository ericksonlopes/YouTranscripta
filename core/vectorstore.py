from typing import List

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from loguru import logger


class VectorStoreHandler:
    def __init__(self, persist_dir: str = "./chroma_langchain_db"):
        self.persist_dir = persist_dir
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
        self.collection_name = "youtube_transcripts"
        self.vectorstore = Chroma(
            embedding_function=self.embeddings,
            persist_directory=self.persist_dir,
            collection_name=self.collection_name
        )

    def video_already_indexed(self, video_id: str) -> bool:
        """Check if the given video_id already exists in the vectorstore."""
        existing = self.vectorstore.get(where={"video_id": video_id})
        return bool(existing and existing.get("ids"))

    def create_vectorstore(self, documents: List[Document]) -> Chroma:
        """Create and persist vectorstore if video_id is not already indexed."""
        logger.info("Initializing vectorstore...")

        if not documents:
            logger.warning("No documents provided for storage.")
            return self.vectorstore

        video_id = documents[0].metadata.get("video_id")
        if not video_id:
            logger.error("video_id not found in document metadata.")
            return self.vectorstore

        if self.video_already_indexed(video_id):
            logger.info(f"Documents with video_id='{video_id}' already exist. Skipping creation.")
            return self.vectorstore

        self.vectorstore.add_documents(documents)
        logger.success("Vectorstore successfully created.")
        return self.vectorstore
