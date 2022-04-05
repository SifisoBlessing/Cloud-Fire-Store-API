from flask import Flask, request, Response
from main.API import APIHandler
import json

app = Flask(__name__)


@app.route('/deposited', methods=['POST'])
def deposited():
    try:
        data = request.get_data()
        data = f"{data}".strip('b\'][')
        data = json.loads(data)
        apiHandler = APIHandler.APIHandler()
        apiHandler.deposited(data)
        return Response("success")
    except:
        return Response(status=400)


@app.route('/compensated', methods=['POST'])
def compensated():
    try:
        data = request.get_data()
        data = f"{data}".strip('b\'][')
        data = json.loads(data)
        apiHandler = APIHandler.APIHandler()
        apiHandler.compensated(data)
        return Response("success")
    except:
        return Response(status=400)


@app.route('/unsettled', methods=['POST'])
def void():
    try:
        data = request.get_data()
        data = f"{data}".strip('b\'][')
        data = json.loads(data)
        apiHandler = APIHandler.APIHandler()
        apiHandler.unsettled(data)
        return Response("success")
    except:
        return Response(status=400)


"""""
{\"name\": \"sifiso\",\"surname\": \"ncube\",\"customer_id\": \"\",\"email\":\"sifisoncube017@gmail.com\",\"product_name\": \"earphone\",\"category\": \"phones\",\"product_id\": \"1efa35\",\"value\": \"250\"}"
"""
