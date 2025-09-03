from flask import Flask, render_template, request
from numbers_set import NumbersSet

app = Flask(__name__)
numbers_set = NumbersSet()

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        if "manual" in request.form:
            num = request.form.get("manual_input")
            try:
                extracted = numbers_set.extract(int(num))
                message = f"Número extraído: {extracted}"
            except ValueError as e:
                message = str(e)
        elif "random" in request.form:
            extracted = numbers_set.extract()
            message = f"Número aleatorio extraído: {extracted}"

    grid = numbers_set.get_grid()
    return render_template("index.html", grid=grid, message=message)

if __name__ == "__main__":
    app.run(debug=True)
