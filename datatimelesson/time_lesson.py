# import datetime


# x = datetime.datetime.today()
# print(x)

# x = datetime.date.today()
# print(x)

# x = datetime.datetime.today().time()
# print(x)

# import datetime

# y = datetime.datetime(2020, 2, 29, 18, 20, 50)
# print(y)
# # 2020-02-29 18:20:50

# print(y.strftime("%A, %d. %B %Y %I:%M%p"))
# print(y.strftime("%C %Y %d %w"))

# # Saturday, 29. February 2020 06:20PM

# import datetime
# import locale

# locale.setlocale(locale.LC_TIME, "lt_LT.UTF-8")
# x = datetime.datetime(2020, 2, 29, 18, 20, 50)
# print(x.strftime("%A, %d. %B %Y %I:%M%p"))

# import datetime
# now = datetime.datetime.now()
# print(now)
# print(now - datetime.timedelta(days=5))
# print(now + datetime.timedelta(hours=5))
# print(now + datetime.timedelta(days=20, hours=8))

# # 2020-11-25 12:26:14.575023
# # 2020-11-20 12:26:14.575023
# # 2020-11-25 17:26:14.575023
# # 2020-12-15 20:26:14.575023

# import datetime
# now = datetime.datetime.now()
# nepriklausomybes_diena = datetime.datetime(1990, 3, 11)
# skirtumas = now - nepriklausomybes_diena
# print(skirtumas.days)


# import datetime

# now = datetime.datetime.today()

# print(now.year)
# print(now.month)
# print(now.weekday())
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.microsecond)

# 2020
# 11
# 2
# 25
# 12
# 13
# 45
# 760594


# import datetime

# pradzia = datetime.datetime.today()
# for x in range(10000):
#     print(x)

# pabaiga = datetime.datetime.today()
# print(f"Programa užtruko {(pabaiga - pradzia).total_seconds()}")


# 2 užduotis
# Parašyti programą, kuri:

# Atspausdintų dabartinę datą ir laiką
# Atimtų iš dabartinės datos ir laiko 5 dienas ir juos atspausdintų
# Pridėti prie dabartinės datos ir laiko 8 valandas ir juos atspausdintų
# Atspausdintų dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17
# Patarimas: naudoti datetime, timedelta (from datetime import timedelta)

import datetime

now = datetime.datetime.now()
five_day_diff = now - datetime.timedelta(days=5)
print(five_day_diff)
add_time = now + datetime.timedelta(days=8)
print(add_time)

print(now.strftime("%Y-%m-%d, %H:%M:%S"))
