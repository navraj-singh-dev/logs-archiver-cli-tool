import os
import tarfile
import datetime
import logging
from pathlib import Path


class LogArchiver:
    def __init__(self, source_dir, archive_dir):
        # This is where log files lives
        self.source_dir = Path(source_dir)
        # This is where compressed archives will be saved
        self.archive_dir = Path(archive_dir)
        self.archive_dir.mkdir(parents=True, exist_ok=True)

        # Setup logging
        logging.basicConfig(
            level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger = logging.getLogger(__name__)

    def create_archive(self):
        """Create a tar.gz archive of log files"""
        timestamp = datetime.datetime.now().strftime("%d_%m_%Y__%H_%M_%S")
        archive_name = f"logs_{timestamp}.tar.gz"
        archive_path = self.archive_dir / archive_name

        try:
            with tarfile.open(archive_path, "w:gz") as tar:
                # Walk through all files in source directory
                for root, _, files in os.walk(self.source_dir):
                    for file in files:
                        if file.endswith(".log"):
                            file_path = Path(root) / file
                            tar.add(file_path, arcname=file_path.name)
                            self.logger.info(f"Added {file} to archive")

            # Create metadata file
            self._create_metadata(archive_name, timestamp)
            return str(archive_path)

        except Exception as e:
            self.logger.error(f"Archive creation failed: {str(e)}")
            raise

    def _create_metadata(self, archive_name, timestamp):
        """Create metadata file for the archive"""
        metadata_path = self.archive_dir / f"{archive_name}_metadata.txt"
        with open(metadata_path, "w") as f:
            f.write(f"Archive Created: {timestamp}\n")
            f.write(f"Source Directory: {self.source_dir}\n")
            f.write(f"Archive Location: {self.archive_dir / archive_name}\n")

    def list_archives(self):
        """List all available archives"""
        archives = []
        for file in self.archive_dir.glob("*.tar.gz"):
            archives.append(str(file))
        return archives

    def extract_archive(self, archive_name, extract_path=None):
        """Extract a specific archive"""
        # Check if archive_name is an absolute path or contains directory components
        if os.path.sep in archive_name:
            archive_path = Path(archive_name)  # Use the provided path directly
        else:
            archive_path = (
                self.archive_dir / archive_name
            )  # Use archive_dir only for bare filenames

        if not archive_path.exists():
            raise FileNotFoundError(f"Archive {archive_path} not found")

        # Create extract path if not provided
        extract_path = Path(extract_path) if extract_path else Path.cwd()

        # Create a directory named after the archive (without the .tar.gz extension)
        archive_basename = archive_path.stem.replace(
            ".tar", ""
        )  # Remove both .tar and .gz
        extract_dir = extract_path / archive_basename
        extract_dir.mkdir(parents=True, exist_ok=True)

        try:
            with tarfile.open(archive_path, "r:gz") as tar:
                tar.extractall(path=extract_dir)
            self.logger.info(f"Archive extracted to {extract_dir}")

            # Create an info file inside the extracted directory
            with open(extract_dir / "archive_info.txt", "w") as f:
                f.write(f"Extracted from: {archive_path}\n")
                f.write(
                    f"Extraction time: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
                )
                f.write(f"Original archive size: {self._get_file_size(archive_path)}\n")

        except Exception as e:
            self.logger.error(f"Archive extraction failed: {str(e)}")
            raise

    def _get_file_size(self, file_path):
        """Get human-readable file size"""
        size = os.path.getsize(file_path)
        for unit in ["B", "KB", "MB", "GB"]:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} TB"
