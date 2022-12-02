lines = open("input.txt").readlines()

dict1 =  {'A': 1, 'B': 2, 'C': 3}
dict2 =  {'X': 1, 'Y': 2, 'Z': 3}
score = 0
for line in lines:
    opponent, you = line.split()

    opponent = dict1[opponent]
    you = dict2[you]
    score += you
    
    if you == opponent:
        score += 3
        continue
    if you == opponent + 1 or (opponent == 3 and you == 1):
        score += 6
print(score)
