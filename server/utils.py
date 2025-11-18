import re

def strip_json_comments(text):
    pattern = r'("(?:\\.|[^"\\])*")|(?:\/\/.*?$)'
    return re.sub(pattern, lambda m: m.group(1) if m.group(1) else '', text, flags=re.MULTILINE)

