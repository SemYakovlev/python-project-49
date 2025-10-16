from random import randint

import prompt


# 1 Приветствуем и узнаём имя
def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    # 2 Сообщение с текстом про игру
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    # 3 Запуск раундов
    def is_prime(n):
        if n < 2:
            return False
        sqrt_num = int(n**0.5) + 1
        for i in range(2, sqrt_num):
            if n % i == 0:
                return False
        return True

    for _ in range(3):
        number = randint(1, 100)

        # Задаём вопрос
        print(f"Question: {number}")

        correct_answer = "yes" if is_prime(number) else "no"

        # Получаем ответ и сравниваем с правильным
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
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
