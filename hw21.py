from flask import Flask, jsonify, request
from datetime import datetime, date

app = Flask(__name__)

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

@app.route("/age", methods = ['POST'])
def age():
    if request.method == 'POST':
        try:
            day = request.form.get('day')
            print(day)
            date_of_birth = datetime.strptime(day, "%d-%m-%Y")
            print(date_of_birth)
            return jsonify({ 'birthday': day, 'age': calculate_age(date_of_birth)})
            pass
        except Exception as e:
            return jsonify({ 'birthday': str(e), 'age': str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True, port=5000)
