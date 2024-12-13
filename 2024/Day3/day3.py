import re

with open('input.txt', 'r', encoding='utf-8') as dosya:
    content = dosya.read()

matches = re.findall(r'mul\([0-9]+,[0-9]+\)', content)

res = 0
for match in matches:
    values = match[:-1][4:].split(',')
    res += int(values[0]) * int(values[1])

print(res)
