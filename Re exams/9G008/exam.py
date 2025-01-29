
"""
4-mashq | 10 Ball
Foydalanuvchidan uning yoshini so’rang. 
Agar u maktab yoshida bo’lsa(7-18) undan nechanchi sinfda o’qishini so’rang. 
Agar foydalanuvchi 0 dan kichik va 101 dan katta son kiritisa,unga “Noto’g’ri son kiritdingiz !” degan habar chiqsin.
Qolgan barcha yosh uchun, unga hech qanday javob qaytarmang. 
"""
""" 
5-mashq | 15 Ball
Davlatlar va ularning poytaxtlari lug'atini tuzing. Foydalanuvchidan istalgan davlatni kiritishni so'rang agar foydalanuvchi davlar kiritsa uning poytaxini, poytaxt kiritsa uning davlatini konsulga chiqaring. 
Agar foydalanuvchi lug'atda yo'q davlatni kiritsa,  "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring
"""

"""
1-mashq | 5 Ball
Quidagi o’zgaruvchini ---> 	name = “ AnToNy  ” ; 
•	o’ng tomonidagi bo’shliqni olib tashlab;
•	chap tomonidagi bo’shliqni olib tashlab;
•	barcha hariflarini kichik qilib;
•	barcha hariflarini katta qilib;
•	birinchi harifni katta qilib konsulga chiqaring.
"""
# name = " AnToNy  "

# print(name.rstrip())
# print(name.lstrip())
# print(name.lower())
# print(name.upper())
# print(name.title())


"""
2-mashq | 10 Ball
Ismlar deb nomlangan o’zgaruvchi yarating.
Unda o’zingiz  bilgan 6 ta ism bo’lsin.
Avval ro’yhatning uzunligini o’lchang.
O’sish va kamayish tartibida tartiblang.
“remove” metodi yordamida 1 ta elementni o’chirib tashlang.
“insert” metodi yordamida 2 ta element qo’shing.
"""

# names = ["John", "Jane", "Bob", "Alice", "Emily", "David"]

# print(len(names))

# names.sort()
# names.sort(reverse=True)
# print(names)

# names.remove("Jane")
# print(names)

# names.insert(1, "Mary")
# names.insert(2, "Dan")

# print(names)


"""
3-mashq | 10 Ball
100 dan 700 gacha  toq sonli ro’yhat yarating. Va ro’yhatdagi:
•	200 gacha bo’lgan sonlarning kvadratini toping;
•	300 dan 400 gacha bo’lgan sonlarning ildizni toping;
•	500 dan 700 gacha bo’lgan sonlarning 4-darajasini toping.
"""
sonlar = list(range(101, 700, 2))

for s in sonlar:
    if s < 200:
        print(s**2)
    elif s >= 300 and s <= 400: