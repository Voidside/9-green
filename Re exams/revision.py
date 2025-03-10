""" 9G016 """
""" 1 """
def my_ranje(start, stop, step):
    """ Sonli oraliq """
     
    result = [start]

    for son in result:
        son =+ 1



""" 2 """
class Inson():
    """ """
    def __init__(self, ism: str, familiya: str, yosh: int, t_yil: int, pho_num: int, address: str, prof: str):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
        self.t_yil = t_yil
        self.pho_num = pho_num
        self.address = address
        self.prof = prof



    def ism1(self):
        """ Ism """
        return f"{self.ism.title()}"
    


    def familiya1(self):
        """ Familiya """
        return f"{self.familiya.title()}"
    


    def yosh1(self):
        """ Yosh """
        return f"{self.yosh}"
    


    def pho_num1(self):
        """ Phone number """
        return f"{self.pho_num}"
    


    def address1(self):
        """ Address """
        return f"{self.address}"
    


    def get_info(self):
        """ All info """
        return f"Ism: {self.ism.title()}\n Familiya: {self.familiya.title()}\n Yosh: {self.yosh}\n Tel. raqam: {self.pho_num}\n Manzil: {self.address}"
    

