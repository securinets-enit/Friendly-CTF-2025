# Writeup

# Description

The idea behind this challenge is a **multi-staged**, little-obfuscated compression script that compresses the file as the user expects but also downloads two stagers to be saved in a legit-looking /tmp directory belonging to systemd. Then, using a bash script, reassemble the C codes obtained from both portals, compiles them and run the resulting binary to get a reverse shell written in C. Upon successful connection, it deletes itself and the whole added /tmp directory.


The players will be given the **zlib_compressor.py** file and is asked to respond to the asker.


Since the downloaded files get deleted too quickly, the player can debug the program to obtain the source codes of the stagers and cleaning script. This step may be included in the writeup but it's not the main focus of the challenge.


