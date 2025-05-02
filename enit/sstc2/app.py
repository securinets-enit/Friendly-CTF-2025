from flask import Flask, render_template_string, request, redirect
import os
import base64
import random
import string
from jinja2.exceptions import TemplateSyntaxError 
import re
app = Flask(__name__)



def encrypt(data: str) -> str:
    res = "".join(random.choices(string.ascii_letters + string.digits, k=20))
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
    encrypted_flag =  encrypt(os.environ.get("FLAG"))
    original = re.sub(r'[_\[\]\.]|\|join|base|mro|class', "", original) 
    try :
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
    except TemplateSyntaxError:
        return render_template_string(""" <!doctype html> <h1 style="font-size:100px;" align="center">""" + "plz no hack" + """</h1>""", ) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
