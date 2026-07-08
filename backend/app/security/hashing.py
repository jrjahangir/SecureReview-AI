import hashlib

def calculate_sha256(file_bytes: bytes):

    sha256 = hashlib.sha256()

    sha256.update(file_bytes)

    return sha256.hexdigest()