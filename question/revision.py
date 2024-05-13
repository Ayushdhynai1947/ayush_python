def deco(fun1):
    def check(result):
        for s in result:
            if s>77:
                print("distinction")
        else:
            fun1(result)
    return check


@deco
def value(result):
    for m in result:
        if m >33:
            print("passs")
        else:
            print("fail")
        
    else:
        print("pass")
        
        
value([23,45,78,12,34])
        
#######################################

def deco(fun1):
    def check (*args, **kwargs):
        print("give to number ",*args)
        c=fun1(*args,**kwargs)
        
     
    return check
@deco
def sum(a,b):
    c =  a+b
    print("Sum",c)
sum(2,3)
    
###########################################
###args and quargs defrence 

def example_function (*args, **kwargs):
    print("position argumnet  is ",args)
    print("key word argumnet is ",kwargs)
    
example_function(1,2,3, a=4, b =5 ,n=9)
############################################ mw_nu_rwt



###########object consept############################

class computer:
    
    def __init__(self) -> None:
        self.cpu = "i7"
        self.ram =16
        
    
    
    def show():
        print('heelo world')

com1 = computer()
com1.cpu = "i7"

com2 = computer()
com2.cpu ="i9"
print(com1.cpu)
###########################################################



###########################################################
class Student:
    def __init__(self,marks) -> None:
        self.marks =marks
        
        
    def compare(s1,s2):
        if s1.marks >s2.marks:
            print("s1")
        else:
            print("s2")
            
s1 = Student(23)
s2 = Student(20)

Student.compare(s1,s2)
#####################################################



################################################
class student:
    
    name = "dav"
    def __init__(self,marks) -> None:
        self.mark = marks 
        
    def get_marks(self):
        return self.mark
    @classmethod
    def check_name(cls):
        return cls.name
    @staticmethod
    def add(x,y):
        return x+y 
    
    
a1 = student(23)
print(a1.mark)
print(a1.add(3,4))

print(student.check_name())
######################################################




#########################################################
class A:
    def f1(self):
        print("I am f1")

class B:
    def f2(self):
        print( " iam b f2")

class C(B,A):
    
    def f3(self):
        print(" i am C f3")
        

ob =C()
ob.f2()
ob.f3()

##############################################################



#####################################################
class A:
    def __init__(self) -> None:
        self.m1 = 9
class B:
    
    def __init__(self) -> None:
        self.m2 = 3      
class C(B,A):
    
    def __init__(self) -> None:
        A.__init__(self)
        B.__init__(self)
        self.m3 =8

obj = C()

print(obj.m3)
print(obj.m2)
print(obj.m1)

####################################################
##################operartor overloding######################



##############################################################



class A:  
    def __init__(self,m1 ,m2) -> None:
        self.m1 = m1
        self.m2 = m2
        
    def __add__(self,other):
        total_m1 = self.m1 + other.m1
        total_m2 = self.m2 + other.m2 
        s3 = A(total_m1,total_m2)
        return s3
    
    def __sub__ (self,other):
        total_m1 = self.m1 - other.m1
        total_m2 = self.m2 - other.m2
        s4 = A(total_m1,total_m2)
        return s4
      
    def __str__(self) -> str:
        return str(self.m1) + ":"+ str(self.m2)  
    
     
c1 = A(23,45)
c2 = A(54,76)

s3 = c1 + c2    # A.__add__(s1,s2)
               # s1.__add__(s2)
s4 = c1 - c2
print(s3)
print(s4)



#################################################################



#################funtiona overloding##################################################
class O1 :
    
    
    def call(self):
        print("calling 15")
        
    
    def getNotification(self):
        print("Notification on top 15")
        
        
class OS2(O1):
    def getNotification(self):
        print("notification at the bottom ,16")
        
        
class IPHONE:
    
    def getOSVersion(self,os):
        os.getNotification()
    
    def call(self,os):
        os.call()

a1 =OS2()
# a1.getNotification()

a2 = IPHONE()
a2.getOSVersion(a1)
a2.call(a1)

#####################################################



###################################################


##########overloding ####################
class  Calculator:
    
    # def add(self,n1 ,n2):
    #     print(n1+n2)
        
    def add(self,n1,n2=0,n3=0):
        print(n1+n2+n3)
        
        
    def add1 (self,n1,n2,n3):
        s = 0
        
        if n3!=None:
            s = n1+n2+n3
        elif n2!=None:
            s =n1+n2
        else:
            s = n1
        
        return s
            
        
        
c1 = Calculator()
c1.add(4,5)