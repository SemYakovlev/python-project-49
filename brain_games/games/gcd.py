from random import randint

RULES = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def get_round():
    MAX = randint(1, 100)
    MIN = randint(1, 100)
    correct_answer = gcd(MAX, MIN)
    question = f"{MAX} {MIN}"
    return question, correct_answer
