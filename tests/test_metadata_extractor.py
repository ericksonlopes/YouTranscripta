from core.metadata_extractor import VideoMetadataExtractor

def test_extract_metadata(monkeypatch):
    monkeypatch.setattr("yt_dlp.YoutubeDL.extract_info", lambda self, url, download: {"title": "Titulo", "channel": "Canal", "tags": ["educativo"]})
    monkeypatch.setattr("yt_dlp.YoutubeDL.__enter__", lambda self: self)
    monkeypatch.setattr("yt_dlp.YoutubeDL.__exit__", lambda self, exc_type, exc_val, exc_tb: None)

    extractor = VideoMetadataExtractor(video_id="abc123")
    metadata = extractor.extract_metadata()
    assert metadata.get("title") == "Titulo"
