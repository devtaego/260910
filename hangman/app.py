from hangman.hangman_play import hangman_play
from hangman.hangman_ranking import show_ranking


def hangman_app(user_id):

    while True:

        print("=" * 50)
        print(f"{'HANGMAN':^50}")
        print("=" * 50)
        print("1. 게임 시작")
        print("2. 랭킹 보기")
        print("3. 메인 메뉴")

        try:
            menu_number = int(input("선택 : "))
        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        print()

        if menu_number == 1:
            hangman_play(user_id)

        elif menu_number == 2:
            show_ranking()

        elif menu_number == 3:
            break

        else:
            print("올바르지 않은 번호입니다.")