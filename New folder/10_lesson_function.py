# def yosh_top():
#     ism = input("Ismingizni kiriting: ")

#     yosh = int(input(f"{ism.title()} tug'ilgan yilingiz: "))

    # print(f"{ism.title()} siz {yosh} dasiz")


# def salom_ber():
#     print("Assalomu aleykum")



def max():
    num1 = int(input("Birinchi sonni kiriting: "))
    num2 = int(input("Ikinchi sonni kiriting: "))
    if num1 > num2:
        print(f"{num1}")


# max()




""" Docstring """

# def yosh_top(t_yil):
#     """ Tug'ilgan yil olib yoshni chiqaruvchi funksiya

#     t_yil --> int
#     """
#     print(f"Siz  {2024-t_yil} yosdasiz")

# yosh_top(2012)

# x = int(input("Tug'ilgan yilingiz: "))
# yosh_top(x)






# print(print.__doc__)

""" Parametrni key_word bilan berish """
# def yosh_top(t_yil):
#     """ Tug'ilgan yil olib yoshni chiqaruvchi funksiya

#     t_yil --> int
#     """
#     print(f"Siz  {2024-t_yil} yosdasiz")

# yosh_top(t_yil=2012)


""" Standart qiymat"""
# def yosh_top(t_yil=2000):
#     """ Tug'ilgan yil olib yoshni chiqaruvchi funksiya

#     t_yil --> int
#     """
#     print(f"Siz  {2024-t_yil} yosdasiz")

# yosh_top(t_yil=2012)




""" 9B010 """
""" 1 """
# print(len.__doc__)
# print(max.__doc__)
# print(sum.__doc__)
# print(range.__doc__)
# print(list.__doc__)


""" 2 """
def baholovchi(baho):
    if baho < 0 or baho > 100:
        print("Noto'g'ri ma'lumot kiritildi!")
    elif baho >= 0 and baho <= 50:
        print(f"Siz {baho} ball oldingiz, bu qoniqarsiz")
    elif baho >= 51 and baho <= 70:
        print(f"Siz {baho} ball oldingiz, bu qoniqarli")
    elif baho >= 71 and baho <= 90:
        print(f"Siz {baho} ball oldingiz, bu yaxshi")
    elif baho >= 91 and baho <= 100:
        print(f"Siz {baho} ball oldingiz, bu a'lo")

# baholovchi(66)


""" 3 """
def p_s(a,b):
    """ perimetr va yuz """
    print(f"Tomonlari {a} va {b} ga teng bolgan to'g'ri to'rtburchakning perimetri {2*(a+b)} ga yuzi {a*b}")

# p_s(5,6)

""" 4 """
sonlar = [22, 444, 5556, 6566, 6,6]

def tartiblovchi(sonlar1):
    sonlar1.sort()
    print(sonlar1)

# tartiblovchi(sonlar)




""" Funksiyadan qiymat qaytarish """
# def yosh_top(t_yil: int, ism: str, oila: list) -> int: # t_yil - parametr
def yosh_top(t_yil: int) -> int:
    """ Tug'ilgan yil olib yoshni chiqaruvchi funksiya

    t_yil --> int
    """
    yosh = 2024-t_yil
    return yosh # return --> qaytarish

# malikaning_yoshi = yosh_top(2009)
# print(f"Malikaning {malikaning_yoshi} yoshda")


def person(name: str, surname:str, age: int, email: str ):
    """ """
    person = {
        "name": name,
        "surname":surname,
        "age":age,
        "email":email
    }

    return person

# odam  = person("Marcuss", "Person", 20, "marcusspersony@gmail.com")

# print(odam)



def family_list(father: str, mother: str, brother:str, sister:str):
    """ Family list """
    family = []
    family.append(father)
    family.append(mother)
    family.append(brother)
    family.append(sister)
    return family

# family1 = family_list("John", "Lily", "Ronald", "Jinny")
# print(family1.title())



def info(name: str, age: int, sinf="9 Green") -> str:
    """ Ma'lumotlar """
    return f"{name.title()} your age {age}, your class {sinf}"

