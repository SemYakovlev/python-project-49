from random import choice, randint

import prompt


# 1 Приветствуем и узнаём имя
def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    # 2 Сообщение с текстом про игру
    print("What is the result of the expression?")

    # 3 Запуск раундов
    operators = ["+", "-", "*"]

    for _ in range(3):
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        oper = choice(operators)
        # Задаём вопрос
        print(f"Question: {num1} {oper} {num2}")

        if oper == "+":
            correct_answer = num1 + num2
        elif oper == "-":
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2
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
