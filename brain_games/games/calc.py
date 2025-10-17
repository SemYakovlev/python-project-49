from random import choice, randint

RULES = "What is the result of the expression?"


def get_round():
    operators = ["+", "-", "*"]
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    operation = choice(operators)

    question = f"{num1} {operation} {num2}"

    if operation == "+":
        correct_answer = num1 + num2
    elif operation == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    return question, correct_answer
