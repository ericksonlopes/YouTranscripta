import math
from typing import List

from langchain_core.documents import Document
from youtube_transcript_api import FetchedTranscript
from loguru import logger

class TemporalTextSplitter:
    """Divide a transcrição em janelas temporais com sobreposição."""

    def __init__(self, video_id: str, window_size: int = 30, overlap: int = 5):
        self.video_id = video_id
        self.window_size = window_size
        self.overlap = overlap
        self.step = self.window_size - self.overlap

    def split_transcript(self, transcript: FetchedTranscript) -> List[Document]:
        """Divide a transcrição em documentos com metadados temporais."""
        logger.info("Iniciando divisão da transcrição em janelas...")
        documents = []
        if not transcript:
            logger.warning("Transcrição vazia.")
            return documents

        total_duration = transcript[-1].start + transcript[-1].duration
        windows = math.ceil(total_duration / self.step)

        for i in range(windows):
            start = i * self.step
            end = start + self.window_size
            window_text = [
                snippet.text for snippet in transcript
                if start <= snippet.start < end
            ]

            if window_text:
                documents.append(self._create_document(window_text, start, end))

        logger.success(f"Transcrição dividida em {len(documents)} janelas.")
        return documents

    def _create_document(self, text_segments: List[str], start: float, end: float) -> Document:
        """Cria um Document com metadados temporais."""
        return Document(
            page_content=" ".join(text_segments),
            metadata={
                "window_start": start,
                "window_end": end,
                "video_id": self.video_id,
            }
        )