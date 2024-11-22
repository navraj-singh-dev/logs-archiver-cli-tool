import os
from pathlib import Path


class Config:
    DEFAULT_SOURCE_DIR = "/var/log"
    DEFAULT_ARCHIVE_DIR = str(Path.home() / "log_archives")

    @staticmethod
    def get_source_dir():
        return os.getenv("LOG_ARCHIVE_SOURCE", Config.DEFAULT_SOURCE_DIR)

    @staticmethod
    def get_archive_dir():
        return os.getenv("LOG_ARCHIVE_DEST", Config.DEFAULT_ARCHIVE_DIR)
