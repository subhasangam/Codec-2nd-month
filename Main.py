from utils.metadata import extract_metadata
from utils.hashing import hash_file
from utils.hidden_files import find_hidden_files
from utils.keyword_search import search_keywords
import os

def main():
    filepath = input("Enter file/folder path: ")
    if os.path.isfile(filepath):
        print("\n[+] File Metadata:")
        extract_metadata(filepath)

        print("\n[+] File Hashes:")
        hash_file(filepath)

        print("\n[+] Keyword Search:")
        keyword = input("Enter keyword to search: ")
        search_keywords(filepath, keyword)

    elif os.path.isdir(filepath):
        print("\n[+] Searching for Hidden Files:")
        find_hidden_files(filepath)

    else:
        print("Invalid path!")

if __name__ == "__main__":
    main()
