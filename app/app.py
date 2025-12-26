from flask import Flask, render_template, request, abort
import subprocess
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ping", methods=["POST"])
def ping():
    host = request.form.get("host")

    # ✅ Validation بسيطة (غير domain أو IP)
    if not host or not re.match(r"^[a-zA-Z0-9\.\-]+$", host):
        abort(400, "Invalid host")

    # ✅ Secure subprocess (no shell=True)
    result = subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True,
        text=True,
        timeout=5
    )

    return f"<pre>{result.stdout}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
