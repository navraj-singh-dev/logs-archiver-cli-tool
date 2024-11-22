`extract_archive` function line by line, breaking down each part carefully:

```python
def extract_archive(self, archive_name, extract_path=None):
    """Extract a specific archive"""
```

- This is a method in the LogArchiver class
- Takes 2 parameters:
  - `archive_name`: Name of archive to extract (required)
  - `extract_path`: Where to extract files (optional, defaults to None)
- Purpose stated in docstring: Extract files from an archive

```python
if os.path.sep in archive_name:
    archive_path = Path(archive_name)  # Use the provided path directly
else:
    archive_path = self.archive_dir / archive_name  # Use archive_dir only for bare filenames
```

- Checks if `archive_name` contains path separators (like / or \)
- If it has separators:
  - Treats it as a full path
  - Creates Path object directly from it
- If no separators:
  - Assumes it's just a filename
  - Combines it with the archive directory path
  - Uses / operator which properly joins paths on any OS

```python
if not archive_path.exists():
    raise FileNotFoundError(f"Archive {archive_path} not found")
```

- Checks if the archive file actually exists
- If not found:
  - Raises FileNotFoundError with helpful message
  - Includes the full path in error message

```python
extract_path = Path(extract_path) if extract_path else Path.cwd()
```

- If extract_path was provided:
  - Converts it to a Path object
- If not provided (None):
  - Uses current working directory (Path.cwd())
- Ensures we always have a valid Path object

```python
archive_basename = archive_path.stem.replace('.tar', '')  # Remove both .tar and .gz
extract_dir = extract_path / archive_basename
extract_dir.mkdir(parents=True, exist_ok=True)
```

- Gets base name of archive without extensions:
  - `.stem` removes last extension (.gz)
  - `.replace('.tar', '')` removes .tar
- Creates new directory path by joining:
  - extract_path (where to extract)
  - archive_basename (name without extensions)
- Creates the directory:
  - `parents=True`: creates parent directories if needed
  - `exist_ok=True`: doesn't error if directory exists

```python
try:
    with tarfile.open(archive_path, "r:gz") as tar:
        tar.extractall(path=extract_dir)
    self.logger.info(f"Archive extracted to {extract_dir}")
```

- Opens archive in try block (handles errors gracefully)
- Uses tarfile to open archive:
  - "r:gz" means read gzipped tar file
  - Uses context manager (`with`) for automatic cleanup
- Extracts all files to extract_dir
- Logs successful extraction with destination path

```python
with open(extract_dir / "archive_info.txt", "w") as f:
    f.write(f"Extracted from: {archive_path}\n")
    f.write(f"Extraction time: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
    f.write(f"Original archive size: {self._get_file_size(archive_path)}\n")
```

- Creates info file in extracted directory
- Opens file in write mode
- Writes three pieces of information:
  - Original archive path
  - Current time formatted as day/month/year hour:minute:second
  - Original archive size (using helper method)
- Uses \n for line breaks

```python
except Exception as e:
    self.logger.error(f"Archive extraction failed: {str(e)}")
    raise
```

- Catches any errors during extraction
- Logs error message with specific error details
- Re-raises exception to let caller handle it
