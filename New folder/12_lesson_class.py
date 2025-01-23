""" Class """
""" OOP - Object Oriented Programming """

# class Car():
#     """ Docstring """

#     def __init__(self, company:str, model:str, color:str, price:int, max_speed:int, year:int, ):
#         self.company = company
#         self.model = model
#         self.color =color
#         self.price = price
#         self.max_speed = max_speed
#         self.year = year
        
#     def get_info(self):
#         """ Mashina haqida ma'lumot beruvchi funksiya """

#         info = f"Mashina haqidagi ma'lumotlar: \nKompaniya: {self.company} \nModel: {self.model} \nRangi: {self.color} \
#             \nNarxi: {self.price} \nEng yuqori tezligi: {self.max_speed} \nIshlab chiqarilgan yili: {self.year} \n"
        
#         # return info
    
#     def get_company(self):
#         comp = f"Kompaniya: {self.company} \nModel: {self.model}"

#         return comp
    
# car1 = Car("Tesla", "Model 3", "black", 30_000, 220, 2025)
# car2 = Car("BMW", "M5", "black", 50_000, 290, 2025)
# car3 = Car("Mersedes-Benz", "CLS 6", "black", 100_000, 300, 2022)


# print(car1.get_company())



class Student():
    """ """
    def __init__(self, name: str, surname: str, grade: int, *marks: int):
        self.name = name
        self.surname = surname
        self.grade = grade
        self.marks = marks


    def get_info(self):
        """ Info """
        return f"Name: {self.name.title()} \nSurname: {self.surname.title()} \nGrade: {self.grade} \nMarks: {self.marks}"
    
    def mid_mark(self): 
        """ """
        return f"Mid. mark: {sum(self.marks)/len(self.marks)}"
    

ali = Student("Amir", "Abbasov", 2, 4,3,56,3,56,4,5,)

print(ali.get_info())
print(ali.mid_mark())