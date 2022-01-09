import requests
url = 'https://xkcd.com/1906/'

r = requests.get(url)

print(r.status_code)

msg = "Hello World"
print(msg)