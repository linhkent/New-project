from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/register', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        user = request.form
        u = user["username"]
        p = user["password"]
        print(u, p)
        return "Registered"
  
if __name__ == '__main__':
  app.run(debug=True)