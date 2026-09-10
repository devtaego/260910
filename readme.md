# 🎮 Gaming Project

Python을 이용한 미니게임 프로젝트

프로젝트의 주요 목표는 하나의 파일에 모든 기능을 작성하는 것이 아니라,
기능과 책임에 따라 **Function → Class → Module → Package**로 분리하여 관리하는 것이다.

---

# 1. 📁 프로젝트 구조

```text
gaming_project/
│
├── main.py
│
├── common/
│   ├── __init__.py
│   ├── config.py
│   └── login_manager.py
│
├── updown/
│   ├── __init__.py
│   ├── app.py
│   ├── updown_play.py
│   └── updown_ranking.py
│
├── hangman/
│   ├── __init__.py
│   ├── app.py
│   ├── hangman_play.py
│   └── hangman_ranking.py
│
└── lotto/
    ├── __init__.py
    ├── app.py
    ├── lotto_auto.py
    ├── lotto_manual.py
   ├── lotto_semi_auto.py
    └── lotto_records.py
```

---

# 2. 🏗️ 프로젝트 계층

```text
Project
│
├── main.py
│
├── Package
│   ├── common
│   ├── updown
│   ├── hangman
│   └── lotto
│
│       ↓
│
├── Module
│   ├── login_manager.py
│   ├── updown_play.py
│   ├── updown_ranking.py
│   ├── hangman_play.py
│   ├── hangman_ranking.py
│   ├── lotto_auto.py
│   ├── lotto_manual.py
│   ├── lotto_semi_auto.py
│   └── lotto_records.py
│
│       ↓
│
├── Class
│   └── LoginManager
│
│       ↓
│
└── Function
    ├── login()
    ├── start_game()
    ├── check_answer()
    ├── save_record()
    └── ...
```

> 모든 Module이 반드시 Class를 가져야 하는 것은 아니다.
> 단순한 기능은 Function 중심으로 작성하고, 상태와 데이터를 함께 관리해야 할 경우 Class를 사용한다.

---

# 3. 🔐 프로그램 전체 흐름

프로그램은 **로그인부터 시작한다.**

```text
                         main.py
                            │
                            ▼
                    ┌──────────────┐
                    │    로그인    │
                    └──────┬───────┘
                           │
                     로그인 성공
                           │
                           ▼
                    ┌──────────────┐
                    │    메인 메뉴 │
                    └── login()────┘

# 4. 🏠 메인 메뉴
                     현재 프로젝트에서 사용하는 Class는 `LoginManager`이며,
                     게임 랭킹과 로또 기록은 모듈 전역 리스트와 함수로 관리한다.

                     ---

                     ## 실행 방법

                     프로젝트 루트에서 다음 명령을 실행한다.

                     ```bash
                     python main.py
                     ```

                     테스트 계정으로 로그인한 뒤 메인 메뉴에서 게임을 선택한다.
로그인에 성공하면 전체 게임을 선택할 수 있는 메인 메뉴로 이동한다.

```text
==================================================
            GAME CENTER
==================================================

1. 업앤다운
2. 행맨
3. 로또
4. 로그아웃

선택 :
```

### 메인 메뉴의 역할

`main.py`는 전체 프로그램의 흐름을 담당한다.

```text
main.py
│
├── 로그인
│
├── 메인 메뉴
│   ├── 업앤다운 → updown.app
│   ├── 행맨     → hangman.app
│   └── 로또     → lotto.app
│
└── 로그아웃
```

`main.py`에서 각각의 게임 내부 로직을 직접 처리하지 않는다.

---

# 5. 🔑 로그인

로그인은 모든 게임에서 공통으로 사용하는 기능이다.

따라서 특정 게임 Package에 넣지 않고 `common` Package에서 관리한다.

```text
common/
├── config.py
└── login_manager.py
```

## 테스트 계정

```text
ID       : admin
Password : 1234
```

> 해당 계정은 학습 및 테스트용 계정이다.

---

## 로그인 흐름

```text
아이디 입력
    ↓
아이디 확인
    ↓
비밀번호 입력
    ↓
비밀번호 검증
    ↓
┌───────────────┐
│               │
▼               ▼
성공            실패
│               │
▼               ▼
메인 메뉴       재로그인
```

---

## 현재 인증 방식

학습 프로젝트에서는 테스트용 ID와 비밀번호를 `common/config.py`에 저장하고,
`LoginManager`가 입력값과 비교한다.

```text
password = "1234"
```

실제 서비스에서는 비밀번호를 소스 코드에 직접 저장하지 않고,
Argon2, bcrypt, PBKDF2와 같은 전용 해시 방식을 사용해야 한다.

---

# 6. 👤 로그인 ID 관리

로그인에 성공하면 현재 로그인한 사용자의 ID를 게임에 전달한다.

예:

```text
로그인
 ↓
