""" Class """
""" OOP - Object Oriented Programming """

class Car():
    """ Docstring """

    def __init__(self, company:str, model:str, color:str, price:int, max_speed:int, year:int, ):
        self.company = company
        self.model = model
        self.color =color
        self.price = price
        self.max_speed = max_speed
        self.year = year
        
    def get_info(self):
        """ Mashina haqida ma'lumot beruvchi funksiya """

        info = f"Mashina haqidagi ma'lumotlar: \nKompaniya: {self.company} \nModel: {self.model} \nRangi: {self.color} \
            \nNarxi: {self.price} \nEng yuqori tezligi: {self.max_speed} \nIshlab chiqarilgan yili: {self.year} \n"
        
        return info
    
    def get_company(self):
        comp = f"Kompaniya: {self.company} \nModel: {self.model}"

        return comp
    
car1 = Car("Tesla", "Model 3", "black", 30_000, 220, 2025)
car2 = Car("BMW", "M5", "black", 50_000, 290, 2025)
car3 = Car("Mersedes-Benz", "CLS 6", "black", 100_000, 300, 2022)


# print(car1.get_company())



class Student():
    """ """
    def __init__(self, name: str, surname: str, year: int, grade: int, *marks: int, friends:list):
        self.name = name
        self.surname = surname
        self.grade = grade
        self.marks = marks
        self.friends = friends
        self.year = year


    def get_info(self):
        """ Info """
        return f"Name: {self.name.title()} \nSurname: {self.surname.title()} \nGrade: {self.grade} \nMarks: {self.marks}"
    

    def get_full_name(self):
        """ """
        

    def get_age(self, now=2025):
        """ """
        return now-self.year

    def get_mid_mark(self): 
        """ """
        return f"Mid. mark: {sum(self.marks)/len(self.marks)}"
    

    def get_friends(self):
        """ """
        info = f"{self.name}ning do'stlari: "

        for name in self.friends:
            info += f" {name.title()}"

        return info
    

    def get_grade(self):
        """ """
        if self.grade < 6:
            self.grade+1
        else:
            return f"Siz uchun keyingi bosqich mavjud emas"
        return self.grade


amir = Student("Amir", "Abbasov", 2009, 4, [4,3,56,3,56,4,5],friends=["Abdulahad", "Ibrohim", "avazxon"] )

# print(amir.get_info())

# print(amir.mid_mark())

# print(amir.get_friends())

# print(amir.get_full_name())

# print(amir.get_grade())



class Book():
    """ """
    def __init__(self, name: str, author: str, year: int, publisher: str, price: int):
        self.name = name
        self.author = author
        self.year = year
        self.publisher = publisher
        self.price = price

    
    def __str__(self):
        return self.name
    
    def get_info(self):
        """ Umumiy ma'lumotlar """
        return f"Kitob nomi: {self.name} \nMuallifi: {self.author.title()} \nChiqqan yili: {self.year} \nNashriyotchi: {self.publisher} \nNarxi: {self.price}"
    

    def get_name(self):
        """ """
        return self.name

book1 = Book("Atomic Habits", "James Clear", 2000, "Asaxiy", 45_000)


class Library():
    """ """

    def __init__(self, name: str, adress: str):
        self.name = name
        self.adress = adress
        self.books = []
        self.book_amount = 0

    
    def __str__(self):
        return self.name
    
    
    def __repr__(self):
        return self.name

    def get_info(self):
        """ Umumiy ma'lumotlar """
        return f"Kutubxona nomi: {self.name.title()}  \nManzil: {self.adress.title()} \nKitoblar soni: {self.book_amount}\n"

    
    def add_book(self, *book):
        """ Kitob qoshish, kitoblar nomi va sonini qaytarish """

        for bok in book:
            self.books.append(bok)
            self.book_amount += 1
        return f"Kitoblar: {self.books} \nKitob soni: {self.book_amount}\n"

    def get_book(self):
        """ Kitob nomlarini chiqarish """
        info = f"{self.name.title()}dagi kitoblar: "

        for bok in self.books:
            if bok == self.books[-1]:
                info += f" {bok.title()}."
            else:
                info += f" {bok},"

        return info
    

    def delete_book(self, book):
        """ """
        if book in self.books:
            self.books.remove(book)
            self.book_amount -= 1
            return f"{book} kitobi kutubxonadan ochirildi"
        else:
            return f"{book} kitobi kutubxonada mavjud emas"


bookie = Library("Bookwarm", "Tashkent")


# print(bookie.add_book("Atomic Habits", "Harry Potter", "The Alchemist"))

# print(bookie.get_info())

# print(bookie.get_book())

# print(bookie)



""" Obyektning hususiyat va metodlarini korish """
""" dir() funksiyasi """

from pprint import pprint

pprint(dir(bookie))
pprint(dir(book1))



""" __dict__ metodi """
""" __dict__ metodi xususiyatlarini lug'at ko'rinishida qaytaradi """
print(bookie.__dict__)
print(book1.__dict__)