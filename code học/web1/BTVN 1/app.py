from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route("/about_me")
def introduce():
    return render_template("about_me.html")

@app.route("/school")
def school():
  return redirect("http://techkids.vn")

if __name__ == '__main__':
  app.run(debug=True)