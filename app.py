from flask import Flask, request, jsonify, send_from_directory
from nash_parking import find_equilibrium

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/map")
def map_page():
    return send_from_directory(".", "map.html")

@app.route("/nash", methods=["POST"])
def nash():
    spots = request.json["spots"]
    result = find_equilibrium(spots)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
