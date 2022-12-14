def main():
    input_data = input_parsing("F:/Documentos/Trabalho/Advent Of Code 2022/advent8.txt")
    visible_trees = find_num_visible(input_data)
    print(visible_trees)
    best_scenic_score = find_most_scenic_score(input_data)
    print(best_scenic_score)


def input_parsing(file_path: str) -> list:
    tree_map = []

    with open(file_path) as file:
        reader = file.readlines()
        for line in reader:
            tree_map.append(line.strip("\n"))
    return tree_map


def find_num_visible(tree_map: list) -> int:
    map_height = len(tree_map)
    map_length = len(tree_map[0])
    visible_trees_list = []
    total_visible_trees = 0

    for i in range(map_height):
        for j in range(map_length):
            if i == 0 or j == 0 or i == map_height - 1 or j == map_length - 1:
                if i == j:
                    if [i, j] not in visible_trees_list and [j, i] not in visible_trees_list:
                        visible_trees_list.append([i, j])
                        continue
                elif [i, j] not in visible_trees_list:
                    visible_trees_list.append([i, j])
                    continue

            current_tree = tree_map[i][j]
            left_trees = tree_map[i][:j]
            right_trees = tree_map[i][j + 1:]
            top_trees = ""
            down_trees = ""

            for k in range(i):
                top_trees += tree_map[k][j]
            for x in range(i + 1, map_height):
                down_trees += tree_map[x][j]

            sides_tree_list = [left_trees, right_trees, top_trees, down_trees]
            max_trees_list = [max(trees) for trees in sides_tree_list if trees != ""]

            for tree in max_trees_list:
                if current_tree > tree:
                    if i == j:
                        if [i, j] not in visible_trees_list and [j, i] not in visible_trees_list:
                            visible_trees_list.append([i, j])
                    else:
                        if [i, j] not in visible_trees_list:
                            visible_trees_list.append([i, j])
    return len(visible_trees_list)


def find_most_scenic_score(tree_map: list) -> int:
    map_height = len(tree_map)
    map_length = len(tree_map[0])
    max_scenic_value = 0

    for i in range(len(tree_map)):
        for j in range(len(tree_map[0])):
            if i == 0 or j == 0 or i == map_height - 1 or j == map_length - 1:
                continue
            else:
                current_tree = int(tree_map[i][j])
                left_trees = tree_map[i][:j]
                right_trees = tree_map[i][j + 1:]
                top_trees = ""
                down_trees = ""
                left_score = 0
                top_score = 0
                right_score = 0
                down_score = 0
                current_total_score = 0

                for k in range(i):
                    top_trees += tree_map[k][j]
                for x in range(i + 1, map_height):
                    down_trees += tree_map[x][j]

                reversed_left_trees = left_trees[::-1]
                reversed_top_trees = top_trees[::-1]

                for tree in reversed_left_trees:
                    if int(tree) >= current_tree:
                        left_score += 1
                        break
                    if int(tree) < current_tree:
                        left_score += 1
                for tree in reversed_top_trees:
                    if int(tree) >= current_tree:
                        top_score += 1
                        break
                    if int(tree) < current_tree:
                        top_score += 1
                for tree in right_trees:
                    if int(tree) >= current_tree:
                        right_score += 1
                        break
                    if int(tree) < current_tree:
                        right_score += 1
                for tree in down_trees:
                    if int(tree) >= current_tree:
                        down_score += 1
                        break
                    if int(tree) < current_tree:
                        down_score += 1
                current_total_score = left_score * top_score * right_score * down_score

                if current_total_score > max_scenic_value:
                    max_scenic_value = current_total_score
    return max_scenic_value


if __name__ == "__main__":
    main()
