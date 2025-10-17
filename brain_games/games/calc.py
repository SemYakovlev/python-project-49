from random import choice, randint

Rules = "What is the result of the expression?"


def get_round():  # Запуск раундов
    operators = ["+", "-", "*"]
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    oper = choice(operators)

    question = f"{num1} {oper} {num2}"

    if oper == "+":
        correct_answer = num1 + num2
    elif oper == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    return question, correct_answer
