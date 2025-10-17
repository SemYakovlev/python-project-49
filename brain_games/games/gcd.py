from random import randint

Rules = "Find the greatest common divisor of given numbers."


def get_round():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    a, b = num1, num2
    while b != 0:
        a, b = b, a % b
    correct_answer = a
    question = f"{num1} {num2}"
    return question, correct_answer
