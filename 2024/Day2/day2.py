def is_safe(line):
    ascending = None

    for i in range(1, len(line)):
        diff = line[i] - line[i - 1]
        if diff < 0:
            diff = -diff
        if diff < 1 or diff > 3:
            return (False, i)

        if ascending is None:
            if line[i] > line[i - 1]:
                ascending = True
            elif line[i] < line[i - 1]:
                ascending = False
        elif ascending and line[i] < line[i - 1]:
            return (False, i)
        elif not ascending and line[i] > line[i - 1]:
            return (False, i)

    return (True, 0)

lines = open("input.txt").readlines()

safeCount = 0
dampenedSafeCount = 0

for line in lines:
    line = line.strip().split()
    line = [int(x) for x in line]
    res = is_safe(line)
    if res[0]:
        safeCount += 1
        dampenedSafeCount += 1
    else:
        indexRemoved = line[:res[1]] + line[res[1] + 1:]

        if is_safe(indexRemoved)[0]:
            dampenedSafeCount += 1
            continue

        if res[1] > 0:
            indexBeforeRemoved = line[:res[1] - 1] + line[res[1]:]

            if is_safe(indexBeforeRemoved)[0]:
                dampenedSafeCount += 1
                continue
        if res[1] > 1:
            indexTwoBeforeRemoved = line[:res[1] - 2] + line[res[1] - 1:]

            if is_safe(indexTwoBeforeRemoved)[0]:
                dampenedSafeCount += 1
                continue

print(safeCount)
print(dampenedSafeCount)
