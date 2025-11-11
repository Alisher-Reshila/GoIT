
from datetime import datetime


def get_days_from_today(date):
    given_date = datetime.strptime(date, '%Y-%m-%d')
    today = datetime.today().date()
    given_date = given_date.date()
    delta = today - given_date
    return delta.days

test_date = [
    '2025-12-01',
    '2024-11-24',
    '2025-11-12',
    '2025-03-25',
    '2026-06-15'
]

print("Сегодня:", datetime.today().strftime('%Y-%m-%d'))
print('-' * 40)

for d in test_date:
    result = get_days_from_today(d)
    sign = "назад" if result > 0 else "вперёд" if result < 0 else "сегодня"
    print(f"{d} -> {result} days ({abs(result)} {sign})")
