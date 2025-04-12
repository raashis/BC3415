from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/dbs", methods=["POST"])
def predict():
    exchange_rate = float(request.form["q"])
    predicted_price = round(exchange_rate * 1.5, 2)  # Dummy prediction logic
    return f"Predicted DBS Share Price: SGD {predicted_price}"

if __name__ == "__main__":
    app.run(debug=True)
