from flask import Flask, render_template, session
app = Flask(__name__)

@app.route("/")
def home():
    return "OK"

if __name__ == "__main__":
    app.run()