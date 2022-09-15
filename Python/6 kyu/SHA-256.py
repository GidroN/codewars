from hashlib import sha256

def to_sha256(string: str) -> str:
    return sha256(string.encode('utf-8')).hexdigest()
