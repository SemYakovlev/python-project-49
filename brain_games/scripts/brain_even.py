from brain_games.welcome import welcome

from brain_games.games.even import get_round, Rules

import prompt


def game():
    # 1 Приветствуем и узнаём имя
    name = welcome()

    # 2 Сообщение с текстом про игру
    print(Rules)

    # 3 Запуск раундов
    for _ in range(3):
        number, correct_answer = get_round()

        print(f"Question: {number}")

        # Получаем ответ и сравниваем с правильным
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'. "
                f"\nLet's try again, {name}!"
            )
            return
    # 4 Выход победителем
    print(f"Congratulations, {name}!")


def main():
    game()


if __name__ == "__main__":
    main()
