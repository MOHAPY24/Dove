from flask import Flask, request
import ollama

client = ollama.Client()
app = Flask(__name__)

@app.route('/post_endpoint', methods=['POST'])
def handle_post():
    data = request.json # handle JSON data
    print(f"POST: {data}")
    resp = client.chat(model=data["model"], messages=[{'role':'user', 'content': f'respond to {data["NAME"]}: {data["prompt"]}'}])
    
    # Process the data as needed    
    return {'status': 'success', 'response': resp["message"]["content"]}, 200