ID = "admin"
 ↓
메인 메뉴
 ↓
업앤다운 선택
 ↓
현재 ID = "admin"
```

게임이 끝난 후에는 게임 결과와 ID를 함께 기록한다.

```text
admin + 게임 결과
```

---

# 7. 🎯 UP & DOWN

## Package 구조

```text
updown/
├── __init__.py
├── app.py
├── updown_play.py
└── updown_ranking.py
```

---

## UP & DOWN 메뉴

```text
==================================================
            UP & DOWN
==================================================

1. 게임 시작
2. 랭킹 보기
3. 메인 메뉴

선택 :
```

### 메뉴 흐름

```text
updown/app.py
│
├── 1. 게임 시작
│      ↓
│   updown_play.py
│
├── 2. 랭킹 보기
│      ↓
│   updown_ranking.py
│
└── 3. 메인 메뉴
       ↓
     main.py
```

---

## 게임 시작

`updown_play.py`에서 실제 게임을 담당한다.

```text
랜덤 숫자 생성
      ↓
사용자 숫자 입력
      ↓
UP / DOWN 판정
      ↓
정답 확인
      ↓
시도 횟수 계산
      ↓
게임 종료
```

게임 결과:

```text
ID       : admin
시도 횟수 : 5회
난이도   : NORMAL
```

---

## 랭킹 보기

`updown_ranking.py`에서 랭킹을 관리한다.

게임 결과에 로그인 ID를 함께 저장한다.

```text
ID       : admin
기록     : 5회
```

예:

```text
==================================================
             UP & DOWN RANKING
==================================================

[ EASY RANKING ]
+------+------------------+------------+
| 순위 | 닉네임             | 시도 횟수   |
+------+------------------+------------+
|  1   | admin            |     3회     |
+------+------------------+------------+
```

랭킹은 `EASY`, `NORMAL`, `HARD` 난이도별로 분리된다.
같은 사용자가 같은 난이도에서 여러 번 플레이하면 더 낮은 시도 횟수만 유지한다.

---

# 8. 📝 HANGMAN

## Package 구조

```text
hangman/
├── __init__.py
├── app.py
├── hangman_play.py
└── hangman_ranking.py
```

---

## HANGMAN 메뉴

```text
==================================================
          HANGMAN
==================================================

1. 게임 시작
2. 랭킹 보기
3. 메인 메뉴

선택 :
```

### 메뉴 흐름

```text
hangman/app.py
│
├── 1. 게임 시작
│      ↓
│   hangman_play.py
│
├── 2. 랭킹 보기
│      ↓
│   hangman_ranking.py
│
└── 3. 메인 메뉴
       ↓
     main.py
```

---

## 게임 시작

`hangman_play.py`에서 실제 행맨 게임을 담당한다.

```text
단어 선택
   ↓
단어 가리기
   ↓
알파벳 입력
   ↓
입력한 알파벳 표시
   ↓
정답 포함 여부 확인
   ↓
현재 단어 상태 갱신
   ↓
시도 횟수 계산
   ↓
성공 / 실패 확인
   ↓
게임 종료
```

게임 결과에 로그인 ID를 연결한다.

```text
ID       : admin
시도 횟수 : 5회
난이도   : EASY
```

---

## 랭킹 보기

`hangman_ranking.py`에서 랭킹을 관리한다.

```text
==================================================
           HANGMAN RANKING
==================================================

[ EASY RANKING ]
+------+------------------+------------+
| 순위 | 닉네임             | 시도 횟수   |
+------+------------------+------------+
|  1   | admin            |     5회     |
+------+------------------+------------+
```

행맨 랭킹도 `EASY`, `NORMAL`, `HARD` 난이도별로 분리된다.
같은 사용자의 같은 난이도 기록 중 가장 낮은 시도 횟수만 유지한다.

오답 횟수에 따라 ASCII 행맨이 단계적으로 표시되며,
마지막 전 단계에는 `😢`, 마지막 단계에는 `💀`가 표시된다.
정답을 맞히면 ASCII 성공 메시지와 총 시도 횟수가 출력된다.

---

# 9. 🎱 LOTTO

## Package 구조

```text
lotto/
├── __init__.py
├── app.py
├── lotto_auto.py
├── lotto_manual.py
├── lotto_semi_auto.py
└── lotto_records.py
```

---

## LOTTO 메뉴

```text
==================================================
                     LOTTO
