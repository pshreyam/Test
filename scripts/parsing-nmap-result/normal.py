with open('output.txt') as f:
    lines = f.readlines()

ports = []

for line in lines:
    if line.startswith('Discovered open port'):
        ports.append(line.split('/')[0].split()[-1])

print(','.join(ports))