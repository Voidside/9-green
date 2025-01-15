
""" 9G001 """

"""1-	Mashq | 5 Ball
Bir vaqtni o’zida 4 ta o’zgaruvchi yarating(Bu ishni bir qatorda bajarish zarur !). Hamda o’zgaruvchilarni konsulga chiqaring.
"""
""" 1 """
x, y, z, a = "kitob", "daftar", "pilot", "scar"

print(x, y, z, a)


"""
2-	Mashq | 5 Ball |  Ushbu matinni konsulga chiqaring:
“Ahmadning “yuvvosh” mushugi meni ko’rsa, doim yugurib keladi.”
"""
""" 2 """
print(f"Ahmadning \"yuvvosh\" mushugi meni ko'rda, doim yugurib keladi")



"""
3-	Mashq | 5 Ball | Misolni pyhtonda bajaring:
93434 ga 94903 ni qoshing, hosil bo’lgan natijadaan 22344 ni ayring va unga 7363 ni qo’shing
"""
""" 3 """
print((93434+94903)-22344+7363)



"""
4-	Mashq | 10 Ball
Ism, yosh, manzil, maktab, sinf deb nomlangan o’zgaruvchilar yarating va ularni konsulga f”” yordamida chiqaring.
"""
""" 4 """
ism = "Abdulahad"
yosh = "15"
manzil = "Namangan"
maktab = "BM"
sinf = "9-Green"

print(f"{ism}, {yosh}, {manzil}, {maktab}, {sinf}")




"""
5-	Mashq | 10 Ball
Name, surname deb nomlangan o’zgaruvchilar yarating va ularni yangi full_name deb nomlangan o’zgaruvida jamlang. 
Hamda full_name deb nomlangan o’zgaruvchining qiymatini ba’zi metodlar ishlatgan holda barcha hariflarini kichhik qilib konsulga chiqaring.
"""
""" 4 """
name = "Abdulahad"
surname = "Ubaydullayev"
full_name = f"{name} {surname}"
print(full_name.upper())



"""
6-	Mashq | 15 Ball
Quidagi o’zgaruvchini   --->
1)	Chap tomonidagi bo’shliqni olib tashlab;
2)	Har ikki tomonidagi bo’shliqni olib tashlab;
3)	Birinchi harifni katta qilib;
4)	Barcha hariflarini katta qilib;
5)	Barcha hariflarini kichik qilib  konsulga chiqaring.
"""
""" 6 """
gul = "	   BoyCHeCHak	   "

print(gul.lstrip())
print(gul.strip())
print(gul.capitalize())
print(gul.upper())
print(gul.lower())

