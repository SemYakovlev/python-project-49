from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:
        return False
    sqrt_num = int(n**0.5) + 1
    for i in range(2, sqrt_num):
        if n % i == 0:
            return False
    return True


def get_round():
    number = randint(1, 100)
    question = f"{number}"
    correct_answer = "yes" if is_prime(number) else "no"
    return correct_answer, question
