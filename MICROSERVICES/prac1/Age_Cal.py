from flask import Flask, render_template, request
from datetime import date, datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def age():
    age = None

    if request.method == 'POST':
        dob = request.form['dob']

        birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
        today = date.today()

        age = today.year - birth_date.year

        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

    return render_template('AGE.html', age=age)

if __name__ == "__main__":
    app.run(debug=True)