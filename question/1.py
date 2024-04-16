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





