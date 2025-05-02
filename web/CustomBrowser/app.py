from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent', '')
    remote_addr = request.remote_addr  # For demo (in production, check X-Forwarded-For from Tor)

    response = make_response("This service is restricted to our authorized agents only hihihi ;).")

    # Normal headers (distractions)
    response.headers['Server'] = 'Apache/2.4.41 (Onion)'
    response.headers['X-Powered-By'] = 'SecurinetsENIT-PROTECTED'
    response.headers['Warning'] = 'Unauthorized access logged'

    # Tor Browser's User-Agent contains "Tor"
    if "SecurinetsENIT" in user_agent:
        response.headers['X-Flag'] = 'SecurinetsENIT{6d94cde11cea6f13c8721704763a8195}'
    else:
        response.headers['X-Access-Denied'] = 'Only use our custom browser you can ask our navigation secret keeper salamnki for the binary'

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)