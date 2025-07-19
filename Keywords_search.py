def search_keywords(filepath, keyword):
    try:
        with open(filepath, 'r', errors='ignore') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if keyword in line:
                    print(f"[Line {i+1}] {line.strip()}")
    except Exception as e:
        print(f"Error reading file: {e}")
