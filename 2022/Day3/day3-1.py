def priority(letter):
    if letter.islower():
        return ord(letter)-96
    return ord(letter.lower()) - 70

lines = open("input.txt").readlines()

sum = 0
for line in lines:
    length = len(line)
    c1 = set(list(line[0:int(length/2)]))
    c2 = set(list(line[int(length/2): length - 1]))
    
    sum += priority(list(c1.intersection(c2))[0])
print(sum)
