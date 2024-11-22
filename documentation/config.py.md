`config.py` file in detail, line by line:

1. **Imports**:

```python
import os
from pathlib import Path
```

- `import os`: Gets access to operating system functions

  - Used for environment variables
  - Works on all operating systems (Windows, Linux, Mac)
  - We use it here for `os.getenv()`

- `from pathlib import Path`: Modern way to handle file paths
  - Makes paths work on any operating system
  - Easier than old-style string paths
  - Has helpful methods for path operations

2. **Class Definition**:

```python
class Config:
```

- Creates a class to hold all configuration settings
- Works as a container for related settings
- Makes settings easy to import anywhere in project

3. **Default Settings**:

```python
DEFAULT_SOURCE_DIR = "/var/log"
DEFAULT_ARCHIVE_DIR = str(Path.home() / "log_archives")
```

- `DEFAULT_SOURCE_DIR = "/var/log"`:

  - Where logs are usually kept on Linux
  - Default place to look for logs
  - Can be overridden by environment variable

- `DEFAULT_ARCHIVE_DIR = str(Path.home() / "log_archives")`:
  - `Path.home()`: Gets user's home directory
    - Windows: "C:\Users\username"
    - Linux: "/home/username"
    - Mac: "/Users/username"
  - `/ "log_archives"`: Adds folder name to path
  - `str()`: Converts Path object to string

4. **Source Directory Getter**:

```python
@staticmethod
def get_source_dir():
    return os.getenv("LOG_ARCHIVE_SOURCE", Config.DEFAULT_SOURCE_DIR)
```

- `@staticmethod`: Means you can use method without creating class instance
- `get_source_dir()`: Function to get source directory
- `os.getenv()`: Checks environment variables
  - First argument: "LOG_ARCHIVE_SOURCE" (variable to check)
  - Second argument: Default value if variable not found
  - If LOG_ARCHIVE_SOURCE is set, uses that
  - If not set, uses DEFAULT_SOURCE_DIR

5. **Archive Directory Getter**:

```python
@staticmethod
def get_archive_dir():
    return os.getenv("LOG_ARCHIVE_DEST", Config.DEFAULT_ARCHIVE_DIR)
```

- Same pattern as get_source_dir()
- Checks LOG_ARCHIVE_DEST environment variable
- Falls back to DEFAULT_ARCHIVE_DIR if not set

6. **How to Use This Config**:

```python
# In other files:
from .config import Config

# Get source directory
source_dir = Config.get_source_dir()

# Get archive directory
archive_dir = Config.get_archive_dir()

# Override with environment variables:
# Linux/Mac:
export LOG_ARCHIVE_SOURCE="/different/logs"
# Windows:
set LOG_ARCHIVE_SOURCE=C:\different\logs
```
