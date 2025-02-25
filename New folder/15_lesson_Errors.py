"""https://www.tutorialsteacher.com/python/error-types-in-python"""


""" try-except """

try:
    son = int(input("Son kiriting: "))
    print(f"{son} ning kavadrati {son**2}")
except:
    print("Siz faqat son kirita olasiz")

print("Dastur davomi.")



try:
    x = int(input("Sonni kiriting: "))
    y = int(input("Sonni kiriting: "))
    print(x/y)
except ZeroDivisionError:
    print("Sonni nolga bolib bo'lmaydi!")
except NameError:
    print("'x' degan o'zgaruvchi topilmadi!")
except:
    print("Boshqa xatolik yuzaga keldi!")