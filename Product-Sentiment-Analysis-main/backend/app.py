from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    result = ""

    if request.method == "POST":
        review = request.form["review"]

        if "good" in review.lower() or "amazing" in review.lower():
            result = "Positive 😊"
        elif "bad" in review.lower():
            result = "Negative 😠"
        else:
            result = "Neutral 😐"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)