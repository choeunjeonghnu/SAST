from flask import Flask, request

app = Flask(__name__)

@app.route("/greet")
def greet():
    name = request.args.get("name")
    return f"Hello {name}!"  # XSS 취약점 예제

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
