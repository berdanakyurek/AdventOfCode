lines = open("input.txt").readlines()
head = (0,0)
tail = (0,0)

def U():
    global head
    global tail
    head = (head[0], head[1]+1)
def D():
    global head
    global tail
    head = (head[0], head[1]-1)
def L():
    global head
    global tail
    head = (head[0]-1, head[1])
def R():
    global head
    global tail
    head = (head[0]+1, head[1])

def isTouching(h, t):
    if abs(h[0]-t[0]) <= 1 and abs(h[1]-t[1]) <= 1:
        return True
    return False

def moveTail():
    global head
    global tail
    
    if isTouching(head, tail):
        return
    
    if head[0] == tail[0]:
        if head[1] > tail[1]:
            tail = (tail[0], tail[1]+1)
        else:
            tail = (tail[0], tail[1]-1)
    elif head[1] == tail[1]:
        if head[0] > tail[0]:
            tail = (tail[0]+1, tail[1])
        else:
            tail = (tail[0]-1, tail[1])
    else:
        if head[0] > tail[0]:
            if head[1] > tail[1]:
                tail = (tail[0]+1, tail[1]+1)
            else:
                tail = (tail[0]+1, tail[1]-1)
        else:
            if head[1] > tail[1]:
                tail = (tail[0]-1, tail[1]+1)
            else:
                tail = (tail[0]-1, tail[1]-1)

visited = set()
for line in lines:
    
    for i in range(int(line.split()[1])):
        globals()[line.split()[0]]()
        moveTail()
        visited.add(tail)

print(len(visited))
