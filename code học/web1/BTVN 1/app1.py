from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/bmi/<int:w>/<int:h>")
# def bmi(w, h):
#     h1 = h/100
#     bmi = w / (h1 * h1)
#     if bmi < 16:
#         return "Severely underweight"
#     elif bmi < 18.5:
#         return "Underweight"
#     elif bmi < 25:
#         return "Normal"
#     elif bmi < 30: 
#         return "Overweight"
#     else:
#         return "Obese"

@app.route("/bmi/<int:w>/<int:h>")
def bmi(w, h):
    h1 = h / 100
    bmi = w / (h1 * h1)
    return render_template("bmi.html", bmi=bmi)

if __name__ == '__main__':
  app.run(debug=True)