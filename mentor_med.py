import os
from openai import OpenAI
from dotenv import load_dotenv

# Carrega a chave da API
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def conversar_com_agente(pergunta):
    resposta = client.chat.completions.create(
        model="gpt-4o-2024-11-20",
        messages=[
            {"role": "system", "content": "Você é um especialista em análise curricular e processos seletivos para residência médica no Brasil."},
            {"role": "user", "content": pergunta}
        ]
    )
    return resposta.choices[0].message.content

# Executa se for chamado diretamente
if __name__ == "__main__":
    pergunta = input("Digite sua pergunta para o Dr. MentorMed: ")
    resposta = conversar_com_agente(pergunta)
    print("\nResposta do Dr. MentorMed:")
    print(resposta)

