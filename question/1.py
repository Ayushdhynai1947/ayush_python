"write a program to print first n natural number"
print("enter  two numbers")
a = int(input())
b = int (input())
L= a if a>b else b
while L <=a*b:
    if L%a ==0 and L%b==0:
        print('LCM is',L)
        break
    L+=1
print()


#####################################
i = 1
while i<+10:
    print(2*i-1,end=' ')
    i+=1
print()
################################e
i = 1
while i<=10:
    print(2*i-2,end=' ')
    i+=1
print()
#################################3

help(list)



####################################
t1 =tuple([int(e) for e in input().split(",")] )
t1 =tuple()
t2 = tuple([1,2,3])
t3 = tuple(range(5))
#######################
############################

def f1():
    print("enter a number")
    n = int(input())
    for e in range(1,n+1):
        print(e**2, end='')
    print()
    

f1()




#########recusrion funtion ###########
def f1(n):
    if n ==1:
        return 1
    
    s  = n +f1(n-1)
    return s

f1(4)
        
        
        
        
##############factorail using recursion ############
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)


f = lambda n: 1 if n ==0 or n==1 else n*f(n-1)


