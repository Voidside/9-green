

"""
1-mashq | 5 Ball
Quidagicha sonli ro’yhatlar yarating:
200 dan 400 gacha toq sonli;
301 dan 500 gacha juft sonli;
10 dan 600 gacha 25 ga bo’linadigan sonlardan iborat;
"""
sonlar = list(range(201, 400, 2))
# print(sonlar)

sonlar = list(range(302, 500, 2))
# print(sonlar)

sonlar = list(range(25, 600, 25))
# print(sonlar)


"""
2-mashq | 10 Ball
O’zingizga ma’lum 7 ta davlat nomini qo’shgan holatda davlatlar deb nomlangan ro’yhat tuzing. 
	3 ta elementni 3 hil usulda o’chirib tashlang.  Yangi 2 ta davlat nomini 2 xil usulda qo’shing.
"""

davlatlar = ['Azerbaijan', 'Qazaqstan', 'Turkmenistan', 'Yunanistan', 'Qirg’izstan', 'Uzbekistan', 'Kazakhstan']

del davlatlar[0]
# print(davlatlar)

davlatlar.pop(-1)
# print(davlatlar)

davlatlar.remove("Turkmenistan")
# print(davlatlar)

davlatlar.append("Chili")
# print(davlatlar)

davlatlar.insert(2, "Tajikistan")
# print(davlatlar)



"""
3-mashq | 15 Ball
Names deb nomlangan ro’yhat yararing unda o’zingiz bilgan 3, 4 ta ism bo’lsin. Keyin esa 
foydalanuvchidan uning ismini ham so’rang agar uning ismi sizning ro’yhatingizda bo’lsa, “Kechirasiz sizning ismingiz mening ro’yhatimda bor ekan” degan habarni agar ro’yhatda bo’lmasa “Guruhga hush kelibsiz” degan habarni konsulga chiqaring.
"""

# ism = input("Ism kiriting: ")
# names = ["John", "Jane", "Michael"]

# if ism in names:
#     print("Kechirasiz sizning ismingiz mening ro'yhatimda bor ekan")
# else:
#     names.append(ism)
    


"""
4-mashq | 20 Ball
O’quv qurollari nomlaridan iborat ro’yhat tuzing. Foydalanuvchiga ro’yhatdagi mahsulotlar 
nomini ko’rsating va undan nechta mahsulot va nimalar olmoqchiligini so’rang. Keyin esa foydalanuvchi olmoqchi bo’lgan ,
do’koningizda bor va yo’q mahsulotlarni ko’rsatib o’ting.
"""
konselyar = ["qalam", "ruchka", "daftar", "chizg'ich"]
print(f"Assalomu aleykum, do'konimizga xush kelibsiz! \nBizning do'konda {len(konselyar)} ta mahsulotlar bor:", end=" ")

for mahsulot in konselyar:
    if mahsulot == konselyar[0]:
        print(f"{mahsulot.title()}", end=", ")
    elif mahsulot == konselyar[-1]:
        print(f"{mahsulot}", end=".")
    else:
        print(f"{mahsulot}", end=", ")
        
bor = []
yoq = []

savol = int(input("\nNechta narsa olmoqchisiz: "))

for s in range(savol):
    mahsulot = input(f"{s+1} chi mahsulotni kiriting: ").lower()
    if mahsulot in konselyar:
        bor.append(mahsulot)
    else:
        yoq.append(mahsulot)
        
print(f"Bizda bor mahsulotlar: ", end="")
for mahsulot in bor:
    if mahsulot == bor[0]:
        print(f"{mahsulot.title()}", end=", ")
    elif mahsulot == bor[-1]:
        print(f"{mahsulot}", end=".")
    else:
        print(f"{mahsulot}", end=", ")
        


print(f"\nBizda yoq mahsulotlar: ", end="")
for mahsulot in yoq:
    if mahsulot == yoq[0]:
        print(f"{mahsulot.title()}", end=", ")
    elif mahsulot == yoq[-1]:
        print(f"{mahsulot}", end=".")
    else:
        print(f"{mahsulot}", end=", ")