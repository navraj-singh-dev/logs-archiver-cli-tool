`_create_metadata` function in detail with examples:

1. **Function Purpose**:

```python
def _create_metadata(self, archive_name, timestamp):
    """Create metadata file for the archive"""
```

- Creates a separate text file with information about the archive
- The underscore `_` means it's intended for internal use
- Takes two parameters: archive name and when it was created
- Lives inside the LogArchiver class

2. **Creating Metadata Path**:

```python
metadata_path = self.archive_dir / f"{archive_name}_metadata.txt"
```

- Uses `self.archive_dir` (example: "C:/Users/You/log_archives")
- Adds archive name with "\_metadata.txt" at end
- Example path:
  - If archive_name is "logs_20_11_2024\_\_15_30_45.tar.gz"
  - Result: "C:/Users/You/log_archives/logs_20_11_2024\_\_15_30_45.tar.gz_metadata.txt"

3. **Opening File for Writing**:

```python
with open(metadata_path, 'w') as f:
```

- 'w' means write mode (creates new file or overwrites existing)
- Uses `with` for automatic file closing
- Creates a new text file at metadata_path

4. **Writing Archive Creation Time**:

```python
f.write(f"Archive Created: {timestamp}\n")
```

- Writes when archive was created
- `\n` adds a new line
- Example output:
  ```
  Archive Created: 20_11_2024__15_30_45
  ```

5. **Writing Source Directory**:

```python
f.write(f"Source Directory: {self.source_dir}\n")
```

- Records where log files came from
- Example output:
  ```
  Source Directory: C:/var/log
  ```

6. **Writing Archive Location**:

```python
f.write(f"Archive Location: {self.archive_dir / archive_name}\n")
```

- Shows where the actual archive is stored
- Example output:
  ```
  Archive Location: C:/Users/You/log_archives/logs_20_11_2024__15_30_45.tar.gz
  ```

7. **Complete Metadata File Example**:

```
Archive Created: 20_11_2024__15_30_45
Source Directory: C:/var/log
Archive Location: C:/Users/You/log_archives/logs_20_11_2024__15_30_45.tar.gz
```

8. **Why This is Useful**:

- Helps track when archives were created
- Shows where files originally came from
- Makes it easy to find the actual archive file
- Useful for auditing and tracking
- Helps when extracting files later

9. **Error Handling**:

- File operations automatically handled by `with` statement
- If writing fails, file will be properly closed
- Parent function will catch any file-related errors

10. **Important Notes**:

- Metadata file is separate from archive
- Uses plain text for easy reading
- Names are linked to archive for easy reference
- Creates one metadata file per archive
