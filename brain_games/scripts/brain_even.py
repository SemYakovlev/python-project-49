from random import randint

import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    def is_even(n):
        return n % 2 == 0

    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        number = randint(1, 100)
        print(f"Question: {number}")

        if is_even(number):
            correct_answer = "yes"
        else:
            correct_answer = "no"

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

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
