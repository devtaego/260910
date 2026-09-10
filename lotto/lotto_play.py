from lotto.lotto_auto import lotto_auto
from lotto.lotto_manual import lotto_manual


def lotto_play(user_id):

    while True:

        print("=" * 50)
        print("                    LOTTO GAME")
        print("=" * 50)
        print("1. 자동 번호")
        print("2. 수동 번호")
        print("3. 로또 메뉴")

        try:
            menu_number = int(input("선택 : "))
        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        print()

        if menu_number == 1:
            lotto_auto(user_id)

        elif menu_number == 2:
            lotto_manual(user_id)

        elif menu_number == 3:
            break

        else:
            print("올바르지 않은 번호입니다.")