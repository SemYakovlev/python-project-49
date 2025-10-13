from random import randint

import prompt


# 1 Приветствуем и узнаём имя
def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    # 2 Сообщение с текстом про игру
    print("What number is missing in the progression?")

    # 3 Запуск раундов
    def progression(start, step, length):
        lst = []
        for i in range(length):
            currentElement = start + i * step
            lst.append(str(currentElement))
        return lst

    for _ in range(3):
        start = randint(0, 20)
        step = randint(1, 10)
        length = randint(5, 10)
        gen_progr = progression(start, step, length)

        index = randint(1, length - 1)
        correct_answer = gen_progr[index]
        gen_progr[index] = ".."

        quest = " ".join(gen_progr)

        # Задаём вопрос
        print(f"Question: {quest}")

        # Получаем ответ и сравниваем с правильным
        user_answer = prompt.string("Your answer: ")
        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'. "
                f"\nLet's try again, {name}!"
            )
            return
    # 4 Выход победителем
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
