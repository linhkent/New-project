from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, I'm again"
  
@app.route("/c4e25")
def c4e25():
    return "This is C4E25, happy coding!!!"

@app.route("/hi/quan")
def hi_me():
    return "Hello Quan"

@app.route("/hi/<name>")
def hi(name):
    return "HI " + name + ". Have a nice day."

@app.route("/add/<int:x>/<int:y>")
def add(x, y):
    return str(x + y)

@app.route("/simple_html")
def simple_html():
    return "<h3>Simple, indeed!!!!</h3>"

@app.route("/html")
def html():
    return render_template("sample.html")

food_list = [
  "Bun dau",
  "Bun cha",
  "Ga ran",
  "Nem lui",
]

@app.route("/menu")
def menu():
  return render_template("menu.html", food_list=food_list)

@app.route("/food/<int:index>")  # detail page
def food(index):
  return render_template("food.html", title=food_list[index])

detail = {
  'title': 'Bun cha',
  'image': 'https://img.taste.com.au/1HfSbEeh/w720-h480-cfill-q80/taste/2016/11/bun-cha-93944-1.jpeg'
}

@app.route("/food_detail")
def food_detail():
  return render_template("food_detail.html", detail=detail)

if __name__ == '__main__':
  app.run(debug=True)