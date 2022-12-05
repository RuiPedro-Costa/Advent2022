def main():
    groups = read_input("F:/Documentos/Trabalho/Advent Of Code 2022/advent4.txt")
    overlaps_part_one = 0
    overlaps_part_two = 0

    for group in groups:
        if find_overlap_part_one(group):
            overlaps_part_one += 1
    print(overlaps_part_one)

    for group in groups:
        if find_overlap_part_two(group):
            overlaps_part_two += 1
    print(overlaps_part_two)


def read_input(file_path: str) -> list:
    pairs = []

    with open(file_path, "r") as f:
        text_input = f.readlines()

    for line in text_input:
        pairs.append(line.strip("\n").split(","))

    return pairs


def find_overlap_part_one(group: list) -> bool:
    first_section = group[0].split("-")
    second_section = group[1].split("-")
    first_list = []
    second_list = []

    for i in range(int(first_section[0]), int(first_section[1]) + 1):
        first_list.append(i)

    for j in range(int(second_section[0]), int(second_section[1]) + 1):
        second_list.append(j)

    if all(elem in second_list for elem in first_list):
        return True
    elif all(elem in first_list for elem in second_list):
        return True


def find_overlap_part_two(group: list) -> int:
    first_section = group[0].split("-")
    second_section = group[1].split("-")
    first_list = []
    second_list = []

    for i in range(int(first_section[0]), int(first_section[1]) + 1):
        first_list.append(i)

    for j in range(int(second_section[0]), int(second_section[1]) + 1):
        second_list.append(j)

    for number in first_list:
        if number in second_list:
            return True
    for number in second_list:
        if number in first_list:
            return True


if __name__ == "__main__":
    main()
