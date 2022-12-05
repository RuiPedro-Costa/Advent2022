def main():

    stack = ["WPGZVSB", "FZCBVJ", "CDZNHMLV", "BJFPZMDL", "HQBJGCFV", "BLSTQFG", "VZCGL", "GLN", "CHFJ"]

    moves_to_make = read_input("F:/Documentos/Trabalho/Advent Of Code 2022/advent5.txt")

    # for move in moves_to_make:
    #     move_box_part_one(stack, move[0], move[1], move[2])
    #
    # for pile in stack:
    #     print(pile[0], end="")
    # print()

    for move in moves_to_make:
        move_box_part_two(stack, move[0], move[1], move[2])

    for pile in stack:
        print(pile[0], end="")
    print()


def read_input(file_path: str) -> list:
    moves = []

    with open(file_path, "r") as f:
        text_input = f.readlines()

    for line in text_input:
        to_move = []
        raw_line = line.split()
        for element in raw_line:
            if not element.isalpha():
                to_move.append(int(element))
        moves.append(to_move)
    return moves


def move_box_part_one(stack: list, num_moves: int, source_stack: int, target_stack: int) -> None:

    for i in range(num_moves):
        box_to_move = stack[source_stack - 1][0]
        new_target_stack = box_to_move + stack[target_stack - 1]
        stack[target_stack - 1] = new_target_stack
        stack[source_stack - 1] = stack[source_stack - 1][1:]


def move_box_part_two(stack: list, num_boxes: int, source_stack: int, target_stack: int) -> None:
    boxes_to_move = stack[source_stack - 1][:num_boxes]
    new_target_stack = boxes_to_move + stack[target_stack - 1]
    stack[target_stack - 1] = new_target_stack
    stack[source_stack - 1] = stack[source_stack - 1][num_boxes :]


if __name__ == "__main__":
    main()
