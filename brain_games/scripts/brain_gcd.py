from random import randint

import prompt


# 1 Приветствуем и узнаём имя
def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    # 2 Сообщение с текстом про игру
    print("Find the greatest common divisor of given numbers.")

    # 3 Запуск раундов
    for _ in range(3):
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        a, b = num1, num2
        while b != 0:
            a, b = b, a % b
        correct_answer = a

        # Задаём вопрос
        print(f"Question: {num1} {num2}")

        # Получаем ответ и сравниваем с правильным
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
    # 4 Выход победителем
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
