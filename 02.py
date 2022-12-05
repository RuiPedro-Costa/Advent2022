def main() -> None:

    shape_points = {
        "A": 1,
        "B": 2,
        "C": 3
    }

    player_score_points = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    rounds = read_input("F:/Documentos/Trabalho/Advent Of Code 2022/advent2.txt")
    print(play_game_part_one(rounds, shape_points, player_score_points))
    print(play_game_part_two(rounds, shape_points, player_score_points))


def read_input(file_path: str) -> list:
    input_rounds = []

    with open(file_path) as f:
        lines = f.readlines()

    for line in lines:
        input_rounds.append(line.split())

    return input_rounds


def play_game_part_one(game_rounds: list, shape_points: dict, player_score_points: dict) -> int:
    player_score = 0

    for game_round in game_rounds:
        if shape_points.get(game_round[0]) == player_score_points.get(game_round[1]):
            player_score += player_score_points.get(game_round[1]) + 3
        elif game_round[1] == "X" and game_round[0] == "C":
            player_score += player_score_points.get(game_round[1]) + 6
        elif game_round[1] == "Y" and game_round[0] == "A":
            player_score += player_score_points.get(game_round[1]) + 6
        elif game_round[1] == "Z" and game_round[0] == "B":
            player_score += player_score_points.get(game_round[1]) + 6
        else:
            player_score += player_score_points.get(game_round[1])
    return player_score


def play_game_part_two(game_rounds: list, shape_points: dict, player_score_points: dict) -> int:
    player_score = 0

    for game_round in game_rounds:
        if game_round[1] == "Y":
            player_score += shape_points.get(game_round[0]) + 3
        elif game_round[1] == "X" and game_round[0] == "A":
            player_score += player_score_points.get("Z")
        elif game_round[1] == "X" and game_round[0] == "B":
            player_score += player_score_points.get("X")
        elif game_round[1] == "X" and game_round[0] == "C":
            player_score += player_score_points.get("Y")
        elif game_round[1] == "Z" and game_round[0] == "A":
            player_score += player_score_points.get("Y") + 6
        elif game_round[1] == "Z" and game_round[0] == "B":
            player_score += player_score_points.get("Z") + 6
        elif game_round[1] == "Z" and game_round[0] == "C":
            player_score += player_score_points.get("X") + 6
    return player_score


if __name__ == "__main__":
    main()
