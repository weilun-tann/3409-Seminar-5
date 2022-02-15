import keras
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", result="GET")

    attr1 = float(request.form.get("attr1"))
    attr2 = float(request.form.get("attr2"))
    attr3 = float(request.form.get("attr3"))
    model = keras.models.load_model("src/bankruptcy")
    results = model.predict([[attr1, attr2, attr3]])
    return render_template("index.html", result=str(results[0]))


if __name__ == "__main__":
    app.debug = True
    app.run()
