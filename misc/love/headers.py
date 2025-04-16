import os
import struct

def fix_wav_headers_in_dir():
    for filename in os.listdir('.'):
        if filename.lower().endswith('.wav'):
            try:
                filesize = os.path.getsize(filename)
                riff_chunk_size = filesize - 8

                # Convert to 4-byte little-endian
                packed = struct.pack('<I', riff_chunk_size)
                hex_repr = ' '.join(f'{byte:02x}' for byte in packed)

                # Patch the header
                with open(filename, 'r+b') as f:
                    f.seek(4)
                    f.write(packed)

                print(f"[+] {filename} | Size: {filesize} bytes | ChunkSize: {riff_chunk_size} | Hex: {hex_repr}")

            except Exception as e:
                print(f"[!] Error processing {filename}: {e}")

if __name__ == "__main__":
    fix_wav_headers_in_dir()

