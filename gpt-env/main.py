from password import API_KEY
import requests
import json

headers = {"Authorization": f"Bearer " + API_KEY, "Content-Type": "application/json"}

link = "https://api.openai.com/v1/chat/completions"

body_message = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Escreva uma mensagem legal para minha mãe"}]
}

body_message = json.dumps(body_message)#convert the dictionary in JSON

requisicao = requests.post(link, headers=headers, data = body_message)
print(requisicao)
print(requisicao.text)