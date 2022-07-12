import os
from flask import Flask
import jsonify, requests
from math import sqrt

app = Flask(__name__)


@app.route('/')
def nao_entre_em_panico():

    primos = "Tudo vaidar certo, caros alunos"

    return primos


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)
