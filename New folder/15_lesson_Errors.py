"""https://www.tutorialsteacher.com/python/error-types-in-python"""


""" try-except """

# try:
#     son = int(input("Son kiriting: "))
#     print(f"{son} ning kavadrati {son**2}")
# except:
#     print("Siz faqat son kirita olasiz")

# print("Dastur davomi.")



# try:
#     x = int(input("Sonni kiriting: "))
#     y = int(input("Sonni kiriting: "))
#     print(x/y)
# except ZeroDivisionError:
#     print("Sonni nolga bolib bo'lmaydi!")
# except NameError:
#     print("'x' degan o'zgaruvchi topilmadi!")
# except:
#     print("Boshqa xatolik yuzaga keldi!")



""" Calculator """
def cal():
    """ """
    while True:
            try:
                num1 = input("Son kiriting(Chiqish uchun 'exit'): ")
                if num1 == "exit":
                    break
                sign = input("Amal kiriting(Chiqish uchun 'exit'): ")
                if num1 == "exit":
                    break
                num2 = input("Son kiriting(Chiqish uchun 'exit'): ")
                if num1 == "exit":
                    break
            except ValueError:
                 print(f"Siz faqat son kiritishingiz mumkin!")
            if num2.isdigit():
                if sign == "+":
                    print(f"{int(num1+num2)}")
                elif sign == "-":
                    print(f"{int(num1-num2)}")
                elif sign == "*":
                    print(f"{int(num1*num2)}")
                elif sign == ":":
                    try:
                        print(f"{int(num1/num2)}")
                    except ZeroDivisionError:
                        print(f"Sonni nolga bolish mumkin emas!")
                else:
                    print(f"Value error")
            
            

print(cal())

# num1 = int(input("Son kiriting: "))
# amal = input("Amal kiriting: ")
# num2 = int(input("Son kiriting: "))