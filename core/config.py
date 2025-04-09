import os

from decouple import config
from loguru import logger


# Environment configuration class
class Config:
    """Centralized environment configuration class."""

    def __init__(self):
        logger.info("Loading environment variables...")
        self.openai_api_key = config('OPENAI_API_KEY')
        os.environ['OPENAI_API_KEY'] = self.openai_api_key
        logger.success("OPENAI_API_KEY successfully loaded.")
