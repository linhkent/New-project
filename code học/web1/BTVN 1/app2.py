from flask import Flask, render_template

app = Flask(__name__)

users = {
    "huy": {
        "name": "huy",
        "age": 20
    },
    "quan": {
        "name": "quan",
        "age": 19
    }
}


@app.route("/user/<username>")
def user_check(username):
    if username in users:
        return render_template("user.html", username=users[username])
    else:
        return "<h3>User not Found</h3>"



if __name__ == '__main__':
  app.run(debug=True)
