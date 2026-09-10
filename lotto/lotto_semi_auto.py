import random

from lotto.lotto_records import save_record


def lotto_semi_auto(user_id):
    lotto = []

    print("=" * 50)
    print(f"{'반자동 번호':^50}")
    print("=" * 50)
    print("원하는 번호를 입력하세요.")
    print("0을 입력하면 남은 번호를 자동으로 생성합니다.")

    while len(lotto) < 6:
        prompt = f"{len(lotto) + 1}번째 번호 (종료: 0) : "
        value = input(prompt).strip()

        try:
            number = int(value)
        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        if number == 0:
            break

        if number < 1 or number > 45:
            print("1부터 45까지 입력해주세요.")
            continue

        if number in lotto:
            print("이미 입력한 번호입니다.")
            continue

        lotto.append(number)

    remaining_numbers = 6 - len(lotto)
    lotto.extend(
        random.sample(
            [number for number in range(1, 46) if number not in lotto],
            remaining_numbers
        )
    )
    lotto.sort()

    print()
    print("생성된 번호 :", lotto)

    save_record(
        user_id,
        "반자동",
        lotto
    )

    print("기록이 저장되었습니다.")
    print()
