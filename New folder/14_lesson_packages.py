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
bugun = datetime.date.today()
ramazon = datetime.date(2025, 3, 1)

# print(ramazon-bugun)


# Vaqtdan vaqtni ayirish
bugun1 =    datetime.datetime.now()
ramazon = datetime.datetime(2025, 3, 1, 00, 00, 1)

# print(bugun1)
# print(ramazon)

farq = ramazon-bugun1
# print(farq)
# print(farq.days)


# print(farq.seconds)



# t_sana = datetime.datetime(2001, 1, 18, 3, 0, 0)
# print(t_sana)

# print(t_sana + datetime.datetime(days=20, hour=8))



hozir = datetime.datetime.now()



# t_yil = input(f"ni kiriting:")
# t_oy = input(f"ni kiriting:")
# t_kun = input(f"ni kiriting:")


t_yil = 2009
t_oy = 12
t_kun = 30

t_sana = datetime.date(t_yil, t_oy, t_kun)

# bugun = datetime.