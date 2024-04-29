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

## namespace  is mapping if name with the object 


# local scope in pyhton 
class person():
    def __init__(self, age):
        self.age = age 
        

fab  = person(age= 45)
print(fab.age)
print(id(fab))
print(id(fab.age))

fab.age = 34
print(id(fab))
##############################3
# immutable string,touple,bytes

c = list(zip(['h','e','l','l','o'],[1,2,3,4,5]))
print(c)

d = dict(zip('hello',range(5)))
print(d)





######################enumeratoe in pyhton #################
surnames = ['ayush','dhyani','kiran']
for position,surname in enumerate(surnames):
    print(position,surname)
    
    
    
    
pople = ['ayush ','dhyani ','rahul ', 'siya']
ages =[23,45,67,87]
nationality = ['poaland','india','soutafrica','antarica']
for perosn ,age,nationalityes in zip(pople,ages,nationality):
    print(perosn,age,nationalityes)
    
    
    
############another method################ 
pople = ['ayush ','dhyani ','rahul ', 'siya']
ages =[23,45,67,87]
nationality = ['poaland','india','soutafrica','antarica']
for data in zip(pople,ages,nationality):
    perosn,age,nationalityes=data
    print(perosn,age,nationalityes)
    
    
##########################


n = 45
remainer =[]
while n>0:
    n,remainer =divmod(n,2)
    remainer.insert(0,remainer)
    
    
##################prime genartor   #######################
primes =[]
upto = 100
for n in range(2,upto+1):
    flag = True
    for number in range(2,n):
        if n%number ==0:
            flag = False
            break
        
    if flag:
        primes.append(n)
print(primes)



for n in range(2,5):
    print(n)
    
    
    
    
    
    
    
    
    
    
    
##########psotional argument########################

def miminum(*n):
    print(type(n)) 
    
    if n:
        mn=n[0]
        for vaalue in n[1:]:
            if vaalue<mn:
                mn= vaalue
        print(mn)  

miminum(1,2,3,-4)



##########variablel keyword argumnet 
def fun(**kwargs):
    print(type(kwargs)) 
    
    print(kwargs)
    
fun(a=2,b =5,c = 7)




################lamda function ###############
def is_multiple(n):
    return  not n %5

def get_multiple(n):
    return list(filter(is_multiple,range(n)))


p = get_multiple(10)
print(p)


######################zip function ############

a =[3,4,5,6,6]
b = [3,45,5,6,7]
_maxz = map(lambda n:max(*n),zip(a,b))
print(_maxz)



a =[3,4,5,6,6]
p = list(filter(lambda x:x ,a))
print(p)










#############fibonachi second#########
def fibonacci(N):
    yield 0
    if N==0:
        return
    
    a =0
    b =1
    while b<=N:
        yield b
        a,b = b,a+b
        
print(list(fibonacci(5)))