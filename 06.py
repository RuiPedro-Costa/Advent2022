def main():
    data_stream = read_input("F:/Documentos/Trabalho/Advent Of Code 2022/advent6.txt")

    packet_checker = start_of_marker_finder(data_stream)
    print(packet_checker)
    message_checker = star_of_message_finder(data_stream)
    print(message_checker)


def read_input(file_path: str) -> str:
    data_stream = ""
    with open(file_path) as file:
        reader = file.read()
        for char in reader:
            data_stream += char
    return data_stream


def start_of_marker_finder(data_stream: str) -> int:
    num_chars_processed = 0
    for i in range(len(data_stream)):
        packet = data_stream[i:i + 5]
        packet_checker = set(packet)
        if len(packet_checker) != len(packet):
            num_chars_processed += 1
        else:
            num_chars_processed += 4
            return num_chars_processed


def star_of_message_finder(data_stream: str) -> int:
    num_chars_processed = 0
    for i in range(len(data_stream)):
        packet = data_stream[i:i + 14]
        packet_checker = set(packet)
        if len(packet_checker) != len(packet):
            num_chars_processed += 1
        else:
            num_chars_processed += 14
            return num_chars_processed


if __name__ == "__main__":
    main()
