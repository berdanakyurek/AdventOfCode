lines = open("input.txt").readlines()

count = 0
for line in lines:
    elves = line.strip().split(',')
    elves[0] = elves[0].split('-')
    elves[1] = elves[1].split('-')

    if int(elves[0][0]) <= int(elves[1][0]) and int(elves[0][1]) >= int(elves[1][1]):
        count += 1
    elif int(elves[0][0]) >= int(elves[1][0]) and int(elves[0][1]) <= int(elves[1][1]):
        count += 1
    
print(count)
