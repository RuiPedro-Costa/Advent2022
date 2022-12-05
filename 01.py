with open("F:/Documentos/Trabalho/Advent Of Code 2022/advent1.txt") as f:
    lines = f.readlines()

values = []

for line in lines:
    values.append(line.removesuffix("\n"))

elf_cal = []
cal = 0

for value in values:
    if value == "":
        elf_cal.append(cal)
        cal = 0
        continue
    cal += int(value)

elf_cal.sort()


print(values)
print(elf_cal)
print(elf_cal[-1] + elf_cal[-2] + elf_cal[-3])
