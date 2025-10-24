from random import randint

RULES = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def get_round():
    max_gcd = randint(1, 100)
    min_gcd = randint(1, 100)
    correct_answer = gcd(max_gcd, min_gcd)
    question = f"{max_gcd} {min_gcd}"
    return question, correct_answer
