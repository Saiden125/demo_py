from datetime import date, timedelta
youbi = '月火水木金土日'
start = date(2019, 9, 14)
for d in range(14):
    cur = start + timedelta(days = d)
    wd = cur.weekday()
    print(cur, youbi[wd])