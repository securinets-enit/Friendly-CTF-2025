from flask import Flask, request, render_template, session, redirect, url_for, flash
import sqlite3
import os
import re

app = Flask(__name__)
app.secret_key = 'secretkeyy1$'

DB_PATH = "/app/users.db"

# Initialize DB
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', 'adminPASSW$')")
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('Taha', 'TahaMarouani@samirloussif')")
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('Hidri', 'HidriLovesSQL1Inject1on')")
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    query = None  # store query for debug display

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        #  Vulnerable query (intended for SQLi)
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        try:
            c.execute(query)
            user = c.fetchone()
            conn.close()
            if user:
                session['username'] = user[1]
                session['user_id'] = user[0]
                return redirect(url_for('ping'))
            else:
                error = "Invalid credentials!"
        except sqlite3.Error as e:
            # Show the exact query AND the error — to encourage error-based SQLi
            error = f"Database error: {e}<br><code>{query}</code>"
            conn.close()

    return render_template("login.html",
                           title="Login",
                           subtitle="Access the Ping Machine",
                           error=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_id', None)
    return redirect(url_for('login'))


@app.route('/ping', methods=['GET', 'POST'])
def ping():
    if 'username' not in session:
        return redirect(url_for('login'))

    user = session['username']
    output = None
    ip = request.form.get('ip') if request.method == 'POST' else None

    if user == 'Hidri' and ip:
        if re.search(r'[&|>`]', ip) or 'rm' in ip:
            flash("Blocked command detected!", 'error')
        else:
            command = f"/bin/sh -c 'ping -c 2 {ip}'"
            output = os.popen(command).read()

    return render_template("ping.html",
                           title="Ping Machine",
                           user=user,
                           user_id=session.get('user_id'),
                           ip=ip if ip else '8.8.8.8',
                           output=output)


@app.route('/user/<int:user_id>')
def get_user(user_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    username = None
    error = None

    try:
        query = f"SELECT username FROM users WHERE id = {user_id}"
        c.execute(query)
        user = c.fetchone()
        if user:
            username = user[0]
    except sqlite3.Error as e:
        error = str(e)
    finally:
        conn.close()

    return render_template("user.html",
                           title="User Details",
                           user_id=user_id,
                           username=username,
                           error=error)


init_db()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
