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



