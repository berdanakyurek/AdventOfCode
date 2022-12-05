def priority(letter):
    if letter.islower():
        return ord(letter)-96
    return ord(letter.lower()) - 70

lines = open("input.txt").readlines()
sum = 0
sets = [{}, {}, {}]
for i in range(len(lines)):
    sets[i%3] = set(list(lines[i].strip()))
    if i%3 == 2:
        sum += priority(list(set.intersection(*sets))[0])
        
print(sum)
