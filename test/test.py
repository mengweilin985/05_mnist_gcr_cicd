import requests

resp = requests.post("https://ml-run-service-h6j65vuzbq-as.a.run.app", files={'file': open('eight.png', 'rb')})

print(resp.json())
