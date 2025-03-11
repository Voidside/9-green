""" 9G016 """
""" 1 """
# def my_ranje(start, stop, step):
#     """ Sonli oraliq """
     
#     result = [start]

#     for son in result:
#         son =+ 1



""" 2 """
# class Homosapiens():
#     """ """
#     def __init__(self, name: str, surname: str, age: int, b_year: int, pho_num: int, address: str, prof: str):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.b_year = b_year
#         self.pho_num = pho_num
#         self.address = address
#         self.prof = prof



#     def name1(self):
#         """ Name """
#         return f"{self.name.title()}"
    


#     def surname1(self):
#         """ Surname """
#         return f"{self.surname.title()}"
    


#     def age1(self):
#         """ Age """
#         return f"{self.age}"
    


#     def pho_num1(self):
#         """ Phone number """
#         return f"{self.pho_num}"
    


#     def address1(self):
#         """ Address """
#         return f"{self.address}"
    


#     def get_info(self):
#         """ All info """
#         return f"Name: {self.name.title()} \nSurname: {self.surname.title()} \nAge: {self.age} \nBirth year: {self.b_year} \nPhone number: {self.pho_num} \nManzil: {self.address}"
    
# object1 = Homosapiens("Abdulahad", "Ubaydullayev", 15, 2009, 998771170073, "Namangan", "IT (Junior)")

# print(object1.name1())
# print(object1.surname1())
# print(object1.age1())
# print(object1.pho_num1())
# print(object1.get_info())




""" Student """

class Student(): 
    """ """
    def __init__(self, name: str, surname: str, fath_name: str, school: str, grade: int, address: str, marks: list, classes:list, friends: list):
        self.name = name
        self.surname = surname
        self.fath_name = fath_name
        self.school = school
        self.grade = grade
        self.address = address
        self.marks = marks
        self.classes = classes
        self.friends = friends



    def get_overall_ball(self):
        """ """
        return sum(self.marks)
    


    def get_mid_ball(self):
        """ """
        return sum(self.marks)/len(self.marks)
    



object1 = Student("Abdulahad", "Ubaydullayev", "Iskandar", "BM", 9, "Namangan", [32,55,12,54,64,33], ["de", "are", "sde"], ["f","r","i"])