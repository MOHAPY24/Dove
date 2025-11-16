import json
import re

import re

def strip_json_comments(text):
    pattern = r'("(?:\\.|[^"\\])*")|(?:\/\/.*?$)'
    return re.sub(pattern, lambda m: m.group(1) if m.group(1) else '', text, flags=re.MULTILINE)


def load():
    with open("client/configs/session.jsonc", 'r') as f:
        return json.loads(strip_json_comments(f.read()))