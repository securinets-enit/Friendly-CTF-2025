from flask import Flask, request, render_template
import re
import os
app = Flask(__name__)

FORBIDDEN = ['&', '||', ';', '$', '>', '<', '(', ')', 
            '{', '}', '[', ']', '\\', '\'', '"', 'cat', 'ls','\n','\'']

def sanitize_input(url):
    # Remove forbidden characters
    for char in FORBIDDEN:
        url = url.replace(char, '')
    
    # Extract domain
    domain = re.sub(r'^https?://', '', url, flags=re.IGNORECASE)
    domain = domain.split('/')[0].split('?')[0].split(':')[0]
    
    
    
    if '.' not in domain or domain.startswith('.') or domain.endswith('.'):
        return None
    
    return domain

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    result_class = 'error'
    
    if request.method == 'POST':
        url = request.form.get('url', '').strip()
        domain = sanitize_input(url)
        
        if not domain:
            result = "Invalid URL format!"
        else:
            try:
                # Execute dig command
                exit_code = os.system(f"dig +short {domain} | grep . >/dev/null && exit 0 || exit 1")


                if exit_code == 0:
                    result = f"Site is up! "
                    result_class = 'success'
                else:
                    result = "DNS lookup failed!"
                    
            
            except Exception as e:
                result = f"Server error: {str(e)}"
    
    return render_template('index.html', result=result, result_class=result_class)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
