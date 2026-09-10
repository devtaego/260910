from lotto.lotto_play import lotto_play
from lotto.lotto_records import lotto_records


def lotto_app(user_id):

    while True:

        print("=" * 50)
        print("                    LOTTO")
        print("=" * 50)
        print("1. 게임 시작")
        print("2. 기록 보기")
        print("3. 메인 메뉴")

        try:
            menu_number = int(input("선택 : "))
        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        print()

        if menu_number == 1:
            lotto_play(user_id)

        elif menu_number == 2:
            lotto_records(user_id)

        elif menu_number == 3:
            break

        else:
            print("올바르지 않은 번호입니다.")