from flask import Flask, request, jsonify
from mentor_med import conversar_com_agente

app = Flask(__name__)

@app.route("/perguntar", methods=["POST"])
def perguntar():
    data = request.get_json()
    pergunta = data.get("pergunta", "")
    resposta = conversar_com_agente(pergunta)
    return jsonify({"resposta": resposta})
