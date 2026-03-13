from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        essay = request.form["essay"]
        result = f"Essay received. Length: {len(essay)} characters"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)