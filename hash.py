import hashlib

def id_to_sha256(id_value):
    # Convert the ID to a string and then encode to bytes (UTF-8 is standard)
    input_bytes = str(id_value).encode('utf-8')
    # Create a new SHA256 hash object
    hash_object = hashlib.sha256(input_bytes)
    # Get the hexadecimal representation of the hash
    hex_digest = hash_object.hexdigest()
    return hex_digest

# Example usage:
my_id = "STU026"
hashed_id = id_to_sha256(my_id)
print(f"Original ID: {my_id}")
print(f"SHA-256 Hash: {hashed_id}")

