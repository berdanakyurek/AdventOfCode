lines = open("input.txt").readlines()

register = 2
cycle = 1

def pr(cycle, register):
    if cycle % 40 in [register - 1, register, register + 1]:
        print('#', end="")
    elif cycle % 40 == 0 and 40 in [register - 1, register, register + 1]:
        print('#', end="")
    else:
        print('.', end="")
    if cycle % 40 == 0:
        print();
    
for line in lines:
    line = line.strip()
    pr(cycle, register)
    if line != 'noop':
        cycle += 1
        pr(cycle, register)
        register += int(line.split()[1])
    cycle += 1
    
