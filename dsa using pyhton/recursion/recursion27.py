# recursion : when a function call itself  again and againis called recursion

def f1(n):
    if n ==1:
        return 1
    s = n + f1(n-1)
    return s

r= f1(3)
print(r)



#############################################
#write a recursion function to calculate sum of first n natural number 

def f1(n):
    if n ==1:
        return 1
    return n + f1(n-1)


n = f1(6)
print(n)


############################################################
###write a resursion function to print first N natural number.

def printN(n):
    if n >0:
        printN(n-1)
        print(n,end=" ")
t =printN(6)
print(t)

# write a recursive function to print  N nautral number in reverse order 
def printreverse(n):
    if n >0:
        print(n,end=" ")
        printreverse(n-1)
t =printreverse(6)
print(t)

# even  natural  number  using recursion 
def printodd(n):
    if n >0:
        printodd(n-1)
        print(2*(n-1) ,end=' ')
        
t =printodd(6)
print(t)



###################################


########even number in reverse order############################
def printodd(n):
    if n >0:
        print(2*(n-1) ,end=' ')
        printodd(n-1)
        
        
t =printodd(6)
print(t)





#########################################################
# odd natural number
def printodd(n):
    if n >0:
        printodd(n-1)
        print(2*n-1 ,end=' ')
        
t =printodd(6)
print(t)

    
########################################################




###########order number inr reverse order##################################
def printodd(n):
    if n >0:
        
        print(2*n-1 ,end=' ')
        printodd(n-1)
        
t =printodd(6)
print(t)
