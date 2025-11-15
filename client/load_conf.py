import json

import re

def remove_comments(jsonc_str):
    jsonc_str = re.sub(r'//.*?(\n|$)', '', jsonc_str)
    jsonc_str = re.sub(r'/\*.*?\*/', '', jsonc_str, flags=re.DOTALL) 
    return jsonc_str

def load():
    with open("client/configs/user.jsonc", 'r') as f:
        return json.loads(remove_comments(f.read()))