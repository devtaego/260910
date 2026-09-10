from common import LoginManager
from hangman import hangman_app
from lotto import lotto_app
from updown import updown_app


def main():

    login_manager = LoginManager()

    user_id = login_manager.login()

    while True:

        print("="*50)
        print("                    GAME CENTER")
        print("="*50)
        print("1. 업앤다운")
        print("2. 행맨")
        print("3. 로또")
        print("4. 로그아웃")

        try:
            menu_number = int(input("선택 : "))
        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        print()

        if menu_number == 1:
            updown_app(user_id)

        elif menu_number == 2:
            hangman_app(user_id)

        elif menu_number == 3:
            lotto_app(user_id)

        elif menu_number == 4:
            print("로그아웃합니다.")
            break

        else:
            print("올바르지 않은 번호입니다.")


if __name__ == "__main__":
    main()