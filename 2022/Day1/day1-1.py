lines = open("input.txt").readlines()

elf_amount = 0
max_elf_amount = 0

for line in lines:
    line = line.strip()

    if line == '':
        if elf_amount > max_elf_amount:
            max_elf_amount = elf_amount
        elf_amount = 0
    else:
        elf_amount += int(line)

print(max_elf_amount)
