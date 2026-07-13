from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    username = None

    if request.method == "POST":
        username = request.form.get("username", "")

    return render_template("hellostring.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)