import random

from hangman.hangman_ranking import save_ranking


WORDS = {
    "EASY": [
        "apple",
        "bread",
        "chair",
        "dream",
        "earth"
    ],

    "NORMAL": [
        "animal",
        "castle",
        "coffee",
        "family",
        "flower"
    ],

    "HARD": [
        "computer",
        "elephant",
        "mountain",
        "keyboard",
        "triangle"
    ]
}

HANGMAN_DRAWINGS = [
    """
  +---+
  |   |
      |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  😢  |
 /|\\  |
 /    |
      |
      |
=========""",
    """
[GAME OVER]
  +---+
  |   |
  💀  |
 /|\\  |
 / \\  |
      |
      |
========="""
]

SUCCESS_ART = r"""
==================================================
||                                              ||
||        * * *  YOU WIN!  * * *                ||
||          HANGMAN CLEARED!                    ||
||                                              ||
==================================================
"""


def show_success():
    print(SUCCESS_ART)
    print("🎉 축하합니다! 정답을 맞혔습니다! 🎉")


def select_difficulty():

    while True:

        print("=" * 50)
        print("                    난이도 선택")
        print("=" * 50)
        print("1. EASY")
        print("2. NORMAL")
        print("3. HARD")

        try:
            choice = int(input("선택 : "))
        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        if choice == 1:
            return "EASY"

        elif choice == 2:
            return "NORMAL"

        elif choice == 3:
            return "HARD"

        else:
            print("올바르지 않은 번호입니다.")


def hangman_play(user_id):

    difficulty = select_difficulty()

    answer = random.choice(WORDS[difficulty])

    guessed = []
    attempts = 0
    wrong_count = 0
    max_wrong = 6

    while True:

        current_word = ""

        for alphabet in answer:

            if alphabet in guessed:
                current_word += alphabet + " "

            else:
                current_word += "_ "

        print()
        print(HANGMAN_DRAWINGS[wrong_count])
        print("단어 :", current_word)
        print("입력한 알파벳 :", " ".join(sorted(guessed)) or "없음")
        print(f"남은 기회 : {max_wrong - wrong_count}")

        if "_" not in current_word:
            print()
            show_success()

            print(f"총 시도 횟수 : {attempts}회")

            save_ranking(
                user_id,
                attempts,
                difficulty
            )

            break

        if wrong_count >= max_wrong:
            print()
            print("게임 오버!")
            print(f"정답 : {answer}")
            break

        alphabet = input("알파벳 입력 : ").lower()

        if len(alphabet) != 1 or not alphabet.isalpha():
            print("알파벳 한 글자만 입력해주세요.")
            continue

        if alphabet in guessed:
            print("이미 입력한 알파벳입니다.")
            continue

        guessed.append(alphabet)
        attempts += 1

        if alphabet not in answer:
            wrong_count += 1
            print("틀렸습니다.")

        else:
            print("맞았습니다!")