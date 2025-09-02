import requests
import numpy as np
import os
  
from dotenv import load_dotenv
load_dotenv()
 
EURON_API_KEY2 = os.getenv("EURON_API_KEY2")
if not EURON_API_KEY2:
    raise ValueError("Missing EURON_API_KEY2 environment variable")


def get_embedding(text,model="text-embedding-3-small"):
    url = "https://api.euron.one/api/v1/euri/embeddings"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {EURON_API_KEY2}"
    }
    payload = {"input": text,"model": model}

    response = requests.post(url, headers=headers, json=payload)
    print("Response JSON:", response.json())
    return np.array(response.json()['data'][0]['embedding'])
