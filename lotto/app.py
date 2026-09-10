from lotto.lotto_auto import lotto_auto
from lotto.lotto_manual import lotto_manual
from lotto.lotto_records import lotto_records
from lotto.lotto_semi_auto import lotto_semi_auto


def lotto_app(user_id):

    while True:

        print("=" * 50)
        print("                    LOTTO")
        print("=" * 50)
        print("1. 자동 번호")
        print("2. 수동 번호")
        print("3. 반자동 번호")
        print("4. 번호 이력 보기")
        print("5. 메인 메뉴")

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
            lotto_semi_auto(user_id)

        elif menu_number == 4:
            lotto_records(user_id)

        elif menu_number == 5:
            break

        else:
            print("올바르지 않은 번호입니다.")