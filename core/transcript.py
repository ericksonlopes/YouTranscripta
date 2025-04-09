from loguru import logger
from youtube_transcript_api import YouTubeTranscriptApi, FetchedTranscript, TranscriptsDisabled, NoTranscriptFound


class TranscriptProcessor:
    """Class to process and split YouTube transcripts."""

    def __init__(self, video_id: str, language: str = 'pt'):
        self.video_id = video_id
        self.language = language
        self.transcript = self._fetch_transcript()

    def _fetch_transcript(self) -> FetchedTranscript:
        """Fetches the transcript for a given video."""
        logger.info(f"Fetching transcript for video: {self.video_id} (language: {self.language})")
        try:
            transcript = YouTubeTranscriptApi().fetch(self.video_id, languages=[self.language])
            logger.success("Transcript successfully fetched.")
            return transcript
        except (TranscriptsDisabled, NoTranscriptFound) as e:
            logger.error(f"Error fetching transcript: {e}")
            raise
