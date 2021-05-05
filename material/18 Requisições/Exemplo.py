import requests
import json

def request_viacep(cep):
    url = f"http://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    print(response.status_code)
    print(response.json())


URL_API = "http://api.positionstack.com/v1/reverse"
API_KEY = "12789d781f9cc6a4d750be832db83f18"

def request_address_by_coords(latitude, longitude):
    query = f"{latitude},{longitude}"
    params = dict(access_key=API_KEY, query=query, limit=1)
    
    response = requests.get(URL_API, params=params)
    print(response.status_code)
    print(response.text)
    
request_address_by_coords("51.50853","-0.12574")