lines = open("input.txt").readlines()

rope = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
def U():
    global rope
    rope[0] = (rope[0][0], rope[0][1]+1)
def D():
    global rope
    rope[0] = (rope[0][0], rope[0][1]-1)
def L():
    global rope
    rope[0] = (rope[0][0]-1, rope[0][1])
def R():
    global rope
    rope[0] = (rope[0][0]+1, rope[0][1])

def isTouching(h, t):
    if abs(h[0]-t[0]) <= 1 and abs(h[1]-t[1]) <= 1:
        return True
    return False

def moveTailK(i):
    global rope
    if isTouching(rope[i-1], rope[i]):
        return
    
    if rope[i-1][0] == rope[i][0]:
        if rope[i-1][1] > rope[i][1]:
            rope[i] = (rope[i][0], rope[i][1]+1)
        else:
            rope[i] = (rope[i][0], rope[i][1]-1)
    elif rope[i-1][1] == rope[i][1]:
        if rope[i-1][0] > rope[i][0]:
            rope[i] = (rope[i][0]+1, rope[i][1])
        else:
            rope[i] = (rope[i][0]-1, rope[i][1])
    else:
        if rope[i-1][0] > rope[i][0]:
            if rope[i-1][1] > rope[i][1]:
                rope[i] = (rope[i][0]+1, rope[i][1]+1)
            else:
                rope[i] = (rope[i][0]+1, rope[i][1]-1)
        else:
            if rope[i-1][1] > rope[i][1]:
                rope[i] = (rope[i][0]-1, rope[i][1]+1)
            else:
                rope[i] = (rope[i][0]-1, rope[i][1]-1)

def moveTail():
    for i in range(1,len(rope)):
        moveTailK(i)
visited = set()
for line in lines:
    
    for i in range(int(line.split()[1])):
        globals()[line.split()[0]]()
        moveTail()
        visited.add(rope[-1])

print(len(visited))
