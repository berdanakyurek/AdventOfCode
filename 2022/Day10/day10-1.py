lines = open("input.txt").readlines()

register = 1
cycle = 1
res = 0

for line in lines:
    line = line.strip()
    if cycle in [20, 60, 100, 140, 180, 220]:
        res += register*cycle
    if line != 'noop':
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            res += register*cycle
        register += int(line.split()[1])
    cycle += 1
    
print(res)