# student = info(sinf="9 Green", age=15, name="Abboss")



""" 1 """
def juft_sonlar(son: int) -> list:
        """ """
        return list(range(0, son, 2))

# son1 = juft_sonlar(133)
# print(son1)



""" 2 """
def aylana(radius: int)-> dict:
    """ """
    pi = 3.14
    aylana1 = {
        "radius":radius,
        "diametr":radius*2,
        "perimetri":radius*pi*2,
        "yuzi":pi*radius**2
    }
    return aylana1


# geomet = aylana(6)
# print(geomet)




""" 3 """
def tub_sonlar(y):
    tub_sonlar = []

    for num in range(1, y + 1):
        if num > 1:
            tub = True
            for i in range(2, num):
                if num % i == 0:
                    tub == False
                    break
            if tub:
                tub_sonlar.append(num)
    return tub_sonlar

# y1 = int(input("Son kiriting: "))
# natija = tub_sonlar(y1)

# print(natija)





def age_ID(ism: str, b_year: int, p_year= 2024):
    """ """
    natija = f"{ism.title()} siz {p_year-b_year} yoshdasiz"
    return natija

# amir = age_ID("Amir", 2000)
# print(amir)



def ranje(start: int, stop:int):
    """  """
    sond = [start]

    for start in  sond:
        if start < stop - 1:
            sond.append(start + 1)


    return sond

# natija = ranje(12,5577777)
# print(natija)



def sqrtt(son: int, daraja):
    son1 = son**0.5
    return son1


# natija = sqrtt(9)
# print(natija)




def sqrtt(son: int, daraja):
    """"""

    son1 = son**daraja
    return son1

# natija = sqrtt(27, 3)
# print(natija)



def unli_undosh(harf:str):
    """"""
    unli = ["a", "e", "u", "i", "o", "o'"]
    if harf in unli:
        return f"{harf} harfi unli"
    else:
        return f"{harf} harfi undosh"
    


# natija = unli_undosh("b")
# print(natija)





def unli_undosh(*harf:str):
    """"""
    unli1= []
    undosh = []
    unli = ["a", "e", "u", "i", "o", "o'"]
    for har in harf:
        if har in unli:
            unli1.append(har)
        else:
            undosh.append(har)
    return f"Unlilar: {unli1} \nUndoshlar: {undosh}"


# natija = unli_undosh("b", "a", "p", "s")
# print(natija)


def lenn(*son):
    len1 = 0
    for son in son:
        len1 = len1 + 1
    return len1

# print(lenn(345,66,7,-66,5645-665))


def summ(*sonlar):
    summa = 0
    for son in sonlar:
        summa = summa + son
    return summa

# print(summ(345,66,7,-66,5645-665))



def unli_undosh(matn:str):
    """"""
    unli1= []
    undosh1 = []
    unli = ["a", "e", "u", "i", "o", "o'"]
    undosh = ["b", "y", "k", "l", "m", "n", "ng", "p", "r", "s", "t", "f", "x", "s", "ch", "sh", "q", "gʻ", "h"]
    for har in matn:
        if har in unli:
            unli1.append(har)
        elif har in undosh:
            undosh1.append(har)
    return f"Unlilar: {unli1} \nUndoshlar: {undosh1}"


# natija = unli_undosh("bhgfjgfjbfdfystyjsadtgzhbt fxt muyjtshtarewytriuvoYTLKHANSVABFB V TWGHIKGHY;GYU;GVJN  hjj")
# print(natija)


def mid_arif(*sonlar: int):
    s = 0
    for son in sonlar:
        s = s + son
    return s/lenn(sonlar)

# print(mid_arif(4,4,4,4))

# import math

# ekub = math.gcd(100)
# print(ekub)




# from random import randrange

# r = randrange(1,10)

# son = int(input("Son kiriting: "))
# if son == r:
#     print("To'g'ri topdingiz!")
# else:
#     print(f"PC {r} sonini oylagan edi")