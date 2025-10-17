from random import randint


Rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(n):
    return n % 2 == 0


def get_round():
    number = randint(1, 100)
    correct_answer = "yes" if is_even(number) else "no"
    return number, correct_answer
