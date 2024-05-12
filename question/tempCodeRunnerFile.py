

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