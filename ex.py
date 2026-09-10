import random

# 자전거 목록
bikes = [
    ("빨강 스포츠 자전거", 0.25),
    ("노랑 스포츠 자전거", 0.25),
    ("파랑 스포츠 자전거", 0.25),
    ("주황 스포츠 자전거", 0.25),

    ("일반 두발 자전거", 25),
    ("어린이용 자전거", 20),
    ("생활용 자전거", 20),
    ("접이식 자전거", 15),
    ("미니 자전거", 10),
    ("중고 자전거", 9)
]

# 11회 뽑기 1세트 가격
cost = 40000 * 1.34

total_cost = 0
set_count = 0
sports_count = 0

while True:

    print()
    print("===== 자전거 뽑기 =====")
    print("1. 11회 뽑기")
    print("2. 누적 결과")
    print("3. 종료")

    select = int(input("선택: "))

    if select == 1:

        set_count += 1
        total_cost += cost

        print()
        print(f"===== {set_count}번째 11회 뽑기 =====")

        for i in range(11):

            number = random.uniform(0, 100)
            current = 0

            for bike, probability in bikes:
                current += probability

                if number <= current:

                    print(f"{i + 1}회 → {bike}")

                    if "스포츠" in bike:
                        sports_count += 1
                        print("🎉 스포츠 자전거 당첨!")

                    break

        print()
        print(f"이번 뽑기 비용: {cost:,.0f} 원")
        print(f"누적 비용: {total_cost:,.0f} 원")

    elif select == 2:

        print()
        print("===== 누적 결과 =====")
        print(f"뽑기 세트: {set_count}회")
        print(f"총 뽑기 횟수: {set_count * 11}회")
        print(f"스포츠 자전거 당첨: {sports_count}개")
        print(f"누적 비용: {total_cost:,.0f} 원")

        if set_count > 0:
            print(f"1세트 비용: {cost:,.0f} 원")

    elif select == 3:

        print("뽑기를 종료합니다.")
        break

    else:
        print("잘못된 번호입니다.")