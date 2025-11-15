import json
import requests
import load_conf


config = load_conf.load()

if config["meta"]["verbose?"] == True:
    verb = True
else:
    verb = False

url = 'http://127.0.0.1:5000/post_endpoint'
if verb:
    print("[*] Made JSON")
data = {"NAME": f"{config["meta"]["sender"]}", "prompt": 'Hello!', 'model':'phi3:mini'}

if verb:
    print("[*] Sending JSON")
response = requests.post(url, json=data)
if verb:
    print("[*] JSON Sent, response recieved")
print(response.json()["response"])        
if verb:
    print("[*] Response back, showing full JSON response")      
    print(response.json())