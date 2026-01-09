# backend/app.py

from flask import Flask, request, jsonify
from nash_parking import find_equilibrium

app = Flask(__name__)

@app.route("/nash", methods=["POST"])
def nash():
    spots = request.json["spots"]
    result = find_equilibrium(spots)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
