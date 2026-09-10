# import random
#
# lotto_history = []
#
# ranking = []
#
# def lotto_sort(lotto):
#     lotto.sort()
#     print(lotto)
#
# def update_ranking(nickname,attempt):
#     for player in ranking:
#         if player[0] == nickname:
#             if attempt < player[1]:
#                 player[1] = attempt
#             return
#
#     ranking.append([nickname,attempt])
#
# def difficulty_select_message(number):
#
#     if number == 1:
#         return "쉬움", "시도 횟수 제한이 없습니다.", 0
#     elif number == 2:
#         return "중간", "최대 10회까지 시도할 수 있습니다.", 10
#     elif number == 3:
#         return "어려움", "최대 5회까지 시도할 수 있습니다.", 5
#
#     return None
#
#
# def difficulty_select():
#
#     print("난이도를 선택해주세요!")
#     print("1. 쉬움 - 횟수 제한 없음")
#     print("2. 중간 - 10회 제한")
#     print("3. 어려움 - 5회 제한")
#
#     difficulty = int(input())
#     result = difficulty_select_message(difficulty)
#
#     if result is None:
#         print("올바르지 않은 난이도입니다!")
#         return None
#
#     difficulty_name, message, max_attempt = result
#     print(f"{difficulty_name} 난이도를 선택하셨습니다!")
#     print(message)
#     return max_attempt
#
# def play_up_down():
#     print("****** 숫자 UP & DOWN 게임에 오신걸 환영합니다! ******")
#     print()
#
#     max_attempt = difficulty_select()
#     if max_attempt is None:
#         return
#
#     print()
#     nickname =input("닉네임을 입력해주세요! ")
#     answer = random.randint(1, 100)
#     attempt = 0
#
#     print()
#
#     # 임시용 정답 보이기
#     # print(answer)
#
#     print("1부터 100 사이의 숫자를 입력해주세요!")
#
#     while(True):
#         if max_attempt != 0 and attempt >= max_attempt:
#             print("시도 횟수를 모두 사용하셨습니다!")
#             print(f"정답은 {answer} 이었습니다!")
#             break
#
#         guess = int(input())
#         attempt += 1
#
#         if guess > answer :
#             print("더 작은 수를 입력하세요!")
#         elif guess < answer :
#             print("더 큰 수를 입력하세요!")
#         else :
#             print("정답입니다! ",end="")
#             print(f"{attempt}번 만에 맞추셨습니다!")
#             print()
#             update_ranking(nickname,attempt)
#             break
#
#
# def show_up_down_ranking():
#     if len(ranking) == 0:
#         print("랭킹 기록이 존재하지 않습니다!")
#         print()
#         return
#
#     for i in range(len(ranking)):
#
#         for j in range(i + 1, len(ranking)):
#
#             if ranking[i][1] > ranking[j][1]:
#                 ranking[i], ranking[j] = ranking[j], ranking[i]
#
#             elif ranking[i][1] == ranking[j][1]:
#
#                 if ranking[i][0] > ranking[j][0]:
#                     ranking[i], ranking[j] = ranking[j], ranking[i]
#
#     print("****** UP & DOWN 랭킹 ******")
#     print()
#     for rank, player in enumerate(ranking, start=1):
#         print(f"{rank}위 : {player[0]} - {player[1]}회")
#
#     print()
#
#
# def up_down_menu():
#     while (True) :
#         print("1. UP & DOWN 게임하기 / 2. UP & DOWN 랭킹보기 / 3. 메인 메뉴로 ")
#         menu_number = int(input())
#         print()
#
#         if menu_number == 1:
#             play_up_down()
#         elif menu_number == 2:
#             show_up_down_ranking()
#         elif menu_number == 3:
#             print("메인 메뉴로 이동합니다!")
#             print()
#             break
#         else:
#             print("올바르지 않은 번호입니다! 다시 입력하세요.")
#             print()
#
# def lotto_extraction():
#     while(True):
#         print("1. 자동 추출 / 2. 수동 추출 (반자동 가능) / 3. 메뉴로 돌아가기")
#         menu_number = int(input())
#         print()
#
#         if menu_number == 1:
#             lotto_freemode()
#         elif menu_number == 2:
#             lotto_selectmode()
#         elif menu_number == 3:
#             print("메인 메뉴로 이동합니다!")
#             print()
#             break
#         else :
#             print("올바르지 않은 번호입니다! 다시 입력하세요.")
#             print()
#
# def lotto_freemode():
#     lotto = []
#     while len(lotto) < 6:
#         x = random.randint(1, 45)
#
#         if x not in lotto:
#             lotto.append(x)
#
#     lotto.sort()
#
#     print("추천 번호는 ", end="")
#
#     for i in range(6):
#         print(lotto[i], end=" ")
#
#     print("입니다!")
#     print()
#
#     lotto_history.append(lotto)
#
# def lotto_selectmode():
#     lotto = []
#
#     while len(lotto) < 6:
#
#         print()
#         print("원하시는 번호를 입력해주세요!")
#         print("(모두 자동으로 입력하고 싶으시면 0을 눌러주세요!)")
#
#         wantnum = int(input())
#
#         if wantnum >= 1 and wantnum <= 45:
#
#             if wantnum not in lotto:
#
#                 lotto.append(wantnum)
#
#                 print(
#                     f"지금까지 {len(lotto)}개 입력하셨습니다! "
#                     "다음 번호를 입력해주세요!"
#                 )
#
#             elif wantnum in lotto:
#
#                 print("이미 입력한 숫자입니다! 다른 숫자를 입력해주세요!")
#
#             lotto_sort(lotto)
#
#         elif wantnum == 0:
#
#             while len(lotto) < 6:
#
#                 x = random.randint(1, 45)
#
#                 if x not in lotto:
#                     lotto.append(x)
#
#             lotto_sort(lotto)
#
#         else:
#
#             print("올바르지 않은 숫자입니다! 다시 입력하세요!")
#             continue
#
#         if len(lotto) == 6:
#             lotto_history.append(lotto)
#
# def lotto_record():
#     if len(lotto_history) == 0:
#         print("로또 번호 이력이 존재하지 않습니다!")
#         print()
#         return
#
#
#     print("****** 로또 번호 이력 ******")
#     print()
#
#     for i, lotto in enumerate(lotto_history, start = 1):
#
#         print(f"{i}회차 번호 : ", end="")
#
#         for number in lotto:
#             print(number, end=" ")
#
#         print()
#
#     print()
#
# def lotto_menu():
#     while (True):
#         print("1. 로또 번호 추출 / 2. 로또 이력 보기 / 3. 메인 메뉴")
#         menu_number = int(input())
#         print()
#
#         if menu_number == 1:
#             lotto_extraction()
#         elif menu_number == 2:
#             lotto_record()
#         elif menu_number == 3:
#             print("메인 메뉴로 이동합니다!")
#             print()
#             break
#         else:
#             print("올바르지 않은 번호입니다! 다시 입력하세요.")
#             print()
#
# def main():
#     print("메뉴를 선택해주세요!")
#
#     while True:
#         print("1. UP & DOWN / 2. 로또 / 3. 게임종료")
#         menu_number = int(input())
#         print()
#
#         if menu_number == 1:
#             up_down_menu()
#         elif menu_number == 2:
#             lotto_menu()
#         elif menu_number == 3:
#             print("게임을 종료합니다.")
#             break
#         else:
#             print("올바르지 않은 번호입니다!")
#
# main()
#
#
#
