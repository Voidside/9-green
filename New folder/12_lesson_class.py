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
        
        # return info
    
    def get_company(self):
        comp = f"Kompaniya: {self.company} \nModel: {self.model}"

        return comp
    
car1 = Car("Tesla", "Model 3", "black", 30_000, 220, 2025)
car2 = Car("BMW", "M5", "black", 50_000, 290, 2025)
car3 = Car("Mersedes-Benz", "CLS 6", "black", 100_000, 300, 2022)


print(car1.get_company())