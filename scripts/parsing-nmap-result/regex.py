import re

with open('output.txt') as f:
    text = f.read()

ports = list(map(lambda x: x.split()[-1],re.findall(r'Discovered open port \d+', text)))

print(ports)