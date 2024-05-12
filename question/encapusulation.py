class student :
    
    school = "chsp"
    
    
    def __init__(self) -> None:
        self.__number = None
    
    def get_number(self):
        return self.__number
    
    def set_number(self,a):
        self.__number =a
    
    @classmethod
    def check(self):
        return self.school
    
    
    @staticmethod
    def add(x,y):
        return x+y
        
        
p1 = student()
print(p1.__number)
p1.set_number(34)
print(p1.get_number())
print(student.check())