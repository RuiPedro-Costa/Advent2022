def main() -> None:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    priority_part_one = 0
    priority_part_two = 0
    rucksacks = read_input("F:/Documentos/Trabalho/Advent Of Code 2022/advent3.txt")

    for rucksack in rucksacks:
        priority_part_one += find_priority_part_one(alphabet, rucksack_splitter(rucksack))

    for group in rucksack_group_splitter(rucksacks):
        priority_part_two += find_priority_part_two(alphabet, group)

    print(priority_part_one)
    print(priority_part_two)


def read_input(file_path: str) -> list:
    rucksacks = []

    with open(file_path, "r") as f:
        text_input = f.readlines()

    for line in text_input:
        rucksacks.append(line.strip("\n"))

    return rucksacks


def rucksack_splitter(rucksack: list) -> list:
    first_half = rucksack[:int(len(rucksack) / 2)]
    second_half = rucksack[int(len(rucksack) / 2):]
    return [first_half, second_half]


def find_priority_part_one(alphabet: str, split_rucksack: list) -> int:
    first_half = split_rucksack[0]
    second_half = split_rucksack[1]
    priority_sum = 0

    for letter in first_half:
        if letter in second_half:
            if letter.isupper():
                for i in range(len(alphabet)):
                    if letter.lower() == alphabet[i]:
                        priority_sum += i + 27
                        return priority_sum
            else:
                for j in range(len(alphabet)):
                    if letter == alphabet[j]:
                        priority_sum += j + 1
                        return priority_sum


def rucksack_group_splitter(rucksack: list) -> list:
    groups = []

    for i in range(0, len(rucksack), 3):
        groups.append([rucksack[i], rucksack[i + 1], rucksack[i + 2]])

    return groups


def find_priority_part_two(alphabet: str, group: list) -> int:
    priority_sum = 0
    first_sack = group[0]
    second_sack = group[1]
    third_sack = group[2]

    for letter in first_sack:
        if letter in second_sack and letter in third_sack:
            if letter.isupper():
                for i in range(len(alphabet)):
                    if letter.lower() == alphabet[i]:
                        priority_sum += i + 27
                        return priority_sum
            else:
                for i in range(len(alphabet)):
                    if letter == alphabet[i]:
                        priority_sum += i + 1
                        return priority_sum


if __name__ == "__main__":
    main()
