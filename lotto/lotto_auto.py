import random

from lotto.lotto_records import save_record


def lotto_auto(user_id):

    lotto = random.sample(
        range(1, 46),
        6
    )

    lotto.sort()

    print("=" * 50)
    print(f"{'자동 번호':^50}")
    print("=" * 50)
    print("생성된 번호 :", lotto)

    save_record(
        user_id,
        "자동",
        lotto
    )

    print("기록이 저장되었습니다.")
    print()