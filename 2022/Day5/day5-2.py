lines = open("input.txt").readlines()


stacks = []

for i in range(len(lines[0])//4):
    stacks.append([])

move = False

for line in lines:
    if line.strip() == "":
        move = True
        continue

    if not move:
        for i in range(len(line)):
            letter = line[i];
            if letter.isalpha():
                stacks[(i-1)//4].insert(0, letter)
    
    else:
        words = line.split()
        count = int(words[1])
        frm = int(words[3]) - 1
        to = int(words[5]) - 1

        if frm == to:
            continue

        tempStack = []
        for i in range(count):
            tempStack.append(stacks[frm].pop())
        for i in range(count):
            stacks[to].append(tempStack.pop())
            
for i in stacks:
    print(i[-1], end="")
print()
