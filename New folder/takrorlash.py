"""---9B001---"""
""" 1 """
# ism = "Abdulahad"
# print(type(ism))

# familiya = "Ubaydullayev"
# print(type(familiya))

# yosh = 15
# print(type(yosh))

# kitoblar = ["Atomic Habits", "Anor"]
# print(type(kitoblar))

# kasb = "Game dev"
# print(type(kasb))

""" 2 """
# from math import sqrt
# print(round(sqrt(4364+1233)))

# """ 3 """
# son = int(input("Son kiriting: "))
# son2 = int(input("Son kiriting: "))

# print((son**2)/23)
# print((son2**2)/23)

""" 4 """
# son = int(input("Son kiriting: "))
# print(type(float(son)))
# print(type(int(son)))

""" 5 """
# kitoblar = []
# kitoblar.append(int(input("Kitob nomini kiriting: ")))
# kitoblar.append(int(input("Kitob nomini kiriting: ")))
# kitoblar.append(int(input("Kitob nomini kiriting: ")))
# kitoblar.append(int(input("Kitob nomini kiriting: ")))
# kitoblar.append(int(input("Kitob nomini kiriting: ")))
# print(kitoblar)

""" 6 """
# students = ["Ali", "Ma'ruf","Bahrom"]
# students.append("Abdulahad")
# students.insert(0, "Islom")
# students.insert(-1, "Abdulloh")

# students[0] = "Ikrom"
# print(students)

# students[0] = "Anvar"
# print(students)


"""---9B002---"""
""" 1 """
# import random
# son = int(input("Son kiriting: "))
# son2 = int(input("Son kiriting: "))

# print(random.randrange(son, son2))


""" 2 """
# kitoblar = []
# ism = input("Ism kiriting: ")
# son = int(input("Nechta kitob o'qigansiz: "))

# for s in range(son):
#     kitoblar.append(input("Kitob nomini kiriting: "))

# del kitoblar[0]

# kitoblar.insert(2, "Harry Potter")
# kitoblar.insert(3, "LOTRO")

# print(kitoblar)

""" 3 """
# fanlar = ["IT", "Algebra"]

# fanlar.append("Atomic Habits")
# fanlar.insert(0, "Dor ostidagi odam")

# fanlar[0] = "Savdogarlar ustozi"
# fanlar[1] = "Dunyoning ishlari"

# del fanlar[0]
# fanlar.remove("Dunyoning ishlari")
# fanlar.pop(-1)

# fanlar1 = fanlar.copy()

# fanlar.clear()

""" 4 """
# family = []
# son = int(input("Oila a'zolaringiz sonini kiriting: "))
# for s in range(son):
#     name = input("Ism kiriting: ")
#     family.append(name)
# print(family)

# """ 5 """
# cars = ["Mazda", "Mclaren", "Maserati", "Caddy", "Lambargini", "Honda", "PEUGEOT", "Nexia", "F1", "BMW"]

# print(len(cars))

# cars.sort()
# print(cars)

# cars.sort(reverse=True)
# print(cars)

# cars.reverse()
# print(cars)


"""---9B004---"""
""" 1 """
# sonlar = [45, -96, 0, 63.2, 1257, -6752.2, 42, 3, 542]
# sonlar.sort()
# print(sonlar)
# sonlar.sort(reverse=True)
# print(sonlar)
# sonlar.reverse()
# print(sonlar)

""" 2 """
# mevalar = ["olma", "o'rik", "shaftoli", "apelsin", "malina", "xurmo"]
# for m in mevalar:
#     if m == "olma" or m == "malina":
#         print(m.upper())
#     else:
#         print(m.capitalize())

""" 3 """
# books = {
#     "1":"Atomic Habits",
#     "2":"Alchimic"
# }

# books.update({"3":"Anor"})
# books["4"] = "Harry Potter"
# print(books)

# books.update({"3":"Iskanja"})
# books["4"] = "Dor ostidagi odam"
# print(books)

# del books["1"]
# books.pop("2")
# books.popitem()
# print(books)

# books.clear()


""" 4 """
# from math import sqrt
# son = list(range(102, 1020))
# for s in son:
#     if s < 1000:
#         print(s**3)
#     elif s > 1500:
#         print(s-4)
#     elif s % 7 == 0:
#         print(sqrt(s))


""" 5 """
# ball = int(input("Balingizni kiriting: "))
# orin = int(input("Nechinchi o'rinni oldingiz: "))

# if ball < 0 or ball > 100:
#     print("Noto'g'ri ma'lumot kiritdingiz")
# elif ball >= 0 and ball <= 64:
#     print("Siz imtihondan o'tmadingiz")
# elif ball >= 65 and ball <= 100:
#     print("Siz imtihonda o'tdingiz")
#     if orin == 1:
#         print("Siz 100% grant yutdingiz")
#     elif orin == 2:
#         print("Siz 75% grant yutdingiz")
#     elif orin == 3:
#         print("Siz 50% grant yutdingiz")
#     elif orin == 4:
#         print("Siz 25% grant yutdingiz")


