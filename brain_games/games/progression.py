from random import randint

Rules = "What number is missing in the progression?"


def progression(start, step, length):
    lst = []
    for i in range(length):
        currentElement = start + i * step
        lst.append(str(currentElement))
    return lst


def get_round():
    start = randint(0, 20)
    step = randint(1, 10)
    length = randint(5, 10)
    gen_progr = progression(start, step, length)

    index = randint(1, length - 1)
    correct_answer = gen_progr[index]
    gen_progr[index] = ".."

    question = " ".join(gen_progr)
    return question, correct_answer
