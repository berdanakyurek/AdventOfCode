def scenic(lines, x, y):
    if x == 0 or y == 0 or x == len(lines) - 1 or y == len(lines[0]) - 1:
        return 0
    this_h = int(lines[x][y])

    cnt_r = 0
    cnt_l = 0
    cnt_u = 0
    cnt_d = 0
    
    for i in lines[x][y+1:]:
        cnt_r += 1
        if int(i) >= this_h:
            break
        
    for i in lines[x][:y][::-1]:
        cnt_l += 1
        if int(i) >= this_h:
            break

    for i in lines[x+1:]:
        cnt_d += 1
        if int(i[y]) >= this_h:
            break

    for i in lines[:x][::-1]:
        cnt_u += 1
        if int(i[y]) >= this_h:
            break
    return cnt_u * cnt_l * cnt_r * cnt_d
lines = open("input.txt").read().splitlines()

maxS = -1

for i in range(len(lines)):
    for j in range(len(lines[i])):
        newS = scenic(lines, i, j)
        if  newS > maxS:
            maxS = newS
print(maxS)
