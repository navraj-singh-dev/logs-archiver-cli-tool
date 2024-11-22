`_get_file_size` function in detail:

1. **Function Declaration and Purpose**

```python
def _get_file_size(self, file_path):
    """Get human-readable file size"""
```

- The underscore `_` means it's intended for internal use within the `LogArchiver` class
- Takes a file path as parameter and returns human-readable size
- docstring explains its purpose clearly

2. **Getting Raw File Size**

```python
size = os.path.getsize(file_path)
```

- Uses `os.path.getsize()` to get file size in bytes
- Returns a number like 1048576 (which is 1MB in bytes)

3. **Unit Conversion Loop**

```python
for unit in ['B', 'KB', 'MB', 'GB']:
```

- Creates a loop through size units from smallest to largest
- Starts with Bytes (B)
- Goes through Kilobytes (KB)
- Then Megabytes (MB)
- And finally Gigabytes (GB)

4. **Size Check and Return**

```python
if size < 1024:
    return f"{size:.2f} {unit}"
```

- Checks if current size is less than 1024 (which is 2^10)
- If true, size is small enough for current unit
- `.2f` formats number to 2 decimal places
- Returns formatted string like "123.45 MB"

5. **Size Reduction**

```python
size /= 1024
```

- If size is too big for current unit
- Divides by 1024 to convert to next unit
- Example: 1,048,576 bytes becomes 1024 KB, then 1 MB

6. **Terabyte Fallback**

```python
return f"{size:.2f} TB"
```

- If size is still big after GB
- Returns size in Terabytes (TB)
- This is the largest unit this function handles

Example outputs:

- For 900 bytes: "900.00 B"
- For 1500 bytes: "1.46 KB"
- For 1.5 million bytes: "1.43 MB"
- For 2 billion bytes: "1.86 GB"
- For huge files: "1.23 TB"

This function makes file sizes human-friendly instead of showing just raw bytes.
