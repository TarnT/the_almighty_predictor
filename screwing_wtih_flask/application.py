import random, string
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("futureOfAI.html")

@app.route("/get_data", methods=["GET", "POST"])
def get_data():

    if request.method == "POST":
        age = int(request.form.get("age"))
        gender = request.form.get("gender")
        marital = request.form.get("marital")

        random_seq = "".join([random.choice(string.ascii_letters) for i in range(20)])
        avatar_url = f"https://avatars.dicebear.com/api/{gender}/{random_seq}.svg"

         # get predicted income

        return render_template("predicted.html", avatar_url=avatar_url, income="above 50000", marital=marital, age=age, gender=gender)

    
    else:
        return render_template("get_data.html")


if __name__ == "__main__":
    app.run()