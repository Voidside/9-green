""" Tashqi kutubxonalar """
""" datetime """
import datetime

hozir = datetime.datetime.now()

# print(hozir.year)
# print(hozir.date())
# print(hozir.month)
# print(hozir.weekday())
# print(hozir.day)
# print(hozir.hour)
# print(hozir.minute)
# print(hozir.second)
# print(hozir.microsecond)


"""
link -> https://docs.python.org/3/library/datetime.html
link -> https://www.w3schools.com/python/python_datetime.asp
"""


# print(hozir.date())
# print(hozir.strftime("%A"))

# print(hozir.strftime("%B"))

# print(hozir.strftime("%C"))

# print(hozir.strftime("%a"))

# print(hozir.strftime("%b"))

# print(hozir.strftime("%y"))



# print(f"Sana: {hozir.strftime("A")}")

# Sanadan sanani ayirish
# bugun = datetime.date.today()
# ramazon = datetime.date(2025, 3, 1)

# print(ramazon-bugun)


# Vaqtdan vaqtni ayirish
# bugun1 =    datetime.datetime.now()
# ramazon = datetime.datetime(2025, 3, 1, 00, 00, 1)

# print(bugun1)
# print(ramazon)

# farq = ramazon-bugun1
# print(farq)
# print(farq.days)


# print(farq.seconds)



# t_sana = datetime.datetime(2001, 1, 18, 3, 0, 0)
# print(t_sana)

# print(t_sana + datetime.datetime(days=20, hour=8))



# hozir = datetime.datetime.now()



# t_yil = input(f"ni kiriting:")
# t_oy = input(f"ni kiriting:")
# t_kun = input(f"ni kiriting:")


# t_yil = 2009
# t_oy = 12
# t_kun = 30

# t_sana = datetime.date(t_yil, t_oy, t_kun)

# bugun = datetime.


# bugun1 =    datetime.datetime.now()


# print(f"Bugun sana va vaqt:{bugun1.day} soat{bugun1.hour}:{bugun1.minute}")

# print(f"Bugun sana: {bugun1.day}")

# print(f"Bugun vaqt: {bugun1.hour}:{bugun1.minute}")




# year = int(input("Type in year: "))
# month = int(input("Type in month: "))
# day = int(input("Type in day: "))

# date = datetime.datetime(year, month, day)

# if date.year < bugun.year or date.month < bugun.month:
#     print("404 Not found!")
# else:
#     result = date-bugun
#     print(f"Days left: {result}")




today = datetime.date.today()

# b_month = int(input("Type in birth month"))
# b_day = int(input("Type in birth day"))

# date = datetime.date(today.year, b_month, b_day)
# date1 = datetime.date(today.year+1, b_month, b_day)

# if date > today:
#     print(f"Days left: {(date-today).days}")
# elif date < today:
#     print(f"Days left: {(date1-today).days}")
# else:
#     print(f"Happy birthday!")


# today = datetime.date.today()
# day = int(input("Type in days: "))

# date = today + datetime.timedelta(days=day)

# print(f"After {day} days date will be: {date.day}-{date.strftime("%B")} {date.year}-year. Weekday: {date.strftime("%A")}")

"""
link -> https://www.w3schools.com/python/module_math.asp
link -> https://docs.python.org/3/library/math.html
"""


""" RegEx - Regular Expressions """
import re 

# world1 = "python"
# world2 = "Hello"
# world3 = "notebook"

# print(re.match("^p....n", world1))
# print(re.match("^H...o", world2))
# print(re.match("^n......k", world3))


# ism = input("Ismingizni kiriting: ")

# if re.match("^M", ism):
#     print(f"Salom {ism} sizning  ismingiz M harfi bn boshlanadi.")
# else: 
#     print(f"Salom {ism}")



# Extract phone number from a string
# extract_phone_number_pattern = "\\+998[1-9][0-9]{7,14}"
# re.findall(extract_phone_number_pattern, 'You can reach me out at +12223334444 and +56667778888') # returns ['+12223334444', '+56667778888']



import re

# phone_number_pattern = "^[+]998[\s][0-9]{2}[\s][0-9]{3}[-][0-9]{2}[-][0-9]{2}"
# tel = input("Nomer kiriting: ")
# if re.match(phone_number_pattern, tel):
#     print("Siz to'g'ri raqam kiritdingiz")
# else:
#     print(f"Siz noto'g'ri raqam kiritdingiz")



"""
link -> https://docs.python.org/3/howto/regex.html
link -> https://docs.python.org/3/library/re.html
link -> https://www.w3schools.com/python/python_regex.asp
"""
# matn = """
#     fake@gmail.com
# """


# email_pattern = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
# email = re.search(email_pattern, matn)
# print(email)




""" 1 """
word = "python aaaaa  bbbb ddddd"
word_pattern = r'\b[a-z]{5}\b'

print(re.findall(word_pattern, word))



""" 2 """
date_pattern = r"[0-9]{4}[-][0-9]{2}[-][0-9]{2}"
stt = """2025-02-20 2009-12-30"""
print(re.findall(date_pattern, stt))


""" 3 """
