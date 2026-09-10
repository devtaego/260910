records = []


def save_record(user_id, method, lotto):

    record = {
        "id": user_id,
        "method": method,
        "numbers": lotto
    }

    records.append(record)


def lotto_records(user_id):

    print("=" * 50)
    print(f"{'LOTTO RECORDS':^50}")
    print("=" * 50)

    user_records = []

    for record in records:

        if record["id"] == user_id:
            user_records.append(record)

    if len(user_records) == 0:

        print("저장된 기록이 없습니다.")
        print()
        return

    print(
        f"{'ID':<10}"
        f"{'방식':<10}"
        f"번호"
    )

    for record in user_records:

        numbers = ", ".join(
            map(str, record["numbers"])
        )

        print(
            f"{record['id']:<10}"
            f"{record['method']:<10}"
            f"{numbers}"
        )

    print()