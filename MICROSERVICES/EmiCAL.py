from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def emi():
    emi = None

    if request.method == "POST":
        principal = float(request.form["principal"])
        rate = float(request.form["rate"])
        years = int(request.form["years"])

        monthly_rate = rate / (12 * 100)
        months = years * 12

        emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

    return render_template("index.html", emi=emi)

if __name__ == "__main__":
    app.run(debug=True)