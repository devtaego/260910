from lotto.lotto_records import save_record


def lotto_manual(user_id):

    lotto = []

    print("=" * 50)
    print(f"{'수동 번호':^50}")
    print("=" * 50)

    while len(lotto) < 6:

        try:
            number = int(
                input(
                    f"{len(lotto) + 1}번째 번호 : "
                )
            )

        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        if number < 1 or number > 45:
            print("1부터 45까지 입력해주세요.")
            continue

        if number in lotto:
            print("이미 입력한 번호입니다.")
            continue

        lotto.append(number)

    lotto.sort()

    print()
    print("입력한 번호 :", lotto)

    save_record(
        user_id,
        "수동",
        lotto
    )

    print("기록이 저장되었습니다.")
    print()