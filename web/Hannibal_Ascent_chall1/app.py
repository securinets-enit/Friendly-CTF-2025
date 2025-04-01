from flask import Flask, request, render_template_string, session, redirect, url_for
import sqlite3
import os
import re

app = Flask(__name__)
app.secret_key = 'secretkeyy1$'  # Set a secret key for session management

DB_PATH = "/app/users.db"


# Initialize SQLite database
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', 'adminPASSW$')")
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('Taha', 'TahaMarouani@samirloussif')")
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('Hidri', 'HidriLovesSQL1Inject1on')")
    conn.commit()
    conn.close()


# Landing page redirects to login
@app.route('/')
def index():
    return redirect(url_for('login'))


# Simple HTML layout with Bootstrap and background image
login_page = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hannibal's Ascent - Login</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-image: url('https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
            background-size: cover;
            background-position: center;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0;
        }
        .login-container {
            background: rgba(255, 255, 255, 0.9);
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 450px;
            text-align: center;
        }
        .login-container img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
        }
        .login-container h2 {
            margin-bottom: 1rem;
            color: #333;
        }
        .form-control {
            margin-bottom: 1rem;
        }
        .btn-primary {
            width: 100%;
        }
        .error {
            color: red;
            font-weight: bold;
        }
        .banner {
            width: 100%;
            max-height: 80px;
            margin-bottom: 15px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <img src="https://your-securinets-banner-url.com/banner.png" class="banner" alt="Securinets ENIT Banner">
        <h2>Hannibal's Ascent: The Ping Machine Mission 🚀</h2>
        <p>Hannibal, the legendary tactician, has set his sights beyond the Alps—this time, his ambition stretches to the stars. 
        But there’s a problem… His launch system is locked behind a mysterious control panel, a relic from an ancient cyber civilization. 
        The only tool at our disposal? A ping machine—a seemingly harmless diagnostic tool that might just hold the key to unleashing his cosmic journey.</p>
        <img src="https://your-hannibal-image-url.com/hannibal.jpg" alt="Hannibal the Conqueror">
        <p>Your mission: Hack the system, manipulate the ping machine, and exploit its weaknesses. Find the hidden backdoor, 
        break it, and rewrite history by sending Hannibal into space! 🚀✨</p>
        <form method="POST">
            <div class="mb-3">
                <input type="text" class="form-control" name="username" placeholder="Username" required>
            </div>
            <div class="mb-3">
                <input type="password" class="form-control" name="password" placeholder="Password" required>
            </div>
            <button type="submit" class="btn btn-primary">Login</button>
        </form>
        {% if message %}
            <p class="{{'error' if 'Invalid' in message else 'success'}} mt-3">{{ message }}</p>
        {% endif %}
    </div>
</body>
</html>
'''


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Vulnerable SQL query (intentional for CTF)
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute(query)
        user = c.fetchone()
        conn.close()

        if user:
            session['username'] = user[1]  # Store username in session
            return redirect(url_for('ping'))
        else:
            message = "Invalid credentials!"

    return render_template_string(login_page, message=message)


@app.route('/logout')
def logout():
    session.pop('username', None)  # Clear the session
    return redirect(url_for('login'))


@app.route('/ping', methods=['GET', 'POST'])
def ping():
    if 'username' not in session:
        return redirect(url_for('login'))

    user = session['username']
    ip = request.form.get('ip', '8.8.8.8')  # Default IP to ping

    if user == 'Hidri':
        if request.method == 'POST':
            # Prevent destructive commands but allow reading files
            if re.search(r'[&|>`]', ip) or 'rm' in ip:
                return "<h3 style='color:red;'>Blocked command detected! Action will be reported.</h3>"

            command = f"/bin/sh -c 'ping -c 4 {ip}'"
            output = os.popen(command).read()
            return render_template_string('''
                <div style="background: rgba(255, 255, 255, 0.8); padding: 2rem; border-radius: 10px; 
                            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); width: 100%; max-width: 600px; margin: 2rem auto;">
                    <h1>Ping Results for {{ ip }}</h1>
                    <pre>{{ output }}</pre>
                    <a href="/ping" class="btn btn-primary">Back</a>
                </div>
            ''', ip=ip, output=output)
        else:
            return render_template_string('''
                <div style="background: rgba(255, 255, 255, 0.8); padding: 2rem; border-radius: 10px; 
                            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); width: 100%; max-width: 600px; margin: 2rem auto;">
                    <h1>Welcome, {{ user }}!</h1>
                    <form method="POST">
                        <div class="mb-3">
                            <label for="ip" class="form-label">Enter IP Address:</label>
                            <input type="text" class="form-control" name="ip" placeholder="e.g., 8.8.8.8" required>
                        </div>
                        <button type="submit" class="btn btn-primary">Ping</button>
                    </form>
                    <a href="/logout" class="btn btn-danger mt-3">Logout</a>
                </div>
            ''', user=user)


# Initialize the database
init_db()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
