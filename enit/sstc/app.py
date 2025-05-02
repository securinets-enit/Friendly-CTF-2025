from flask import Flask, render_template_string, request, redirect
import os
import base64
from markupsafe import escape
import random

app = Flask(__name__)

KEY = os.environ.get("KEY")

def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text

def deterministic_padding(input_text, length=25):
    """
    Adds deterministic padding to make the encrypted message exactly `length` characters long.
    Padding is derived from the input text to ensure consistency.
    """
    random.seed(sum(ord(c) for c in input_text))
    padding_chars = ""
    for _ in range(length - len(input_text)):
        padding_chars += chr(random.randint(33, 126))  # Random printable ASCII character
    return padding_chars

def encrypt_with_padding(plaintext, text_key):
    """
    Encrypts the given plaintext using the dynamic_xor_encrypt function and ensures
    the output is exactly 25 characters long.
    """
    encrypted_text = dynamic_xor_encrypt(plaintext, text_key)
    if len(encrypted_text) > 25:
        encrypted_text = encrypted_text[-25:]
    if len(encrypted_text) < 25:
        padding = deterministic_padding(encrypted_text, length=25)
        encrypted_text += padding
    return encrypted_text

def encrypt(data: str) -> str:
    xor = encrypt_with_padding(data, KEY)
    encrypted = []
    for i, char in enumerate(xor):
        # Shift character by the fixed key and add index-based shift
        shifted_char = chr((ord(char) + 69 + i) % 256)
        encrypted.append(shifted_char)
    res = ''.join(encrypted)
    return base64.b64encode(res.encode("utf-8")).decode("utf-8")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect('/encrypt', code=307)
    else:
        return render_template_string("""<!doctype html>
<title>Secure Encryption Service</title>
<h1>🔒 Secure Encryption Service</h1>
<p>I built a secure encryption service that lets you encrypt whatever you want!</p>
<form action="/" method="POST">
What do you want to encrypt: <input name="text" id="text"><br>
<button type="submit">Encrypt</button>
</form>
<p style="font-size:10px;position:fixed;bottom:10px;left:10px;">
*Note: This service also encrypts the flag for you</p>
""")

@app.route("/encrypt", methods=["POST"])
def encrypt_page():
    original = request.form.get("text", "")
    encrypted_text = encrypt(original)
    encrypted_flag =encrypt( os.environ.get("FLAG"))
 # This would be replaced with actual flag encryption
    
    return render_template_string("""<!doctype html>
    
<title>Encryption Results</title>
<h1>Encryption Results</h1>
<p><strong>Original:</strong>"""+  original  +"""</p>
<div class="encrypted">
    <p><strong>Your encrypted text:</strong> {{ encrypted_text }}</p>
    <p><strong>Flag encrypted text:</strong> {{ encrypted_flag }}</p>
</div>
<a href="/">Back to encryption</a>
""", original=original, encrypted_text=encrypted_text, encrypted_flag=encrypted_flag)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
