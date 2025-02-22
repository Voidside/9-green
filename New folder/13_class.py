""" Vorislik """

class Shaxs():
    """ """
    def __init__(self, name: str, surname: str, f_name: str, b_year: int, passport: str, millat: str):
        self.name = name
        self.surname = surname
        self.f_name = f_name        
        self.b_year = b_year
        self.passport = passport
        self.millat = millat


    def __str__(self):
        return f"{self.name.title()} {self.surname} {self.f_name}"



    def get_info(self):
        """ Umumiy ma'lumot """
        return f"{self.surname} {self.name} {self.f_name} {self.b_year} - yilda tug'ilgan. Millati {self.millat}. Passport raqami {self.passport}"


    def get_age(self, h_yil):
        """ Shaxsning yoshi """
        return h_yil-self.b_year


    def get_passport(self):
        """ Passporti """
        return self.passport


    def get_millat(self):
        """ Millati """
        return self.millat

# shaxs1 = Shaxs()

class Student(Shaxs):
        """ """
        def __init__(self, name: str, surname: str, f_name: str, b_year: int, passport: str, millat: str, maktab, sinf, baholar):
            """ Talabaning xususiyatlari """
            super().__init__(name, surname, f_name, b_year, passport, millat)
            self.maktab = maktab
            self.sinf = sinf
            self.baholar = baholar


        def get_maktab(self):
            """ Maktabni qaytaruvchi """
            return self.maktab


        def get_sinf(self):
            """ Sinf qaytaruvchi """
            return self.sinf


        def set_sinf(self):
            """ Sinfni o'zgartiruvchi """
            if self.sinf < 11:
                return self.sinf+1
            else:
                return f"Siz bitiruvchisiz"


        def get_baholar(self):
            """ Umumiy ball """
            return sum(self.baholar)


        def get_age(self, h_yil):
            return f"{self.name.title()} yoshi {h_yil-self.b_year} da"


        def get_passport(self):
            return f"{self.name.title()} ning passport raqami: {self.passport}"



student1 = Student("Abdulahad", "Ubaydullayev", "Iskandar", 2009, "AH1441224", "O'zbek", "BM", 9, [56,65,43,65])

# print(student1.get_age(2025))

# print(student1.get_passport())

# print(student1.get_info())

# print(student1.set_sinf())




class Technic():
    def __init__(self, company: str, OS: str, year: int):
        self.company = company
        self.OS = OS
        self.year = year


    def get_info(self):
        """ Umumiy ma'lumot """
        return f"Kompaniya: {self.company} \nOS: {self.OS} \nYil: {self.year}"



all = Technic("Apple", "IOS", 2024)

class Laptop(Technic):
    def __init__(self, company: str, OS: str, year: int, model: str, price: int, screen: str):
        super().__init__(company, OS, year)
        self.model = model
        self.price = price
        self.screen = screen


    def get_info(self):
        """ Umumiy ma'lumot """
        return f"Kompaniya: {self.company} \nOS: {self.OS} \nYil: {self.year} \nModel: {self.model} \nNarxi: {self.price} \nEkran: {self.screen}"




note = Laptop("Apple", "IOSX", 2025, "MacBook Air  M1", 1400, "4K")

print(note.get_info())


class Phone(Technic):
    def __init__(self, company: str, OS: str, year: int, model: str, price: int, camera: str):
        super().__init__(company, OS, year)
        self.model = model
        self.price = price
        self.camera = camera

        
