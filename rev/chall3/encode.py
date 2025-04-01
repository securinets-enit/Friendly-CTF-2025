def xor_encrypt(data, key):
    return bytes(byte ^ key for byte in data)

def caesar_cipher(data, shift):
    return bytes((byte + shift) % 256 for byte in data)

def encrypt_flag(flag, key, shift):
    xor_encrypted = xor_encrypt(flag, key)  # XOR first
    final_encrypted = caesar_cipher(xor_encrypted, shift)  # Caesar cipher second
    return final_encrypted

if __name__ == "__main__":
    flag = b"SecurinetsENIT{1_th0ught_1_s41d_no_d3bugg1ng_h3r3}"
    key = 0xA5  # XOR key
    shift = 3  # Caesar cipher shift to the right
    
    encrypted_flag = encrypt_flag(flag, key, shift)
    
    print("Encrypted bytes:")
    print(", ".join(f"0x{byte:02X}" for byte in encrypted_flag))
