`Constructor` function line by line:

```python
def __init__(self, source_dir, archive_dir):
```

- `__init__`: Special Python constructor method, always called when creating new class instance
- `self`: Reference to the instance being created
- `source_dir, archive_dir`: Parameters that will store path information

```python
self.source_dir = Path(source_dir)
```

- `Path()`: Function from `pathlib` library that creates a path object
- Why `Path` over string?
  - Handles path separators automatically (/ or \ based on OS)
  - Provides useful methods like `.exists()`, `.mkdir()`, etc.
  - Makes path manipulation easier
- `self.source_dir`: Instance variable that stores the path

```python
self.archive_dir = Path(archive_dir)
```

- Same as above, converts archive directory path to `Path` object

```python
self.archive_dir.mkdir(parents=True, exist_ok=True)
```

- `.mkdir()`: Method from `Path` object to create directory
- `parents=True`:
  - Creates parent directories if they don't exist
  - Like `mkdir -p` in Unix
- `exist_ok=True`:
  - Won't raise error if directory already exists
  - Without this, you'd get `FileExistsError`

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```

- `logging`: Python's built-in logging library
- `basicConfig()`: Sets up basic configuration for logging
- `level=logging.INFO`: Sets log level
  - DEBUG < INFO < WARNING < ERROR < CRITICAL
  - Will show all messages at INFO level and above
- `format=`: Defines log message structure
  - `%(asctime)s`: Timestamp
  - `%(levelname)s`: Log level (INFO, ERROR, etc.)
  - `%(message)s`: Actual log message
  - `-`: Separators between components
  - Example output: `2024-11-20 11:30:55 - INFO - Archive created`

```python
self.logger = logging.getLogger(__name__)
```

- `logging.getLogger()`: Creates/gets a logger instance
- `__name__`: Special Python variable
  - Contains module's name
  - Helps identify which module generated the log
- `self.logger`: Stores logger instance for use in other methods
  - Will be used like `self.logger.info("message")`
  - Or `self.logger.error("error message")`

This constructor sets up:

1. Path handling with `pathlib`
2. Directory structure creation
3. Logging system configuration
4. Instance-specific logger
