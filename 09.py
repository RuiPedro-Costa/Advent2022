def main():
    input_data = input_parsing("F:/Documentos/Trabalho/Advent Of Code 2022/advent9.txt")
    print(input_data)


def input_parsing(file_path: str) -> list:
    move_list = []

    with open(file_path) as file:
        reader = file.readlines()
        for line in reader:
            move_list.append(line.strip("\n").split())
    return move_list


if __name__ == "__main__":
    main()
