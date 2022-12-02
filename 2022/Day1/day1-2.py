lines = open("input.txt").readlines()
lines.append("")

elf_amount = 0
elf_amounts = []

for line in lines:
    line = line.strip()

    if line == '':
        elf_amounts.append(elf_amount)
        elf_amount = 0
    else:
        elf_amount += int(line)

elf_amounts.sort()
print(sum(elf_amounts[-3:]))
