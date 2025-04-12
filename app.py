from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    return render_template("prediction.html")

if __name__ == "__main__":
    app.run()
