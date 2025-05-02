from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import sqlite3
import uuid  # For generating nonces
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'super_secret_key_for_sessions'  # Different from JWT secret!

# Hidden flag
FLAG = "SecurinetsENIT{d37792903cb2b843867d375d17587dcf}"
# Database setup
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT UNIQUE NOT NULL,
                 email TEXT UNIQUE NOT NULL,
                 password_hash TEXT NOT NULL,
                 role TEXT DEFAULT 'user',
                 nonce TEXT,
                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

    # Add admin user if not exists
    try:
        nonce = str(uuid.uuid4())  # Generate nonce for admin
        c.execute("INSERT INTO users (username, email, password_hash, role, nonce) VALUES (?, ?, ?, ?, ?)",
                  ('admin', 'admin@company.com', generate_password_hash('super_secure_admin_pass_123'), 'admin', nonce))
    except sqlite3.IntegrityError:
        pass  # Admin already exists

    conn.commit()
    conn.close()


init_db()


# Routes
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if not all([username, email, password]):
            return render_template('register.html', error='All fields are required')

        try:
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            nonce = str(uuid.uuid4())  # Generate nonce for the new user
            c.execute("INSERT INTO users (username, email, password_hash, nonce) VALUES (?, ?, ?, ?)",
                      (username, email, generate_password_hash(password), nonce))
            conn.commit()

            return redirect(url_for('login'))

        except sqlite3.IntegrityError:
            return render_template('register.html', error='Username or email already exists')
        finally:
            conn.close()

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT username, password_hash, role FROM users WHERE username = ?", (username,))
        user = c.fetchone()
        conn.close()

        if user and check_password_hash(user[1], password):
            session['username'] = user[0]
            session['role'] = user[2]
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    return render_template('dashboard.html',
                           username=session['username'],
                           role=session['role'])


@app.route('/admin_8c6af10764d7ad9948ee687bbc318d7a')
def admin_panel():


    return f"Welcome Admin!  TFADEL HAW LFLAG:  {FLAG}"


@app.route('/admin')
def admin():
    return "Nice try fellow Hacker! what file is accessed by web crawlers crawl crawl more"


@app.route('/robots.txt')
def robots():
    return """User-agent: *
Disallow: /admin
Allow: /admin_8c6af10764d7ad9948ee687bbc318d7a
Disallow: /register
Disallow: /login
"""


# API endpoints (for AJAX)
@app.route('/api/userinfo')
def user_info():
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized'}), 401

    return jsonify({
        'username': session['username'],
        'role': session['role']
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
