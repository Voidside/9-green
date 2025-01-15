""" Theme: Lists """


""" Index 
mevalar = ["olma", "gilos", "o'rik", "olcha"]
              1        2        3       4
             -4       -3       -2      -1 
"""


# mevalar1 = ["olma", "gilos", "o'rik", "olcha"]
# mevalar2 = ("olma", "gilos", "o'rik", "olcha")
# mevalar3 = {"olma", "gilos", "o'rik", "olcha"}
# print(type(mevalar1))
# print(type(mevalar2))
# print(type(mevalar3))

# mevalar = ["olma", "gilos", "o'rik", "olcha"]
# print(mevalar[0])
# print(mevalar[2])
# print(mevalar[3])

# print(f"mening sevimli mevam {mevalar[3]}")

# """list turlari"""
# ismlar = ["olma", "gilos", "o'rik", "olcha"]
# son = [1,-9,45]
# darslar = ["Python", "Django",3,10]
# bosh_royhat = []

# """ ro'yhat qiymatini o'zgartirish"""
# mevalar = ["olma", "gilos", "o'rik", "olcha"]
# mevalar[0] = "salamander"
# print(mevalar)

# son = [1,2,3,4]
# print(son[0] * son[2])

"""  Vazifalar  """
# ismlar degan ro'yxat yarating va kamida 5 ta yaqin do'stingizning ismini kiriting. 
#    Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 

# 2) sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang(musbat, manfiy, butun, o'nlik). 
#     Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring.

# Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa o'chirib tashlaymiz.

# 01
# ismlar = ["Amir", "Ibrohim", "Avaz", "Barkamol", "Bekzod"]
# print(f"Salom {ismlar[0]}")
# print(f"Salom {ismlar[1]}")
# print(f"Salom {ismlar[2]}")
# print(f"Salom {ismlar[3]}")
# print(f"Salom {ismlar[4]}")

# # 02
# son = [34,-5,76.8,12]
# print(son[2]*son[0])
# print(son[1]/son[3])

# son[0] = 455
# print(son)


""" .append oxiridan qo'shish"""
# students = ["ALi","Ma'ruf", "Bahrom" ]
# students.append("Umarbek")
# print(students)

# """ input bilan qo'shish"""
# students.append(input("Ism kiriting: "))
# print(students)

""" .insert """
# students.insert(2, "Amir")
# print(students)

# students.insert(int(input("Son kiriting: ")) , input("Ism kiriting:"))
# print(students)


# friends = []
# friends.append(input("Ism kiriting: "))
# friends.append(input("Ism kiriting: "))
# friends.append(input("Ism kiriting: "))
# print(friends)

# friends.insert(int(input("Sonni kiriting: ")),input("Ism kiriting: "))
# friends.insert(int(input("Sonni kiriting: ")),input("Ism kiriting: "))
# friends.insert(int(input("Sonni kiriting: ")),input("Ism kiriting: "))
# print(friends)

""" extend() --> 1 chi ro'hatni 2 chisiga qo'shadi"""
# fruts = ["apple", "cherry", "grape"]
# tropic_fruts = ["pineapple", "orange" "papaya"]
# fruts.extend(tropic_fruts)
# print(tropic_fruts)
# print(fruts)


students = ["ALi","Ma'ruf", "Bahrom" ]
""" del royhatdan elemantni indexi bo'yicha o'chiradi"""
""" del --> ro'yhatni butunlay o'chirib tashlashi mm"""
# print(students)

# del students[0]
# print(students)

""" .remove() --> elementni qiymati bo'yicha o'chiradi"""
# students.remove("Ali")
# print(students)

""" .pop --> elementni sug'urib oladi"""
""" agar index berilmasa avtomatik oxirgisini o'chiradi"""
# students.pop(0)
# print(students)

# 01
# aktyorlar = ["Uill Smit", "Jony Depp", "John Whick"]
# honandalar = ["Miyagi", "Imagine Dragons", "Eminem"]
# del aktyorlar[1]
# del aktyorlar[0]
# del honandalar[0]
# del honandalar[1]
# aktyorlar.append("Tom Holland")
# aktyorlar.append("Bred Pitt")
# aktyorlar.append("Robert Dauni")
# honandalar.append("Den")
# honandalar.append("John")
# honandalar.append("Bred")
# insonlar = []
# insonlar.extend(aktyorlar)
# insonlar.extend(honandalar)
# print(insonlar)



""" len() ro'yhat uzunligi """
# family = ["father","mother", "me"]
# print(f"Bizning oilada {len(family)} kishi yashaydi")
# print(f"They are {family[0]}, {family[1]}, {family[2]}")


""" list() --> bo'sh ro'yhat yaratish u-n kk"""
# country = list()
# davlatlar = []
# print(country)
# print(davlatlar)

""" Ro'yhat elementlarini tozalash clear()"""
# family = ["father","mother", "me"]
# print(family)
# family.clear()
# print(family)

""" range() --> somli oraliq shakllantirish """
# sonlar = list(range(-10,11))
# sonlar2 = list(range(0,101,5))
# print(sonlar)
# print(sonlar2)

""" Ro'yhatdan nusxa olish """
# son = list(range(100,300))
# son2 = son[10:20]
# # son2 = son[:]
# print(son)
# print(son2)

# taomlar = ["Osh", "Sho'rva", "mastava", "So'msa", "Club sandwich"]
# nonushta = []
# nonushta = taomlar[0:2]
# nonushta.append("Tuxum")
# nonushta.append("Coffee")
# print(nonushta)
# del nonushta[0]
# del nonushta[0]
# # print(taomlar)
# print(nonushta)


"""
 8)
     Taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting.
    -nonushta degan yangi ro'yxatga taomlardan nusxa oling;
    -yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing;
    -ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring;
"""


""" sort() - ro'yhatni alifbo bo'yicha tartiblaydi """
# name = ["Olim", "Avaz", "Sarvar", "Ali","Murod"]
# print(name)
# name.sort()
# name.sort(reverse=True)
# print(name)

# """ sorted() - ro'yhatni bir marta tartiblaydi"""
# print(name)
# print(sorted(name))
# print(sorted(name, reverse=True))

# """ reverse() - royhatni  teskari ogirib beradi"""
# country = ["Uzbekiston", "Albaniya", "Rossiya", "Afrika"]
# print(country)
# country.reverse()
# print(country)

# """ min() , max() , sum()"""
# number = list(range(1,21))
# print(min(number)) #eng kichik qiymat
# print(max(number)) #eng katta qiymat
# print(sum(number)) #yig'indisi

# 01
davlatlar = ["USA", "Uzbakistan", "Russia", "Canada", "Filipin", "UK", "Portugaliya", "Turkiya", "Somali", "Belgiya"]
