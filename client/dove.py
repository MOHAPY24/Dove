import json
import requests
import load_conf
import load_session
import time
import random



class DoveClient:
    def __init__(self):
        self.config = load_conf.load()
        self.sessionco = load_session.load()
        self.URL = self.sessionco["url"]
    

    def create_data(self, prompt:str, model:str):
        if self.config["meta"]["verbose?"]:
            print("[*] Made JSON")
        self.data = {"NAME": f"{self.config["meta"]["sender"]}", "prompt": prompt, 'model':model, "time":time.time()}
    
    def send_to_remote(self, servkey):
        if self.config["meta"]["verbose?"]:
            print("[*] Sending JSON")
        resp = requests.post(self.URL + "/auth")
        if servkey != resp.json()["key"]:
            return "Invalid AUTHkey"
        self.response = requests.post(self.URL + "/post_endpoint", json=self.data)

    def recive_from_remote(self):
        if self.config["meta"]["verbose?"]:
            print("[*] JSON Sent, response recieved")
        print(self.response.json()["response"])        
        if self.config["meta"]["verbose?"]:
            print("[*] Response back, showing full JSON response")      
            print(self.response.json())