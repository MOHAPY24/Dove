from flask import Flask, request
import ollama, json, utils

client = ollama.Client()
app = Flask(__name__)
prev_time = 0
prev_content = ""
prev_name = ""

with open("server/config.jsonc", 'r') as r:
    conf = json.loads(utils.strip_json_comments(r.read()))


try:
    f = open("access.log", 'a')
except FileNotFoundError:
    f = open("access.log", 'w')

@app.route('/post_endpoint', methods=['POST'])
def handle_post():
    global prev_content, prev_name, prev_time, prev_name
    data = request.json # handle JSON data
    f.write(str(data))
    print(f"POST: {data}")
    if data["time"] == prev_time and data['NAME'] == prev_name:
        return {'status':'spam', 'response':"Too much prompts being sent from this device, please slow down."}
    elif data["time"] == prev_time and prev_name == data["NAME"] and prev_content == data["prompt"]:
        return {'status':'spam', 'response':"Repeated prompts being sent from this device, please slow down."}
    resp = client.chat(model=data["model"], messages=[{'role':'user', 'content': f'respond to {data["NAME"]}: {data["prompt"]}'}])
    prev_content = resp["message"]["content"]
    prev_time = data["time"]
    prev_name = data["NAME"]  
    return {'status': 'success', 'response': resp["message"]["content"]}, 200

@app.route('/auth', methods=['POST'])
def getkey():
    return {'status': 'success', 'key': conf["passwd"]}, 200


