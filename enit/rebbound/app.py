from flask import Flask, render_template, request, session, redirect, url_for, send_file
import uuid, os, re, socket, requests
from urllib.parse import urlparse
import ipaddress

app = Flask(__name__)
app.secret_key = os.urandom(64)

# --- users & files setup ---
users = {
    "test": {"password": "69testpass420", "uuid": str(uuid.uuid4()), "files": []},
    "admin": {"password": os.urandom(64),       "uuid": str(uuid.uuid4()), "files": []}
}
flag = "FL1TZ{th1s_1s_Just_4_w4rmup}"

os.makedirs("files", exist_ok=True)
for u in users.values():
    os.makedirs(f"files/{u['uuid']}", exist_ok=True)

with open(f"files/{users['admin']['uuid']}/flag.txt", "w") as f:
    f.write(f"welcome admin here is your flag: {flag}")

# --- utility funcs ---
def is_private(ip_str):
    try:
        ip = ipaddress.ip_address(ip_str)
        return ip.is_private or ip.is_loopback or ip.is_link_local
    except ValueError:
        return True

# --- routes ---
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u, p = request.form.get("username"), request.form.get("password")
        if u in users and users[u]["password"] == p:
            session["username"] = u
            return redirect(url_for("dashboard"))
        return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        u, p = request.form.get("username"), request.form.get("password")
        if not u or not p:
            return render_template("signup.html", error="Username and password are required")
        if u in users:
            return render_template("signup.html", error="Username already exists")
        uid = str(uuid.uuid4())
        users[u] = {"password": p, "uuid": uid, "files": []}
        os.makedirs(f"files/{uid}", exist_ok=True)
        return redirect(url_for("login"))
    return render_template("signup.html")

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))
    u = session["username"]
    uid = users[u]["uuid"]
    files = os.listdir(f"files/{uid}")
    return render_template("dashboard.html", username=u, user_uuid=uid, files=files)

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

pattern = re.compile(r'^[a-z0-9]+\.fl1tz\.me')

@app.route("/submit-url", methods=["POST"])
def submit_url():
    # auth check
    if "username" not in session:
        return redirect(url_for("login"))

    user = session["username"]
    user_uuid = users[user]["uuid"]

    file_url = request.form.get("url", "").strip()
    if not file_url:
        return "No URL provided", 400

    parsed = urlparse(file_url)
    host = parsed.hostname
    if "127" in host:
        return "plz no hack"
    if not host or not pattern.match(host):
        return "Only fl1tz.me subdomains allowed", 403

    # DNS resolution
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        return "DNS lookup failed", 400

    # Build headers only if pointing to localhost
    headers = {}
    if ip == "127.0.0.1":
        headers["X-Ghr4b69-Request-Ip"] = "127.0.0.1"

    # Fetch
    try:
        resp = requests.get(file_url, headers=headers, timeout=5)
        resp.raise_for_status()
    except Exception as e:
        return f"Error fetching URL: {e}", 403

    # Save under a random name
    os.makedirs(f"files/{user_uuid}", exist_ok=True)
    safe_name = parsed.path.rsplit("/",1)[-1] or f"html_{uuid.uuid4().hex}.txt"
    with open(f"files/{user_uuid}/{safe_name}", "w", encoding="utf-8") as fd:
        fd.write(resp.text)

    return resp.text

@app.route("/files/<user_uuid>/<filename>")
def serve_file(user_uuid, filename):
    p = f"files/{user_uuid}/{filename}"
    if os.path.exists(p):
        return send_file(p, mimetype="text/plain")
    return "File not found", 404

@app.route("/users")
def list_users():
    # trust only the real REMOTE_ADDR or our fake header if loopback SSRF ran
    real_ip = request.headers.get("X-Ghr4b69-Request-Ip", request.remote_addr)
    if real_ip != "127.0.0.1":
        return "Forbidden", 403
    return {
        user: {"uuid": users[user]["uuid"]}
        for user in ("test","admin")
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
