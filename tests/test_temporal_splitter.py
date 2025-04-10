from langchain_core.documents import Document

from core.temporal_text_splitter import TemporalTextSplitter


def test_temporal_splitter_basic():
    transcript = [
        type("TranscriptSnippet", (), {"text": "Olá mundo", "start": 0.0, "duration": 2.0})(),
        type("TranscriptSnippet", (), {"text": "Testando", "start": 3.0, "duration": 2.0})(),
        type("TranscriptSnippet", (), {"text": "Final", "start": 6.0, "duration": 2.0})()
    ]

    splitter = TemporalTextSplitter(video_id="abc123", window_size=5, overlap=2)
    docs = splitter.split_transcript(transcript)
    assert isinstance(docs[0], Document)
    assert len(docs) > 0
