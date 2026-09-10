import random

from updown.updown_ranking import save_ranking


def select_difficulty():

    while True:

        print("="*50)
        print("                    난이도 선택")
        print("="*50)
        print("1. EASY   - 제한 없음")
        print("2. NORMAL - 10회 제한")
        print("3. HARD   - 5회 제한")

        try:
            difficulty_number = int(input("선택 : "))
        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        if difficulty_number == 1:
            return "EASY", None

        elif difficulty_number == 2:
            return "NORMAL", 10

        elif difficulty_number == 3:
            return "HARD", 5

        else:
            print("올바르지 않은 번호입니다.")


def updown_play(user_id):

    difficulty, max_attempts = select_difficulty()

    answer = random.randint(1, 100)
    attempts = 0

    print()
    print("="*50)
    print("                    UP & DOWN")
    print("="*50)
    print(f"난이도 : {difficulty}")
    print("1부터 100 사이의 숫자를 맞춰보세요.")

    while True:

        try:
            number = int(input("숫자 입력 : "))
        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        if number < 1 or number > 100:
            print("1부터 100 사이의 숫자를 입력해주세요.")
            continue

        attempts += 1

        if number == answer:

            print()
            print("정답입니다!")
            print(f"시도 횟수 : {attempts}회")

            save_ranking(
                user_id,
                attempts,
                difficulty
            )

            break

        elif number < answer:
            print("UP!")

        else:
            print("DOWN!")

        if max_attempts is not None and attempts >= max_attempts:

            print()
            print("게임 횟수를 모두 사용했습니다.")
            print(f"정답은 {answer}였습니다.")

            break