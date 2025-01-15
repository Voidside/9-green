# son = range(102, 2200)
# for s in son:
#     if 1000 > s:
#         print(f"{s}ning 7 darajasi  {s**7}")
#     elif 1500 < s:
#         print(f"{s}dan 4 ta kichik {s-4}")


""" 2 """
# ismlar = ["Ali", "Olim", "Kamron", "Abdulloh", "Karim", "Usmon"]
# for i in ismlar:
#     if i == "Kamron" or i == "Karim":
#         print(f"Salom {i} ahvollaringiz yaxshimi")
#     else:
#         print(f"Assalomu aleykum {i}")


""" 3 """
# sonlar = [2, 6, -9, 0, 8.5, 21, 65, -34, 43.6,-44, 847, 0, 32, -41]
# for s in sonlar:
#     print(s+s)

# print(len(sonlar))
# print(min(sonlar))
# print(max(sonlar))


""" 4 """
# son5 = list(range(-2024, 2024, 2))
# print(max(son5))

# son6 = list(range(123, 87384, 2))
# print(min(son6))



""" 5 """
# mevalar = ["Olma", "malina", "xurmo", "marakuya", "anjir"]
# mevalar.append("nok")
# mevalar.append("uzum")
# mevalar.append("anor")
# del mevalar[0]
# del mevalar[1]
# del mevalar[2]
# mevalar.insert(-1)
# mevalar.insert(2, "tarvuz")
# mevalar.insert(0, "qovun")
# print(mevalar)


# son7 = list(352, 200111, 11))
# for s in son7:
#     print(f"{s}:11 = {s/11}")

# for s1 in son7:
#     if s1%11 == 0:
#         print(s1)


# ism = input("Ismingizni kiriting: ")
# yosh = int(input("Yoshingiz nechchida: "))
# sinf = input("Sinfingizni kiriting: ").lower()

# if yosh == 15 and sinf == "green":
#     print(f"{ism.title()} siz 207-xonaga kirishingiz mumkin!")
# else:
#     print("Siz 207-xonaga kirishingiz mumkin emas!")


# son = int(input("Son kiriting: "))
# if son % 2 == 0:
#     print(f"{son} juft")
# elif son == 0:
#     print(f"{son} juft ham toq ham emas")
# else:
#     print(f"{son} toq")


# son = int(input("Son kiriting: "))
# from math import sqrt
# if son > 0:
#     print({sqrt(son)})
# elif 0 > son:
#     print("Musbat son kiriting!")


# son1 = int(input("Sonni kiriting: "))
# son2 = int(input("Sonni kiriting: "))
# son3 = int(input("Sonni kiriting: "))
# son =  [son1, son2, son3]
# for s in son:
#     if s > 0:
#         print(s**3)
#     else:
        # print(s)

# son = int(input("Sonni kiriting: "))
# from math import sqrt
# if son % 2 == 0:
#     print(sqrt(son))
# else:
#     print(son**2)


# maktab = []
# son = int(input("Maktablar sonini kiriting: "))
# for m in range(son):
#     m = input("Maktab nomi va soni:")
#     maktab.append(m)
# print(maktab)

# maktab1 = maktab[:]
# print(maktab1)

# parol = "1234"
# p = input("Parol kiriting: ")
# if p == parol:
#         print("Tizimga xush kelibsiz!")


# password =[1111, 2222,3333,4444]
# login = ["AAA", "BBB", "CCC", "DDDD"]
# p = int(input("Parol kiriting: "))
# l = input("Login kiriting: ")
# if p not in password or l not in login:
#       password.append(p)
#       print(password)
# else:
#       print("Parol mavjud")






# ism = input("Ismingiz: ")
# baho = int(input("Bahoingizni kiriting: "))
# if baho == 0 or baho == 1:
#         print(f"{ism} {baho} juda yomon natija")
# elif baho == 2:
#         print(f"{ism} {baho} qoniqarsiz natija")
# elif baho == 3:
#         print(f"{ism} {baho} qoniqarli natija")
# elif baho == 4:
#         print(f"{ism} {baho} yaxshi natija")
# elif baho == 5:
#         print(f"{ism} {baho} a'lo natija")




