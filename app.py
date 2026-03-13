from flask import Flask, render_template, request
from detector import detect_ai

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        essay = request.form["essay"]
        result = detect_ai(essay)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)