"""---9B005---"""
""" 1 """
# dictionary = {
#     "pen":"ruchka",
#     "pencil":"qalam",
#     "juice":"sharbat",
#     "meal":"yegulik",
#     "foot":"oyoq"
# }
# print(dictionary.get(input("So'z kiriting: "), "Bunday so'z mavjud emas"))

""" 2 """

# menu = {
#     "osh":80000,
#     "sumboro":70000,
#     "somsa":60000,
#     "sho'rva":50000,
#     "mastava":40000,
#     "choy":30000,
#     "salat":20000,
#     "non":10000,
# }
# print(menu.keys())
# for key, value  in menu.items():
#     print(f"{key}-{value}")

""" 3 """
# ism = input("Ism kiriting: ")
# yosh = input("Yosh kiriting: ")
# if yosh >= 1 and yosh <= 6:
#     print("Siz bog'cha yoshidasiz")
# elif yosh >= 7 and yosh <= 17:
#     print("Siz maktab o'quxchisisiz")
# elif yosh >= 18 and yosh <= 30:
#     print("Siz talabasiz")
# elif yosh >= 31 and yosh <= 100:
#     print("Siz  mustaqil insonsiz")
# elif yosh < 0 and yosh > 100:
#     print("Noto'g'ri ma'lumot kiritdingiz")

""" 4 """
# classmates = {
#     "olimjanova":"sarvinoz",
#     "botirova":"hadicha",
#     "malikova":"naima",
#     "tohirova":"rahima",
#     "ubaydullayev":"abdulahad"
# }
# ism = input("Ism kiriting: ").lower()
# for key, value in classmates.items():
#     if ism == key:
#         print(f"{key.title()} {value.title()}")
#     elif ism == value:
#         print(f"{value.title()} {key.title()}")
# if ism not in classmates.keys() and ism not in classmates.values():
#     print(f"Bunday ma'lumot bizda mavjud emas")


"""---9G001---"""
""" 1 """
# x,y,z = "olma", "anor", "uzum"
# print(x)
# print(y)
# print(z)

""" 2 """
# print(f"Ahmadning \"yuvvosh\" mushugi meni ko'rsa, doim yugurib keladi")

""" 3 """
# print((93434+94903)-22344+7363)


""" 4 """
# ism = "Abdulahad"
# familiya = "Ubaydullayev"
# manzil = "Namangan"
# maktab = "BM"
# sinf = "9-Green"
# print(f"{ism} {familiya} {manzil} {maktab} {sinf}")

""" 5 """
# name = "Abdulahad"
# surname = "Ubaydullayev"
# full_name = f"{name} {surname}"
# print(full_name.lower())


""" 6 """
# gul = "   BoyCHeCHak "
# print(gul.lstrip())
# print(gul.strip())
# print(gul.capitalize())
# print(gul.upper())
# print(gul.lower())

"""---9G002---"""
""" 1 """
# son = int(input("Son kiriting: "))
# son2 = int(input("Son kiriting: "))
# print(son+son2)
# print(son-son2)
# print(son*son2)
# print(son/son2)
# print(son**2)
# print(son2**3)
# print((son+son2)/2)


""" 2 """
# yosh = int(input("Yoshingizni kiriting: "))
# yil = 2024-yosh
# print(yil)


""" 3 """
# matn1 = "bu mashq uchun berilgan matn"
# print(matn1.capitalize())

# matn2 = "aliSHeR nAvOIy"
# print(matn2.lower())

# matn3 = "boborahim mashrab"
# print(matn2.upper())

# matn4 = "aLIYEV vALI"
# print(matn4.title())

# matn5 = "SolijoNOv JoniBEK"
# print(matn5.lower())

# matn6 = "   Assalomu aleykum"
# print(matn6.lstrip())

# matn7 = "Assalomu aleykum   "
# print(matn7.rstrip())

# matn8 = "  Assalomu aleykum  "
# print(matn8.strip())

# matn9 = "assalomu aleykum"
# print(matn9.title())

# matn10 = "BOBORAHIM MASHRAB"
# print(matn10.lower())

""" 4 """
# from math import sqrt
# import random
# print(round(((231/4.7)*5)/4.7*5))
# print((((231/4.7)*5)/4.7*5))

# print(((3**4)+sqrt(35345))/8)

# print(random.randrange(20, 80))

# radius = int(input("Radius kiriting: "))
# pi = 3.14
# print(pi*radius**2)

# tomon = int(input("Tomon kiriting: "))
# print(f"Yuzi: {tomon*4}")
# print(f"Perimetri: {tomon**2}")