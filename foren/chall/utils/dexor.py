import base64

def xor_decrypt(b64_data, key):
    raw = base64.b64decode(b64_data)
    return ''.join([chr(c ^ key) for c in raw])

# Example encrypted strings (replace these with your own if needed)
encrypted_payload = "c3twbHN0emxze3psc3B7eHV1dXVtMTYjJScwcGwyOw=="
encrypted_compressor = "c3twbHN0emxze3psc3B7eHZ2dnZtMTYjJSdwHTAnNGwh"

# XOR key used for encryption
key = 0x42

# Decrypt
print("Decrypted payload URL:", xor_decrypt(encrypted_payload, key))
print("Decrypted compressor URL:", xor_decrypt(encrypted_compressor, key))

