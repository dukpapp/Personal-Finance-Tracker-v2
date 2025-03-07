from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import session, Transaction
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    transactions = session.query(Transaction).all()
    
    # Prepare data for Chart.js
    chart_data = {
        "dates": [t.date.strftime('%d-%m-%Y') for t in transactions],
        "amounts": [t.amount for t in transactions],
        "categories": [t.category for t in transactions]
    }
    
    return render_template("index.html", transactions=transactions, chart_data=chart_data)

@app.route('/add', methods=["GET", "POST"])
def add_transaction():
    if request.method == "POST":
        date = datetime.strptime(request.form["date"], "%Y-%m-%d")
        amount = float(request.form["amount"])
        category = request.form["category"]
        description = request.form["description"]

        new_transaction = Transaction(date=date, amount=amount, category=category, description=description)
        session.add(new_transaction)
        session.commit()
        return redirect(url_for("index"))
    
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)
