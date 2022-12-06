line = open("input.txt").read().strip()

for i in range(3, len(line)):
    substr = line[i-3:i+1]
    if len(list(substr)) == len(set(list(substr))):
        print(i+1)
        break
