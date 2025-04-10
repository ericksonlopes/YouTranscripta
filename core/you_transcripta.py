from loguru import logger

from core.config import Config
from core.qa_system import QASystem
from core.temporal_text_splitter import TemporalTextSplitter
from core.transcript import TranscriptProcessor
from core.vectorstore import VectorStoreHandler


class YouTranscripta:
    """Facade for the YouTube transcription and RAG-based QA system."""

    def __init__(self, video_id: str, language: str = 'pt'):
        Config()
        self.video_id = video_id
        self.language = language

        self.vector_handler = VectorStoreHandler()

        if self.vector_handler.video_already_indexed(video_id):
            logger.info(f"Video {video_id} is already indexed. Skipping transcription.")
            self.vectorstore = self.vector_handler.vectorstore
        else:
            logger.info("Processing new transcript...")
            processor = TranscriptProcessor(video_id, language)
            splitter = TemporalTextSplitter(video_id)
            documents = splitter.split_transcript(processor.transcript)
            self.vectorstore = self.vector_handler.create_vectorstore(documents)

        self.qa_system = QASystem(self.vectorstore, video_id)

    def ask(self, question: str) -> str:
        return self.qa_system.ask(question)
