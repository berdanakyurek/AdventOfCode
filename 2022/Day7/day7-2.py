from anytree import Node, RenderTree

lines = open("input.txt").readlines()

root = None
current_node = None
for line in lines:
    line = line.strip()
    if line[:4] == "$ cd":
        new_dir = line.split()[-1]
        if new_dir == "/":
            root = Node(new_dir)
            root.size = 0
            current_node = root
        elif new_dir == "..":
            current_node = current_node.parent
        else:
            new_node = Node(new_dir, parent=current_node)
            new_node.size = 0
            current_node = new_node
    elif line[:3] == "dir" or line == "$ ls":
        continue
    else:
        size = int(line.split()[0])
        temp_node = current_node

        while temp_node != None:
            temp_node.size += size
            temp_node = temp_node.parent

unused_space = 70000000 - root.size
req_space = 30000000 - unused_space

candidate = -1
for pre, fill, node in RenderTree(root):
    if node.size >= req_space and (candidate == -1 or candidate > node.size):
        candidate = node.size

print(candidate)
