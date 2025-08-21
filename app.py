from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    num1 = int(request.form["num1"])
    num2 = int(request.form["num2"])
    result = num1 + num2
    return render_template("result.html", num1=num1, num2=num2, result=result)

if __name__ == "__main__":
    app.run(debug=True)
