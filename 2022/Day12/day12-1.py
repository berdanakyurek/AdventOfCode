from numpy import *

lines = open("input.txt").readlines()

def is_goable(frm, to):
    if frm == 'S':
        return is_goable('a', to)
    elif frm == 'E':
        return is_goable('z', to)
    elif to == 'S':
        return is_goable(frm, 'a')
    elif to == 'E':
        return is_goable(frm, 'z')
    
    return ord(to) - ord(frm) <= 1



mat = []
visited = []

s_pos = (-1, -1)
e_pos = (-1, -1)

for i, line in enumerate(lines):
    line = line.strip()
    row = []
    vis = []
    for j, letter in enumerate(line):
        row.append(letter)
        vis.append(False)
        if letter == "S":
            s_pos = (i, j)
        elif letter == "E":
            e_pos = (i, j)
        
    mat.append(row)
    visited.append(vis)


queue = [[s_pos]]

while len(queue) > 0:
    vertex = queue.pop(-1)

    last = vertex[-1]
    
    if visited[last[0]][last[1]]:
        continue
    
    visited[last[0]][last[1]] = True
    current = mat[last[0]][last[1]]
    if(current == "E"):
        print(len(vertex)-1)
        break
    if last[0] > 0 and is_goable(current, mat[last[0]-1][last[1]]) and visited[last[0]-1][last[1]] == False:
        vertex_copy = vertex.copy()
        vertex_copy.append((last[0]-1, last[1]))
        queue.insert(0, vertex_copy)
        
    if last[0] < len(mat)-1 and is_goable(current, mat[last[0]+1][last[1]]) and visited[last[0]+1][last[1]] == False:
        vertex_copy = vertex.copy()
        vertex_copy.append((last[0]+1, last[1]))
        queue.insert(0, vertex_copy)

    if last[1] > 0 and is_goable(current, mat[last[0]][last[1]-1]) and visited[last[0]][last[1]-1] == False:
        vertex_copy = vertex.copy()
        vertex_copy.append((last[0], last[1]-1))
        queue.insert(0, vertex_copy)
        
    if last[1] < len(mat[0])-1 and is_goable(current, mat[last[0]][last[1]+1]) and visited[last[0]][last[1]+1] == False:
        vertex_copy = vertex.copy()
        vertex_copy.append((last[0], last[1]+1))
        queue.insert(0, vertex_copy)
        
