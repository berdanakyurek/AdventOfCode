lines = open("input.txt").readlines()

monkeys = [[]]

for line in lines:
    line = line.strip()
    if line == "":
        monkeys.append([])
        continue
    if line.split()[0] == "Monkey":
        continue
    else:
        monkeys[-1].append(line.split(": ")[-1])

for m in monkeys:
    newItems = []
    for item in m[0].split(", "):
        newItems.append(int(item))
    m[0] = newItems
    m[1] = m[1].split(" = ")[-1][4:].strip().split()
    m[2] = int(m[2].split()[-1])
    m[3] = int(m[3].split()[-1])
    m[4] = int(m[4].split()[-1])
    m.append(0)
    
for i in range(20):
    for m in monkeys: 
        while len(m[0]) > 0:
            item = m[0].pop(0)
            val = 0
            if m[1][1] == 'old':
                val = item
            else:
                val = int(m[1][1])
            if m[1][0] == '+':
                item += val
            elif m[1][0] == '*':
                item *= val

            item = item // 3

            if item % m[2] == 0:
                monkeys[m[3]][0].append(item)
            else:
                monkeys[m[4]][0].append(item)
            m[5] = m[5] + 1

arr = []
for m in monkeys:
    arr.append(m[5])
arr.sort()
print(arr[-2:][0] * arr[-2:][1])
