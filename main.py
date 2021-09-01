import os
import math
import statistics as s
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask.wrappers import Response

app = Flask(__name__)
CORS(app)

#TODO AQUIIIIII PROFESSOORRRRR S2
@app.route('/')
def verificar_api():
    return "Ta funfando", 200


@app.route('/api/calculadora/raizquadrada', methods=['GET'])
def getRaiz():
    num = request.args['num']
    response = {"operacao": "raiz quadrada", "resultado": math.sqrt(int(num))}
    return response, 20


@app.route('/api/calculadora/media/aritmetica', methods=['GET'])
def getMediaAritmetica():
    num1 = request.args['num1']
    num2 = request.args['num2']
    num3 = request.args['num3']
    num4 = request.args['num4']
    num5 = request.args['num5']

    result = s.mean([int(num1), int(num2), int(num3), int(num4), int(num5)])

    response = {"Media aritmetica": result}

    return response, 200

@app.route('/api/calculadora/media/harmonica', methods=['GET'])
def getMediaHarmonica():
    num1 = request.args['num1']
    num2 = request.args['num2']
    num3 = request.args['num3']
    num4 = request.args['num4']
    num5 = request.args['num5']

    result = s.harmonic_mean([int(num1), int(num2), int(num3), int(num4), int(num5)])

    response = {"Media harmonica": result}

    return response, 200

@app.route('/api/calculadora/moda', methods=['GET'])
def getModa():
    num1 = request.args['num1']
    num2 = request.args['num2']
    num3 = request.args['num3']
    num4 = request.args['num4']
    num5 = request.args['num5']

    result = s.mode([int(num1), int(num2), int(num3), int(num4), int(num5)])

    response = {"Moda": result}

    return response, 200


@app.route('/api/calculadora/somar', methods=['GET'])
def getSoma():
    num1 = request.args['num1']
    num2 = request.args['num2']

    result = int(num1) + int(num2)

    response = {"Somar": result}

    return response, 200

@app.route('/api/calculadora/subtrair', methods=['GET'])
def getSubtracao():
    num1 = request.args['num1']
    num2 = request.args['num2']

    result = int(num1) - int(num2)

    response = {"Subtrair": result}

    return response, 200

@app.route('/api/calculadora/multiplicar', methods=['GET'])
def getMultiplicacao():
    num1 = request.args['num1']
    num2 = request.args['num2']

    result = int(num1) * int(num2)

    response = {"Multiplicar": result}

    return response, 2000
    
@app.route('/api/calculadora/dividir', methods=['GET'])
def getDivisao():
    num1 = request.args['num1']
    num2 = request.args['num2']

    result = int(num1) / int(num2)

    response = {"Dividir": result}

    return response, 200

@app.route('/api/calculadora/potencia', methods=['GET'])
def getPotencia():
    num1 = request.args['num1']
    num2 = request.args['num2']

    result = math.pow(int(num1), int(num2))

    response = {"Potencia": result}

    return response, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)