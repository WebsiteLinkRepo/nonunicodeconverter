import json

transcript_path = '/home/samuelvictor/.claude-omniroute/projects/-home-samuelvictor-unicode2nonunicode-com/f1749e26-2147-4d2f-8887-e9c8a666ac15.jsonl'
with open(transcript_path, 'r') as f:
    for line in f:
        data = json.loads(line)
        # Search for mention of fixes related to '`' (grave) or '`w' or 'tha'
        # in assistant messages or tool inputs
        s = json.dumps(data)
        if 'ya_alt' in s or '0xb6' in s or '0x60' in s or 'tha ok' in s or '`w' in s:
            # check if it's a bash command or write file or thought
            if isinstance(data, dict):
                content = data.get('content', '')
                if isinstance(content, list):
                    for c in content:
                        text = c.get('text', '')
                        if 'b6' in text or '0xb6' in text or '0x60' in text or '`w' in text:
                            print("FOUND IN TEXT:", text[:500])
