import json

x='{"nombre":"Miku","edad":18,"trabajo":"Diva Virtual"}'

y=json.loads(x)

print(y["trabajo"])