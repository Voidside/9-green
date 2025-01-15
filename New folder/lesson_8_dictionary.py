"""
Theme: Dictionary
"""

# taomlar = {
#     "ali":"osh",
#     "vali":"shashlik",
#     "hasan":"lag'mon",
#     "olim":"somsa"

# }

# """
# taom = {"ali":"osh"}
# nomi = {"key":"value"}
# """

# print(taomlar)
# print(type(taomlar))

# print(taomlar["ali"])
# print(f"Alining taomi {taomlar['ali']}")

# buyumlar = {
#     "ism":"Ali",
#     "yosh":12,
#     "student":True,
#     "oila":["ota", "ona", "aka"]
# }
# print(buyumlar)


# taomlar = {
#     "ali":"osh",
#     "vali":"shashlik",
#     "hasan":"lag'mon",
#     "olim":"somsa"
# }

# sorov = input("Nima ma'lumot kerak: ")
# if sorov in taomlar["ali"]:
#     print()


green_9 = {
    "olimjanova":"Sarvinoz",
    "botirova":"Hadicha",
    "malikova":"Naima",
    "tohirova":"Rahima"
}
# """ Element qo'shish """
green_9.update({"fazliddinova":"Mubina"})
# print(green_9)

green_9["mamadova"] = "Oydina"
# print(green_9)

# green_9.update({input("Familiya kiriting: "):input("Ism kiriting: ")})
# print(green_9)


# """ Elementni yangilash """
# green_9.update({"fazliddinova":"Muslima"})
# print(green_9)

# green_9["mamadova"] = "Masrura"
# print(green_9)

""" Elementni o'chirish """

# del green_9["botirova"]
# print(green_9)

# green_9.pop("fazliddinova") 
# print(green_9)

# green_9.popitem()
# print(green_9)

# """ Lug'atni o'chirish"""
# del green_9



""" 1 """
# akam = {
#     "ism":"Muzaffar",
#     "familiya":"Musayev",
#     "yosh":"25",
#     "kasb":"Kardiolog"
# }
# print(f"Akamning ismi sharifi {akam['ism']} {akam['familiya']}, uning yoshi {akam['yosh']} da, kasbi {akam['kasb']}.")


""" 2 """
# taomlar = {
#     "otam":"Lag'mon",
#     "onam":"Baliq",
#     "men":"Somsa",
#     "akam":"Sho'rva",
#     "singlim":"Tovuq"
# }
# print(f"Mening sevimli taomim {taomlar['men']}")
# print(f"Otamning sevimli taomi {taomlar['otam']}")
# print(f"Akamning sevimli taomi {taomlar['akam']}")



""" Lug'atni tozalash """
# green_9.clear()
# print(green_9)

""" Nusxa olish """
# math_students = green_9.copy()
# print(math_students)

# math_students1 = dict(green_9)
# print(math_students1)


""" .get() - metodi """
# print(green_9.get("abdulahad" , "Bunday ism yo'q"))
# print(green_9.get(input("key kiriting: "), "Bunday isim mavjud emas"))

""" 1 """
# english = {
#     "pen":"ruchka",
#     "pencil":"qalam",
#     "apple":"olma",
#     "mouse":"sichqon"
# }
# print(english.get(input("So'z kiriting: "), "Bunday so'z mavjud emas"))


""" 2 """
# dost = {
#     "ism":"",
#     "familiya":"",
#     "yosh":"",
#     "hobbi":"",
#     "sport":""
# }
# dost.update({"ism":input("Ism: ")})
# print(dost)


""" keys(), values(), items()"""


# green_9 = {
#     "olimjanova":"Sarvinoz",
#     "botirova":"Hadicha",
#     "malikova":"Naima",
#     "tohirova":"Rahima"
# }
# print(green_9.keys())
# print(green_9.values())

# print(f"9 Green sinfida quidagi o'quvchilar bor: ", end="")
# for familiya in green_9 .keys():
#     print(familiya, end="")

# print(f"9 Green sinfida quidagi o'quvchilar bor: ", end="")
# for ismalar in green_9 .keys():
#     print(ismalar, end="")

# print(green_9.items())
# for key, value in green_9.items():    
#     print(f"{key}-->{value}")



# eng_uz = {
#     "apple":"olma",
#     "bread":"non"
# }

# word = input("So'z kiriting: ").lower()
# for key, value in eng_uz.items():
#     if word == key:
#         print(f"{key}-->{value}")
#     elif word == value:
#         print(f"{value}-->{key}")

# if word not in eng_uz.keys() and word not in eng_uz.values():
#     print("Bu so'z mavjud emas")

""" 1 """
countries = {
    "canada":"Ottava",
    "uzbakistan":"Tashkent",
    "usa":"Vashinton"
}

# print(sorted(countries.keys()))
# print(sorted(countries.values()))



# place = input("Joy nomini kiriting: ").lower()
# for key, value in countries.items():
#     if place == key:
#         print(f"{key.title()}-->{value.title()}")
#     elif place == value:
#         print(f"{value.title()}-->{key.title()}")

# if place not in countries.keys() and place not in countries.values():
#     print("Bu so'z mavjud emas")





# green_9 = {
#     "olimjanova":"sarvinoz",
#     "botirova":"hadicha",
#     "malikova":"naima",
#     "tohirova":"rahima"
# }

# ism = input("Ism kiriting: ").lower()
# for key, value in green_9.items():
#     if ism == key:
#         print(f"{key.title()}-->{value.title()}")
#     elif ism == value:
#         print(f"{value.title()}-->{key.title()}")

# if ism not in green_9.keys() and ism not in green_9.values():
#     print("Bu o'quvchi mavjud emas")



# taomlar = {
#     "osh":10000,
#     "pepsi":15000,
#     "sumboro":20000,
#     "choy":5000,
#     "non":3000
# }
# print(taomlar.keys())

# print(f"{taomlar.keys()}-{taomlar.values()}")

# for key, value in taomlar.items():
#     print(f"{key}-{value}")