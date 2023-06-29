import requests

BASE_URl= 'http://127.0.0.1:8000/api'

def get_data(url):
   response= requests.get(url, params={'abc': 123}, json={"query":"hello client"})
   return (response.json())


print(get_data(BASE_URl))
