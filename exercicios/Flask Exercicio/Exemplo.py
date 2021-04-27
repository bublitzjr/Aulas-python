import requests
import json

def request_viacep(cep):
    URL = f"http://viacep.com.br/ws/{cep}/json"
    response = requests.get(URL)
    print(response.status_code)
    print(response.json())    

# request_viacep("88036135")

URL_KEY = ""
API_KEY = ""

def request_by_coords(latitude, longitude):
    query = f"{latitude},{longitude}"
    params = dict(access_key=API_KEY, query=query, limit=1)
    response = requests.get(params)