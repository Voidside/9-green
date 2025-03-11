import datetime

""" 1 """
bugun = datetime.datetime.now()

# print(bugun.strftime("%w"))


""" 2 """
# print(bugun.strftime("%B"))


""" 3 """
# print(bugun.strftime("%a"))


""" 4 """
# print(f"Current time & date: {bugun.year}/{bugun.month}-{bugun.strftime("%B")}/{bugun.hour}:{bugun.minute}")


""" 5 """
# year = int(input("Type in year: "))
# month = int(input("Type in month: "))
# day = int(input("Type in day: "))

# date = datetime.datetime(year, month, day)

# if date.year < bugun.year or date.month < bugun.month:
#     print("!")
# else:
#     result = date-bugun
#     print(f"")