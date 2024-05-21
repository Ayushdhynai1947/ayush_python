def friends_in_trouble(j_angry, s_angry):
    if j_angry==s_angry:
        return True
    else:
        return False
    
p= friends_in_trouble(True,False)
print(p)

#########################################
# 0 /10
# For Input: 
# 1
# Your Code's output is: 
# Even
# It's Correct output is: 
# Odd
# Output Difference
# EvenOdd
####################################

def checkOddEven(x):
    if(x % 2 == 0) and (x<=2):
      return "Even"
    else:
        return "Odd"

print(checkOddEven(1))


###########################################
def pos(n):
    if n>0 :
        print(n-1)
        pos(n-1)
        
print(pos(4))

def neg(n):
    if n <0:
        print(n)
        neg(n+1)

print(neg(-4))
