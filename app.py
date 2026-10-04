from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    name = request.headers.get("X-MS-CLIENT-PRINCIPAL-NAME", "unknown user")
    return f"<h1>Hello World</h1><p>Signed in as: {name}</p>"
