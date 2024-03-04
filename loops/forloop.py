#basic syntax for loop 
class loop():
    def print_i(self):
        fruits = ["apple", "peach ", "pear"]
        for fruit in fruits:
            print(fruit)
            print(fruit + " pie")
        


a = loop()
a.print_i()





#  exercise: calculate a avergage height of student in list
class avg_height():
    
    def __init__(self) -> None:
        student_height = input("Input a list of student height ").split()
        for n in range(0,len(student_height)):
            student_height[n] = int(student_height[n])
        print(student_height)

        total_height = sum(student_height)
        number_of_student = len(student_height)
        average_height = round(total_height/number_of_student)
        print(f"average heigth of student is {average_height}")
    
a = avg_height()



##########random password generater using loops ###########
import random
class generator:
    
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def align_password(self):
        print("Welcome to the PyPassword Generator!")
        nr_letters= int(input("How many letters would you like in your password?\n")) 
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))
        
        password_list = []
        
        
        for char in range(1,nr_letters+1):
            password_list.append(random.choice(self.letters))
            
        for char in range(1,nr_symbols+1):
            password_list +=random.choice(self.symbols)
            
        for char in range(1,nr_numbers+1):
            password_list+=random.choice(self.numbers)
            
        random.shuffle(password_list)
        print(password_list)
        password =" "
        for char in password_list:
                password += char
        print(f" your password is :{password}")
a = generator()
a.align_password()

