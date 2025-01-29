
"""1-mashq | 10 Ball
	4 dan 873 gacha bo’lgan toq sonli ro’yhat yarating va ro’yhatdagi har bir sonning ildizini chiqaring.
"""
""" 1 """
from math import sqrt
# sonlar = list(range(5, 873, 2))

# for son in sonlar:
#     print(sqrt(son))


"""
2-mashq | 10 Ball
Foydalanuvchidan uning ismini so’rang va unga quida keltirilgan javoblardan mosini qaytaring.
Dasturni tuzishda or operatoridan foydalanig !
Muslima  – Salom Muslima. Davramizda hush ko’rdik.
Zilola/Sevara  – Assalomu aleykum. Zilola/Sevara sizga qanday yordam berishim mumkin?
Anvar/Aziz  – Salom Anvar/Aziz . Bugun Qayerga boramiz ?
"""
""" 2 """
# ism = input("Ism kiriting:")

# if ism.lower() == "muslima":
#     print(f"Salom {ism.title()}. Davramizda xush ko'rdik")
# elif ism.lower() == "zilola" or ism.lower() == "sevara":
#     print(f"Assalomu aleykum. {ism.title()} sizga qanday yordam berishim mumkin?")
# elif ism.lower() == "anvar" or ism.lower() == "aziz":
#     print(f"Salom {ism.title()}. Bugun Qayerga boramiz?")



"""
3-mashq | 10 Ball | 102 dan 2020 gacha bo’lgan sonladan iborat ro’yhat yarating va ro’yhatdagi:
1000 gacha bo’lgan sonning 3-darajasini toping.
1500 dan katta barcha sonlarning o’zidan 4 taga kichik sonni toping.
Ro’yhatdagi 7 ga qoldiqsiz bo’linadigan sonlarning ildizini toping.
"""
""" 3 """
# sonlar = list(range(102, 2020))
# for son  in sonlar:
#     if son < 1000:
#         print(son**3)
#     elif son > 1500:
#         print(son-4)
#     elif son % 7 == 0:
#         print(sqrt(son))



"""
4-mashq | 10 Ball  | -322 dan -2 gacha bo’lgan barcha toq sonlarning:
1) 5 chi va 7 chi darajasini toping;
2) Ro’yhatdagi har bir sondan 4 taga kichik sonni konsulga chiqaring;
3) Ro’yhatning uzunligini o’lchang;
4) Ro’yhatdagi har bir sonning ildizini toping;
5) Ro’yhatni avval o’sish tartibida keyin esa kamayish tartibida tartiblab konsulga chiqaring;
"""
""" 4 """
# sonlar = list(range(3, 322))

# for son in sonlar:
#     print(son**5)
#     print(son**7)

#     print(son-4)

#     print(sqrt(son))

# print(len(sonlar))

# sonlar.sort()
# print(sonlar)
# sonlar.sort(reverse=True)
# print(son)


"""
5-mashq | 10 Ball | Kodni huddi shu ko’rinishda ko’chirib oling va undagi xatolarni topib to’g’irlang
a = float(input("1-sonni kirirting:"))
b = int(input("2-sonni kirirting:"))
if a<b:
print(f"{a}>{b}")
elif a<b:
print(f"{a}<{b}")
elif a != :
print(f"{a}={b}")
"""

# a = float(input("1-sonni kirirting:"))
# b = int(input("2-sonni kirirting:"))

# if a<b:
#     print(f"{a}<{b}")
# elif a>b:
#     print(f"{a}>{b}")
# elif a != b:
#     print(f"{a}={b}")