import hashlib

def hash_file(filepath):
    with open(filepath, "rb") as f:
        data = f.read()
        print(f"MD5: {hashlib.md5(data).hexdigest()}")
        print(f"SHA1: {hashlib.sha1(data).hexdigest()}")
        print(f"SHA256: {hashlib.sha256(data).hexdigest()}")
