from brain_games.games.gcd import get_round, RULES

from brain_games.welcome import welcome

import prompt


def game():
    name = welcome()

    print(RULES)

    for _ in range(3):
        question, correct_answer = get_round()

        print(f"Question: {question}")

        user_answer = prompt.string("Your answer: ")
        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'. "
                f"\nLet's try again, {name}!"
            )
            return
    print(f"Congratulations, {name}!")


def main():
    game()


if __name__ == "__main__":
    main()
