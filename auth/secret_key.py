import secrets

# Generate a random key of 32 bytes (256 bits)
secret_key = secrets.token_hex(32)

print(secret_key)