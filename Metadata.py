import os
import time

def extract_metadata(path):
    try:
        stats = os.stat(path)
        print(f"File: {path}")
        print(f"Size: {stats.st_size} bytes")
        print(f"Created: {time.ctime(stats.st_ctime)}")
        print(f"Modified: {time.ctime(stats.st_mtime)}")
        print(f"Accessed: {time.ctime(stats.st_atime)}")
    except Exception as e:
        print(f"Error: {e}")
