import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

# Carrega a chave da API
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Função do agente
def conversar_com_agente(pergunta):
    resposta = client.chat.completions.create(
        model="gpt-4o-2024-11-20",
        messages=[
            {"role": "system", "content": "Você é um especialista em análise curricular e processos seletivos para residência médica no Brasil."},
            {"role": "user", "content": pergunta}
        ]
    )
    return resposta.choices[0].message.content

# Interface do Streamlit
st.set_page_config(page_title="Dr. MentorMed", page_icon="🧠")
st.title("👨‍⚕️ Dr. MentorMed")
st.markdown("Especialista em análise curricular e residência médica.")

pergunta = st.text_input("Digite sua pergunta:")

if pergunta:
    with st.spinner("Consultando Dr. MentorMed..."):
        resposta = conversar_com_agente(pergunta)
        st.success("Resposta do Dr. MentorMed:")
        st.write(resposta)

