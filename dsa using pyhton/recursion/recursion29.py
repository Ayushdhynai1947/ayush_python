#write a program to clculate sum of first N natural number 
def sumn(n):
    
    if n ==1:
        return 1
    
    return n +sumn(n-1)

t = sumn(5)
print(t)


# write a recusive function to calulate sum of N odd number
def sumodd(n):
    if  n ==1:
        return 1
    return 2*n-1 + sumodd(n-1)
t = sumodd(5)
print(t)

# sum of first even natural number


def sumeven(n):
    if n ==1:
        return 2
    return 2*n+ sumeven(n-1)

k = sumeven(3)
print(k)



# factorial 
def factorial(n):
    if n ==0:
        return 1
    return n*factorial(n-1)

print("sum is ",factorial(20))
    
    
    
# recusive function to culaulate sum of square of first N natural number

def sumofsquare(n):
    if n ==1:
        return 1
    return n*n +sumofsquare(n-1)

print ("sum is ",sumofsquare(10))
    