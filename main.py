import requests

url = 'https://yandex.ru'
response = requests.get(url)

#print(response.ok)
print(response.url)
print(response.encoding)
print(response.is_redirect)

payload = {"text":"python"}

response = requests.get('https://yandex.ru', params=payload)
response.raise_for_status()