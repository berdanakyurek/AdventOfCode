lines = open("input.txt").readlines()

list1 = []
list2 = []
for line in lines:
    line = line.strip().split()
    list1.append(int(line[0]))
    list2.append(int(line[1]))

list1.sort()
list2.sort()
sum = 0

for i in range(len(list1)):
    diff = list1[i] - list2[i]
    if diff < 0:
        diff = -diff

    sum += diff

print(sum)

sum2 = 0

for i in range(len(list1)):
    sum2 += list1[i] * list2.count(list1[i])

print(sum2)
