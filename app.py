from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    data = request.get_json()
    number = float(data["number"])
    return jsonify({"result": number})


if __name__ == "__main__":
    app.run(debug=True)
