from datetime import datetime, timedelta

date = datetime(1901, 1, 1)
ans = 0
while date != datetime(2000, 12, 31):
    if date.weekday() == 6 and date.day == 1:
        ans += 1
    date += timedelta(days=1)

print(ans)

