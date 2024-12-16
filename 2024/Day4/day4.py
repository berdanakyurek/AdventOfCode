lines = open("input.txt").readlines()

matrix = []
for line in lines:
    matrix.append(list(line.strip()))

count = 0
p2count = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'X':
            # Horizontal forward
            if len(matrix[i]) > j + 3:
                if matrix[i][j + 1] == 'M' and matrix[i][j + 2] == 'A' and matrix[i][j + 3] == 'S':
                    count += 1

            # Horizontal backward
            if j - 3 >= 0:
                if matrix[i][j - 1] == 'M' and matrix[i][j - 2] == 'A' and matrix[i][j - 3] == 'S':
                    count += 1

            # Vertical forward
            if len(matrix) > i + 3:
                if matrix[i + 1][j] == 'M' and matrix[i + 2][j] == 'A' and matrix[i + 3][j] == 'S':
                    count += 1

            # Vertical backward
            if i - 3 >= 0:
                if matrix[i - 1][j] == 'M' and matrix[i - 2][j] == 'A' and matrix[i - 3][j] == 'S':
                    count += 1

            # Diaogonal right down
            if len(matrix) > i + 3 and len(matrix[i]) > j + 3:
                if matrix[i + 1][j + 1] == 'M' and matrix[i + 2][j + 2] == 'A' and matrix[i + 3][j + 3] == 'S':
                    count += 1

            # Diaogonal right up
            if i - 3 >= 0 and len(matrix[i]) > j + 3:
                if matrix[i - 1][j + 1] == 'M' and matrix[i - 2][j + 2] == 'A' and matrix[i - 3][j + 3] == 'S':
                    count += 1

            # Diaogonal left down
            if len(matrix) > i + 3 and j - 3 >= 0:
                if matrix[i + 1][j - 1] == 'M' and matrix[i + 2][j - 2] == 'A' and matrix[i + 3][j - 3] == 'S':
                    count += 1

            # Diaogonal left up
            if i - 3 >= 0 and j - 3 >= 0:
                if matrix[i - 1][j - 1] == 'M' and matrix[i - 2][j - 2] == 'A' and matrix[i - 3][j - 3] == 'S':
                    count += 1

        elif matrix[i][j] == 'A':
            if i == 0 or j == 0 or i == len(matrix) - 1 or j == len(matrix[i]) - 1:
                continue

            if matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] != 'S':
                continue
            elif matrix[i-1][j-1] == 'S' and matrix[i+1][j+1] != 'M':
                continue
            elif matrix[i-1][j-1] == 'A' or matrix[i+1][j+1] == 'A':
                continue
            elif matrix[i-1][j-1] == 'X' or matrix[i+1][j+1] == 'X':
                continue

            if matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] != 'S':
                continue
            elif matrix[i-1][j+1] == 'S' and matrix[i+1][j-1] != 'M':
                continue
            elif matrix[i-1][j+1] == 'A' or matrix[i+1][j-1] == 'A':
                continue
            elif matrix[i-1][j+1] == 'X' or matrix[i+1][j-1] == 'X':
                continue
            p2count += 1
            print(i, j)
print(count)
print(p2count)
