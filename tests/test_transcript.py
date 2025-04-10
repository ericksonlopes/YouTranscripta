from core.transcript import TranscriptProcessor


def test_valid_transcript_fetch(monkeypatch):
    def mock_fetch(*args, **kwargs):
        return [{"text": "Hello", "start": 0.0, "duration": 2.0}]

    monkeypatch.setattr("youtube_transcript_api.YouTubeTranscriptApi.fetch", mock_fetch)
    processor = TranscriptProcessor(video_id="dummy_id")
    assert processor.transcript is not None
