def checkFromUpAndLeft(lines):
    column_maxes = [-1] * len(lines[0])
    for lineNo in range(len(lines)):
        row_max = -1
        for digitNo in range(len(lines[lineNo])):
            if lines[lineNo][digitNo][0] > row_max:
                lines[lineNo][digitNo] = (lines[lineNo][digitNo][0], True)
                row_max = lines[lineNo][digitNo][0]
            if lines[lineNo][digitNo][0] > column_maxes[digitNo]:
                lines[lineNo][digitNo] = (lines[lineNo][digitNo][0], True)
                column_maxes[digitNo] = lines[lineNo][digitNo][0]
    return lines

lines = open("input.txt").readlines()

for line in range(len(lines)):
    lines[line] = list(lines[line].strip())
    for digit in range(len(lines[line])):
        lines[line][digit] = (int(lines[line][digit]), False)

lines = checkFromUpAndLeft(lines)

reversed_lines = []

for line in lines:
    reversed_lines.insert(0, line[::-1])

final_lines = checkFromUpAndLeft(reversed_lines)

count = 0
for line in final_lines:
    for digit in line:
        if digit[1]:
            count += 1
print(count)
