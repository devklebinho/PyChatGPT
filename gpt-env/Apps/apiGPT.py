import requests
import json
import os
import openai


def chat_gpt(prompt):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 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'  # Substitua YOUR_API_KEY pela sua chave de API do OpenAI
    }
    data = {
        'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'},
                     {'role': 'user', 'content': prompt}]
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = json.loads(response.text)
        messages = result['choices'][0]['message']['content']
        print("Resposta do Chat GPT:", messages)
    else:
        print("Erro na solicitação. Código de status:", response.status_code)

# Exemplo de uso
prompt = "Descreva quais características um bom dev deve ter"
chat_gpt(prompt)