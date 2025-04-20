#!/bin/bash

# List of all URLs to test
urls=(
    "http://192.168.198.129:9999/stager1.py"
    "http://192.168.198.129:8080/clean.sh"
    "http://192.168.198.129:7777/stager2.py"
    "http://192.168.198.129:4444/stage1_rev.c"
    "http://192.168.198.129:5555/stage2_rev.c"
)

echo "[*] Testing server availability..."

for url in "${urls[@]}"; do
    status=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    if [ "$status" -eq 200 ]; then
        echo "[+] OK: $url"
    else
        echo "[!] ERROR $status: $url"
    fi
done

