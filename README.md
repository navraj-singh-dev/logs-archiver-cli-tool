# Log Archive Tool

A powerful Command Line Interface (CLI) tool built in Python3 with Click framework that extract, compress, archive log files. This CLI provides various commands to archive logs from a source directory, compress them to save space, and extract them when needed, and list(print) them if needed.

## Project Overview

The Log Archive Tool is designed to help system administrators and developers manage log files effectively by:
- Archiving log files from specified directories
- Compressing archives to save storage space
- Providing easy extraction of archived logs
- Maintaining a trackable archive system
- Creating metadata files for complete details about archiving and extraction
- Proper logging helps debug code easier

## Requirements

- Python 3.6 or higher
- pip (Python package installer)

### Dependencies
- click (for CLI interface)

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd log-archive-tool
```

2. Install the package:
```bash
pip install -e .
```

## Configuration

The tool can be configured using environment variables:

- `LOG_ARCHIVE_SOURCE`: Source directory for logs (default: `/var/log` on Linux)
- `LOG_ARCHIVE_DEST`: Destination directory for archives (default: `~/log_archives`)

### Setting Environment Variables:

**Linux/Mac:**
```bash
export LOG_ARCHIVE_SOURCE="/path/to/logs"
export LOG_ARCHIVE_DEST="/path/to/archives"
```

## Usage

The tool provides several commands for managing log archives:

### Archive Logs
Create a new archive of log files:
```bash
log-archive archive [--source SOURCE] [--dest DEST]
```

### Extract Archives
Extract a specific archive:
```bash
log-archive extract ARCHIVE_NAME [--extract-path PATH] [--archive-dir DIR]
```

### List Archives
View all available archives:
```bash
log-archive list [--archive-dir DIR]
```

### Help
Get help on available commands:
```bash
log-archive --help
log-archive COMMAND --help
```

## Command Options

### Archive Command
- `--source`, `-s`: Source directory containing logs
- `--dest`, `-d`: Destination directory for saving archives

### Extract Command
- `ARCHIVE_NAME`: Name of the archive to extract (required)
- `--extract-path`, `-p`: Path where to extract the archive
- `--archive-dir`, `-d`: Directory containing archives

## Development

To set up the development environment:

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
```

2. Install development dependencies:
```bash
pip install -r requirements.txt
```


## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

Feel free to open issues if you find any bugs or have feature requests!
