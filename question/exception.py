a = 7                                         #
c = 0
try:
    b =int(input("enter the number "))
    c = a/b    
except ZeroDivisionError:
    print("you cannot divide by zero")    
except ValueError:
    print("ebter number not string")
except Exception:
    print("anything is wrong") 
else:
    print(c)
    
finally :
    print("file closed") 

print("by")
################################################   












