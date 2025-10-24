from random import randint

RULES = "What number is missing in the progression?"


def generate_progression(start, step, length):
    collection = []
    for i in range(length):
        current_element = start + i * step
        collection.append(str(current_element))
    return collection


def get_round():
    start = randint(0, 20)
    step = randint(1, 10)
    length = randint(5, 10)
    progression = generate_progression(start, step, length)

    index = randint(1, length - 1)
    correct_answer = progression[index]
    progression[index] = ".."

    question = " ".join(progression)
    return question, correct_answer
