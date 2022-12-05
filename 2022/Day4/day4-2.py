lines = open("input.txt").readlines()

count = 0
for line in lines:
    elves = line.strip().split(',')
    elves[0] = elves[0].split('-')
    elves[1] = elves[1].split('-')

    sets= []
    sets.append(set(range(int(elves[0][0]), int(elves[0][1])+1)))
    sets.append(set(range(int(elves[1][0]), int(elves[1][1])+1)))
    if len(list(set.intersection(*sets))) > 0:
        count += 1
    
print(count)
