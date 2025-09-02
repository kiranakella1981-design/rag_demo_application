import requests
import os
from dotenv import load_dotenv
load_dotenv()
EURON_API_KEY2 = os.getenv("EURON_API_KEY2")

def generate_completion(prompt, model="gpt-4.1-nano", temperature=0.3):
    url = "https://api.euron.one/api/v1/euri/chat/completions"
    headers = {
        "Authorization": f"Bearer {EURON_API_KEY2}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500,
        "temperature": temperature
    }
    res = requests.post(url, headers=headers, json=payload)
    return res.json()['choices'][0]['message']['content']

def generate_completion(prompt, model="gpt-4.1-nano"):
    url = "https://api.euron.one/api/v1/euri/chat/completions"
   # url = "https://api.euron.one/api/v1/euri/alpha/chat/completions"
    headers = {
        "Authorization": f"Bearer {EURON_API_KEY2}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500,
        "temperature": 0.3
    }
    response = requests.post(url, headers=headers, json=payload)
    #print(response.json())
    return response.json()['choices'][0]['message']['content']