from flask import Flask, render_template

app = Flask(__name__)

print("Joined Flask Framework ")


@app.route("/")
def home():
    print("물냉면 주문 받았어요!")
    return render_template("food1.html")


@app.route("/contact")
def contact():
    print("비빔냉면 주문 받았어요!")
    return render_template("food2.html")


app.run(debug=True)
