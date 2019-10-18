import logging
from name import app

from flask import request, jsonify

@app.route('/', methods=['GET'])
def default_route():
    return "Let's Go Team 1"

if __name__ == "__main__":
    app.run(debug=True)
