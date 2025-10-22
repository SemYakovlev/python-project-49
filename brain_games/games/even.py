from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(n):
    return n % 2 == 0


def get_round():
    question = randint(1, 100)
    correct_answer = "yes" if is_even(question) else "no"
    return question, correct_answer
