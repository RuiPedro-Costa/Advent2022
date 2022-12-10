def main():
    input_data = input_parsing("F:/Documentos/Trabalho/Advent Of Code 2022/advent7.txt")
    directory_map = directory_mapper(input_data)
    part_one = finding_sum(directory_map)
    part_two = find_folder_to_delete(directory_map)
    print(part_two)


def input_parsing(file_path: str) -> list:
    input_data = []

    with open(file_path) as file:
        reader = file.readlines()
        for line in reader:
            input_data.append(line.strip("\n").strip("$").split())
    return input_data


def directory_mapper(input_data: list) -> dict:
    directory_map: dict[str: int] = {}
    path: list[str] = ['/']
    current_path = "".join(path)
    directory_map.setdefault(current_path, 0)

    for line in input_data:
        if line[0] == "dir":
            directory_map.setdefault(current_path + line[1] + "/", 0)
        elif line[0].isdigit():
            directory_map[current_path] += int(line[0])
        elif line[0] == "cd":
            if line[1] == "..":
                subfolder_size = directory_map.get(current_path)
                path.pop()
                current_path = "".join(path)
                directory_map[current_path] += subfolder_size
            elif line[1] == "/":
                path = [line[1]]
                current_path = "".join(path)
            else:
                path.append(line[1] + "/")
                current_path = "".join(path)

    for folder in range(len(path) - 1):
        subfolder_size = directory_map.get(current_path)
        path.pop()
        current_path = "".join(path)
        directory_map[current_path] += subfolder_size
    return directory_map


def finding_sum(directory_map: dict) -> int:
    total_sum = 0

    for size in directory_map.values():
        if size <= 100000:
            total_sum += size
    return total_sum


def find_folder_to_delete(directory_map: dict) -> int:
    max_space = 70000000
    needed_space = 30000000
    used_space = directory_map.get("/")
    space_left = max_space - used_space
    size_list = []

    for size in directory_map.values():
        if space_left + size >= needed_space:
            size_list.append(size)
    return sorted(size_list)[0]


if __name__ == "__main__":
    main()
