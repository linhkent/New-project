from flask import Flask, request, render_template, redirect, flash, session
import mlab

from models.food import Food
from models.user import User

app = Flask(__name__)
app.config["SECRET_KEY"] = "aajlajfkaf"
mlab.connect()

# f_list = [
#   {
#     "title": "Com",
#     "link": "https:via.placeholder.com/200x200"
#   },
#   {
#     "title": "Pho",
#     "link": "https:via.placeholder.com/200x200"
#   }
# ]

@app.route("/menu")
def menu():
  if "token" in session:
    food_objects = Food.objects()
    return render_template("menu.html", food_list = food_objects)
  else:
    return "Forbidden"

@app.route("/food/<food_id>")
def food_detail(food_id):
  f = Food.objects().with_id(food_id)
  # Invalid Id, Not Found
  return render_template("food_detail.html", food = f)

@app.route("/update_food/<food_id>", methods = ["GET", "POST"])
def update_food(food_id):
  f = Food.objects().with_id(food_id)
  if request.method == "GET":
    return render_template("update_food_form.html", food = f)
  elif request.method == "POST":
    form = request.form
    t = form["title"]
    l = form["link"]
    # Update
    f.update(set__title=t, set__link=l)
    f.reload
    return "Gotcha"

@app.route("/login", methods = ["GET", "POST"])
def login():
  if request.method == "GET":
    return render_template("login.html")
  elif request.method == "POST":
    form = request.form
    u = form["username"]
    p = form["password"]
    # if u == "c4e" and p == "codethechange":
    #   user = User(username = u, password = p)
    #   user.save
    #   return "Done"
    # else:
    #   return redirect("/login")
    user = User.objects(username=u).first()
    if user != None:
      # user ton tai
      # check password
      if user.password == p:
        session["token"] = u
        return redirect("/menu")
      else:
        flash("Invalid Password")
        return render_template("login.html")
    else:
      # user k ton tai
      flash("User not found")
      return render_template("login.html")


@app.route("/logout")
def logout():
  if "token" in session:
    del session["token"]
    return redirect("/login")
  else:
    return redirect("/login")

#1 Open both methods, GET, POST. (using "methods=" )
@app.route('/add_food', methods=["GET", "POST"])
def add_food():
  if request.method == "GET":
      return render_template("food_form.html")
  elif request.method == "POST":
      form = request.form   # form la kieu dictionary   # form hay user trong register la ten dict, request.form thi form la form o trong file html
      # print(form)
      t = form["title"]
      l = form["link"]
      # print(t, l)
      f = Food(title = t, link = l)
      f.save()
      
      return redirect("/food/" + str(f.id))

@app.route('/register', methods=["GET", "POST"])
def register():
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