# baho = int(input("Bahoingizni kiriting: "))
# if baho >= 0 or baho <= 40 :
#         print(f"{baho} sizning natijangiz juda yomon")
# elif baho >= 41 or baho <= 60 :
#         print(f"{baho} sizning natijangiz qoniqarli")
# elif baho >= 61 or baho <= 80 :
#         print(f"{baho} sizning natijangiz yaxshi")
# elif baho >= 81 or baho <= 99 :
#         print(f"{baho} sizning natijangiz a'lo")
# elif baho == 100 :
#         print(f"Tabriklaymiz siz {baho}% lik natija ko'rsatdingiz")
# elif baho < 0 or baho > 100:
#         print("Siz faqat 0-100 oralig'idagi sonlarni ")







# point = int(input("Bahoingizni kiriting: "))
# stage = int(input("Nechinchi o'rinni oldingiz: "))
# if baho >= 0 or baho <= 64 :
#         print(f"Imtihondan o'ta olmadingiz!")
# # elif baho >= 65 or baho <= 100 :
# #         print("Imtihonda o'tdingiz")
# elif baho >= 85 or baho <= 100 :
#         if stage == 4:
#                 print(f"Siz 25% grant olasiz")
#         elif stage == 3:
#                 print(f"Siz 50% grant olasiz")
#         elif stage == 2:
#                 print(f"Siz 75% grant olasiz")
#         elif stage == 1:
#                 print(f"Siz 100% grant olasiz")
# elif baho < 0 or baho > 100:
#         print("Siz faqat 0-100 oralig'idagi sonlarni ")








# password =[1111, 2222,3333,4444]
# login = ["AAA", "BBB", "CCC", "DDDD"]
# p = int(input("Parol kiriting: "))
# l = input("Login kiriting: ")
# if p not in password and l not in login:
#       password.append(p)
#       login.append(l)
#       print(f"Tizimga xush kelibsiz {l} sizning parolingiz {p}")
      
# else:
#       print("Bunday foydalanuvchi mavjud boshqa login kiriting!")



# krug = int(input("Necha aylana yugurish kerak: "))
# print("biz yugurishni boshladik")
# for k in range(krug):
#       print(f"{k+1}- aylana tugadi")
# print("biz yugurishni tugatdik")
# ruxsat = input("O'tiesak bo'ladimi?: ")
# if ruxsat == "ha":
#       print(" ruxsat")
# elif ruxsat == "yoq":
#       k1 = input("Yana qancha yuguraylik")

narh = 0
son = int(input("Necha kishisiz: "))
for s in range(son):
      yosh = int(input("Yoshingiz nechida: "))
      if yosh >= 0 and yosh <= 7:
            narh = narh + 0
      elif yosh >= 8 and yosh <= 18:
            narh = narh + 15.000
      elif yosh >= 19 and yosh < 70:
            narh = narh + 25.000
      elif yosh >= 70 and yosh <= 100:
            narh = narh + 0
print(f"Sizlar uchun kirish {narh} so'm turadi")
      

if yosh >= 0 and yosh <= 7:
            print("Sizga kirish bepul.")
elif yosh >= 8 and yosh <= 18:
            print("Sizga kirish 15.000.")
elif yosh >= 19 and yosh < 70:
            print("Sizga kirish 25.000.")
elif yosh >= 70 and yosh <= 100:
            print("Sizga kirish bepul.")
elif yosh < 0:
            print("Musbat son kiriting")
else:
            print("Xato son kiritdingiz")

sut_emizuvchilar = "AAAAAAAAAAA"   
qushlar = "arfdasdf"
information = input("Qanday ma'lumot olmoqchisiz: ")
if information == "sut emizuvchilar":
      print(sut_emizuvchilar)
elif information == "qushlar":
      print(qushlar)



