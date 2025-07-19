import os

def find_hidden_files(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name.startswith('.'):
                print(f"Hidden File: {os.path.join(root, name)}")