==================================================

1. 자동 번호
2. 수동 번호
3. 반자동 번호
4. 번호 이력 보기
5. 메인 메뉴

선택 :
```

### 메뉴 흐름

```text
lotto/app.py
│
├── 1. 자동 번호 → lotto_auto.py
│
├── 2. 수동 번호 → lotto_manual.py
│
├── 3. 반자동 번호 → lotto_semi_auto.py
│
├── 4. 번호 이력 보기
│      ↓
│   lotto_records.py
│
└── 5. 메인 메뉴
       ↓
     main.py
```

---

## 자동 번호

`lotto_auto.py`

```text
자동 번호 선택
      ↓
랜덤 번호 생성
      ↓
6개 번호 선택
      ↓
번호 정렬
   ↓
사용자 기록 저장
```

---

## 반자동 번호

`lotto_semi_auto.py`

```text
원하는 번호 입력
   ↓
0 입력
   ↓
남은 번호 자동 생성
   ↓
번호 정렬
   ↓
사용자 기록 저장
```

사용자가 원하는 번호를 입력하다가 `0`을 입력하면,
입력한 번호를 제외한 나머지 번호를 자동으로 생성한다.

---

## 수동 번호

`lotto_manual.py`

```text
번호 입력
   ↓
범위 확인
   ↓
중복 확인
   ↓
6개 번호 완성
   ↓
번호 정렬
   ↓
사용자 기록 저장
```

---

## 로또 기록

로또는 게임의 승패를 기준으로 하는 랭킹이 아니라
**현재 사용자가 생성한 번호와 방식을 기록하는 형태**로 관리한다.

`lotto_records.py`

```text
ID + 방식 + 번호
```

예:

```text
==================================================
           LOTTO RECORDS
==================================================

ID        방식      번호
admin     자동      3, 12, 18, 25, 31, 42
admin     수동      1, 7, 15, 22, 33, 41
```

기록 보기에서는 로그인한 사용자의 기록만 출력한다.

---

# 10. 🔄 전체 데이터 흐름

로그인 ID가 게임 결과까지 전달되는 구조이다.

```text
                         로그인
                            │
                            ▼
                       ID = admin
                            │
                            ▼
                        메인 메뉴
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
       UP&DOWN            HANGMAN            LOTTO
          │                 │                 │
          ▼                 ▼                 ▼
       게임 시작          게임 시작          게임 시작
          │                 │                 │
          ▼                 ▼                 ▼
       게임 결과          게임 결과          게임 결과
          │                 │                 │
          ▼                 ▼                 ▼
    admin + 결과       admin + 결과       admin + 결과
          │                 │                 │
          ▼                 ▼                 ▼
      랭킹 저장          랭킹 저장          기록 저장
```

---

# 11. 🧩 파일별 책임

| 파일                           | 책임              |
| ---------------------------- | --------------- |
| `main.py`                    | 프로그램 시작 및 전체 메뉴 |
| `common/config.py`           | 공통 설정           |
| `common/login_manager.py`    | 로그인 및 인증        |
| `updown/app.py`              | 업앤다운 메뉴 및 흐름    |
| `updown/updown_play.py`      | 업앤다운 게임 진행      |
| `updown/updown_ranking.py`   | 업앤다운 랭킹         |
| `hangman/app.py`             | 행맨 메뉴 및 흐름      |
| `hangman/hangman_play.py`    | 행맨 게임 진행        |
| `hangman/hangman_ranking.py` | 행맨 랭킹           |
| `lotto/app.py`               | 로또 메뉴 및 전체 흐름      |
| `lotto/lotto_auto.py`        | 자동 번호 생성        |
| `lotto/lotto_manual.py`      | 수동 번호 입력        |
| `lotto/lotto_semi_auto.py`   | 반자동 번호 생성        |
| `lotto/lotto_records.py`     | 로또 기록 관리        |

---

# 12. 🧱 Function / Class / Module / Package

## Function

`def`를 사용하여 하나의 기능을 분리한다.

```text
login()
start_game()
check_answer()
save_record()
show_ranking()
```

---

## Class

데이터와 관련 기능을 하나의 객체로 묶을 필요가 있을 때 사용한다.

예:

```text
LoginManager
```

예상 구조:

```text
LoginManager
│
└── login()
```

현재 프로젝트에서 사용하는 Class는 `LoginManager`이며,
게임 랭킹과 로또 기록은 모듈 전역 리스트와 함수로 관리한다.

---

## Module

하나의 `.py` 파일을 Module로 사용한다.

```text
login_manager.py
updown_play.py
updown_ranking.py
lotto_auto.py
```

관련 기능을 Module 단위로 분리한다.

---

## Package

관련된 Module들을 폴더로 묶는다.

```text
common/
updown/
hangman/
lotto/
```

---

# 13. 🔗 계층 관계

```text
Package
   │
   └── Module
          │
          ├── Class
          │     │
          │     └── Function
          │
          └── Function
