
import math
import datetime
""" 2 """
# print(abs(-54))
# print(pow(7, 3))
# print(math.ceil(72.99))
# print(math.floor(72.99))
# print(math.factorial(7))



""" 3 """
# today = datetime.date.today()
# week = int(input("Hafta kiriting: "))

# date = today + datetime.timedelta(weeks=week)
# print(f"{week} haftadan keyingi sana: {date.strftime("%d-%B %Y-yil. Haftaning %A kuni bo'ladi.")}")



""" 4 """
# today1 = datetime.date.today()

# oy = int(input("Tug'ilgan oyingizni kiriting: "))
# kun = int(input("Tug'ilgan kuningizni kiriting: "))

# date1 = datetime.date(today1.year, oy, kun)
# date2 = datetime.date(today1.year-1, oy, kun)

# if today1 > date1:      
#     print(f"Sizning tug'ilgan kuningiz {(today1-date1).days} kun oldin o'tib ketgan.")
# elif today1 < date1:
#     print(f"Sizning tug'ilgan kuningiz {(today1-date2).days} kun oldin o'tib ketgan.")



""" 5 """
# today2 = datetime.date.today()

# oy = int(input("Tug'ilgan oyingizni kiriting: "))
# kun = int(input("Tug'ilgan kuningizni kiriting: "))

# date1 = datetime.date(today2.year, oy, kun)
# date2 = datetime.date(today2.year+1, oy, kun)

# if today2 > date1:
#     print(f"Sizning tug'ilgan kuningizga {(date2-today2).days} kun qoldi.")
# elif today2 < date1:
#     print(f"Sizning tug'ilgan kuningizga {(date1-today2).days} kun qoldi.")

import re
num = "WB-02K-1717"

pattern1 = "^[A-Z]{2}[-][0-9]{2}[A-Z][-][0-9]{4}$"
pattern2 = "^[A-Z]{2}[-][0-9]{2}[A-Z][-][0-9]{4}$"

s = re.match(pattern1, num)
s1 = re.match(pattern2, num)

print(s)
print(s1)