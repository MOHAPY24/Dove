import json
import requests
import load_conf
import load_session


class DoveClient:
    def __init__(self):
        self.config = load_conf.load()
        self.sessionco = load_session.load()
        self.URL = self.sessionco["url"]

    def create_data(self, prompt:str, model:str):
        if self.config["meta"]["verbose?"]:
            print("[*] Made JSON")
        self.data = {"NAME": f"{self.config["meta"]["sender"]}", "prompt": prompt, 'model':model}
    
    def send_to_remote(self):
        if self.config["meta"]["verbose?"]:
            print("[*] Sending JSON")
        self.response = requests.post(self.URL, json=self.data)

    def recive_from_remote(self):
        if self.config["meta"]["verbose?"]:
            print("[*] JSON Sent, response recieved")
        print(self.response.json()["response"])        
        if self.config["meta"]["verbose?"]:
            print("[*] Response back, showing full JSON response")      
            print(self.response.json())