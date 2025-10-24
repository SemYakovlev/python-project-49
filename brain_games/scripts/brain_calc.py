from brain_games.games.calc import RULES, get_round
from brain_games.scripts.engine import game


def main():
    game(RULES, get_round)


if __name__ == "__main__":
    main()