```

하지만 반드시 다음과 같은 구조가 되어야 하는 것은 아니다.

```text
Package
   ↓
Module
   ↓
Function
```

처럼 Class 없이 사용할 수도 있다.

중요한 것은 **기능의 성격에 맞게 분리하는 것**이다.

---

# 14. 🎯 오늘의 핵심 과제

## ① 로그인부터 시작

```text
main.py
   ↓
login_manager.py
   ↓
로그인 성공
   ↓
메인 메뉴
```

---

## ② 메인 메뉴에서 게임 선택

```text
메인 메뉴
│
├── 업앤다운
├── 행맨
└── 로또
```

---

## ③ 각 게임에 자체 메뉴 구성

```text
업앤다운
├── 게임 시작
├── 랭킹 보기
└── 메인 메뉴

행맨
├── 게임 시작
├── 랭킹 보기
└── 메인 메뉴

로또
├── 게임 시작
│   ├── 자동
│   └── 수동
├── 기록 보기
└── 메인 메뉴
```

---

## ④ 로그인 ID를 게임에 전달

```text
admin
  ↓
게임 시작
  ↓
게임 결과
  ↓
admin + 결과
  ↓
랭킹 / 기록
```

---

## ⑤ 기능별 Module 분리

```text
게임 진행
    ↓
*_play.py

랭킹
    ↓
*_ranking.py

로또 자동
    ↓
lotto_auto.py

로또 수동
    ↓
lotto_manual.py

로또 기록
    ↓
lotto_records.py
```

---

# 15. ⭐ 최종 구조

```text
                         gaming_project
                              │
                         ┌────┴────┐
                         │ main.py │
                         └────┬────┘
                              │
                            로그인
                              │
                              ▼
                         메인 메뉴
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
           updown          hangman          lotto
              │               │               │
              ▼               ▼               ▼
            app.py          app.py          app.py
              │               │               │
        ┌─────┼─────┐   ┌─────┼─────┐   ┌─────┼──────────┐
        ▼     ▼     ▼   ▼     ▼     ▼   ▼     ▼          ▼
       play ranking main  play ranking main play records  main
                                          │
                                          ▼
                                  ┌───────┴───────┐
                                  ▼               ▼
                                auto            manual
```

---

# 🚀 프로젝트 실행 흐름 요약

```text
1. 프로그램 실행
        ↓
2. 로그인
        ↓
3. 로그인 ID 저장
        ↓
4. 메인 메뉴
        ↓
5. 게임 선택
        ↓
6. 게임별 메뉴
        ↓
7. 게임 시작 / 랭킹 / 기록
        ↓
8. 게임 결과에 로그인 ID 연결
        ↓
9. 랭킹 또는 기록 저장
        ↓
10. 게임 메뉴로 복귀
        ↓
11. 메인 메뉴로 이동
        ↓
12. 로그아웃
```

---

# 💡 설계 원칙

### 하나의 파일에 모든 것을 넣지 않는다.

```text
❌ main.py
   ├── 로그인
   ├── 업앤다운
   ├── 행맨
   ├── 로또
   └── 랭킹
```

### 각각의 책임을 분리한다.

```text
✅ main.py
   → 전체 프로그램 연결

✅ login_manager.py
   → 로그인

✅ updown_play.py
   → 업앤다운 게임

✅ updown_ranking.py
   → 업앤다운 랭킹

✅ hangman_play.py
   → 행맨 게임

✅ hangman_ranking.py
   → 행맨 랭킹

✅ lotto_auto.py
   → 로또 자동

✅ lotto_manual.py
   → 로또 수동

✅ lotto_records.py
   → 로또 기록
```

**최종 목표는 각 Module이 자신의 역할만 담당하고, 상위 계층에서는 하위 기능을 호출하여 전체 프로그램을 구성하는 것이다.**