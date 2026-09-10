ranking = []


def save_ranking(user_id, attempts, difficulty):
    for record in ranking:
        if (
            record["id"] == user_id
            and record["difficulty"] == difficulty
        ):
            if attempts < record["attempts"]:
                record["attempts"] = attempts
            return

    ranking.append({
        "id": user_id,
        "attempts": attempts,
        "difficulty": difficulty
    })


def show_ranking():
    print("=" * 50)
    print(f"{'HANGMAN RANKING':^50}")
    print("=" * 50)

    if len(ranking) == 0:
        print("등록된 기록이 없습니다.")
        print()
        return

    for difficulty in ("EASY", "NORMAL", "HARD"):
        difficulty_ranking = sorted(
            (
                record for record in ranking
                if record["difficulty"] == difficulty
            ),
            key=lambda record: (record["attempts"], record["id"])
        )

        if not difficulty_ranking:
            continue

        print()
        print(f"[ {difficulty} RANKING ]")
        print("+------+------------------+------------+")
        print("| 순위  | 닉네임            | 시도 횟수   |")
        print("+------+------------------+------------+")

        for index, record in enumerate(difficulty_ranking, start=1):
            print(
                f"| {index:^4} "
                f"| {record['id']:<16} "
                f"| {str(record['attempts']) + '회':^10} |"
            )

        print("+------+------------------+------------+")
        print()