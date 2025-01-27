"""Theme: Sonlar(Lists) """

""" Sonlarning turlari """
# x = 1 #int
# y = 2.8 # float
# z = 1j # complex

""" Butun son turlari"""
# a = 15
# b = -8
# c = 0
# print(a)
# print(type(a))

"""O'nlik son turlari """
# x = 35e3 # 35000.0
# y = 12E4 # 120000.0
# z = 14.76
# print(x)
# print(type(x))

""" Sonni kvadratga ko'tarish"""
# f =3**4 # ** kvadrat belgisi
# print(f)

# from math import pow # power --> pow
# print(pow(2,6))

""" Sonni ildizdan chiqarish"""
# d = 16 
# from math import sqrt
# print(sqrt(d))

"""Yaxlidlash"""
# x = 32.222222223
# print(round(x))

""" Random """
# import random
# print(random.randrange(1, 10, ))

""" int()/ float()/ str()"""
# a = 5
# b = 12.5
# c = "Salom"

# print(b)
# print(type(b))
# b = int(b)
# print(b)
# print(type(b))

# print(type(a))
# print(a)

# a1 = float(a) # a ni o'nlik son(float)ga o'zgartiramiz

# print(type(a1))
# print(a1)

""" Mashq """
# son = 3232
# matn = "94948"
# pi = 3.14

# son = float(son)
# print(son)
# print(type(son))

# matn = int(matn)
# print(matn)
# print(type(matn))

# pi = int(pi)
# print(pi)
# print(type(pi))
# pi = str(pi)
# print(pi)
# print(type(pi))

# """ input  """
# ism = input("Ismingizni kiriting: ")
# yosh = int(input(f"{ism.title()} tug'ilgan yilingiz: "))
# yosh1 = 2024 - yosh
# print(f"Siz {yosh1} yoshdasiz ")

""" 01 """
# 01
#aylana uzunligi
# r = int(input("Radiusni kiriting: "))
# pi = 3.14
# print(f"Radiusi {r}ga teng bo'lgan aylananing uzunligi {2*pi*r} ga teng bo'ladi")

# # 02
# r = int(input("Radiusni kiriting: "))
# pi = 3.14
# print(f"Radiusi {r}ga teng bo'lgan doiraning yuzi {pi*r**2} ga teng bo'ladi")

# 03
# katet_a = int(input("a katetni kiriting: "))
# katet_b = int(input("b katetni kiriting: "))
# gipotenuza = katet_a**2 + katet_b**2
# from math import sqrt
# print(f"Katetlari {katet_a} va {katet_b} teng bo'lgan to'g'ri burchakli uchburchakning gipotenuzasi {int(sqrt(gipotenuza))}")

# 04
a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))
c = (a + b)/2
print(round(c))