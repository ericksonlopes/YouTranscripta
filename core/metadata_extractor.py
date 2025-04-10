from loguru import logger
from yt_dlp import YoutubeDL


class VideoMetadataExtractor:
    """Class to extract metadata from a YouTube video."""

    def __init__(self, video_id: str):
        self.video_id = video_id
        self.video_url = f"https://www.youtube.com/watch?v={video_id}"

    def extract_metadata(self) -> dict:
        """Extracts metadata from the video using yt_dlp."""
        logger.info(f"Extracting metadata for video {self.video_id}...")
        ydl_opts = {
            'format': 'best',
            'noplaylist': True,
            'quiet': True,
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(self.video_url, download=False)

                metadata = {
                    'video_id': self.video_id,
                    'original_url': info_dict.get('original_url'),
                    'title': info_dict.get('title'),
                    'fulltitle': info_dict.get('fulltitle'),
                    'description': info_dict.get('description'),
                    'duration': info_dict.get('duration'),
                    'duration_string': info_dict.get('duration_string'),
                    'categories': info_dict.get('categories'),
                    'tags': info_dict.get('tags'),
                    'channel': info_dict.get('channel'),
                    'channel_id': info_dict.get('channel_id'),
                    'url_streaming': info_dict.get('url'),
                    'upload_date': info_dict.get('upload_date'),
                    'language': info_dict.get('language'),
                    'is_live': info_dict.get('is_live'),
                    'uploader': info_dict.get('uploader'),
                    'uploader_id': info_dict.get('uploader_id'),
                    'uploader_url': info_dict.get('uploader_url'),
                }

                logger.success(f"Metadata successfully extracted for {self.video_id}")
                return metadata

        except Exception as e:
            logger.error(f"Error extracting metadata for video {self.video_id}: {e}")
            return {}
