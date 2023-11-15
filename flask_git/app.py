from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hi():
    return "Welocme to calculator api"


@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    result = data["operand1"] + data["operand2"]
    return jsonify({"result": result})


@app.route("/subtract", methods=["POST"])
def subtract():
    data = request.get_json()
    result = data["operand1"] - data["operand2"]
    return jsonify({"result": result})


@app.route("/multiply", methods=["POST"])
def multiply():
    data = request.get_json()
    result = data["operand1"] * data["operand2"]
    return jsonify({"result": result})


@app.route("/divide", methods=["POST"])
def divide():
    data = request.get_json()
    operand2 = data["operand2"]

    if operand2 == 0:
        return jsonify({"error": "Cannot divide by zero!"}), 400

    result = data["operand1"] / operand2
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")
