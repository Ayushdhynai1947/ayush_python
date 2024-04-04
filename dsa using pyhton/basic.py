li = [True ,'heeelo', 1 , 23,4]
print(li)

li.append([1,2,4,5,6,7])
print(li)

li.pop(2)
print(li)

##############################################################
li ={'mango ':45 ,'apple':30 ,'orange':77}
print(li)
print(li.keys)

#######################################################################

# addiing maore then one elment in a set , set can not conatin duplicate vlaue 
# value which make them unique from other
s1 = {1,'q',4,3,16, 1,23,4,5,555,55,5}
print(s1)

#adding single value in set
s1.add('heelo world')

# for multiple value 
s1.update([2,1,2,4,5])
print(s1)








##################(1d)####################################################
my_array = []

# Ask the user for input
n = int(input("Enter the number of elements: "))

# Loop to enter elements
for i in range(n):
    element = input("Enter element {}: ".format(i + 1))
    my_array.append(element)

# Print the array
print("Array:", my_array)



############(2d)#######################################################
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
array_2d = []

# Input elements into the 2D array
for i in range(rows):
    row = []
    for j in range(cols):
        element = input("Enter element at position ({}, {}): ".format(i, j))
        row.append(element)
    array_2d.append(row)

# Print the 2D array
print("2D Array:")
for row in array_2d:
    print(row)
    
    
    
#############deleting element in  aray ##############################################################
my_aaray = []

# Input number of elements
num_elements = int(input('Enter the number of elements in the array: '))

# Loop to input elements
for k in range(num_elements):
    element = input("Enter the element {}: ".format(k+1))
    my_aaray.append(element)
    
print("Array:", my_aaray)

# Input value to remove
val = input("Enter the value to remove: ")

# Check if value exists in array and remove it
if val in my_aaray:
    my_aaray.remove(val)
    print("Array after removal:", end=" ")
    for i in range(len(my_aaray)):
        print(my_aaray[i], end=" ")
else:
    print('Value not found in array')
    
    
################################################################################

arr = [10, 22, 38,27,11]
temp = 0

print('elements of orignial array ',arr)
for i in range(0,len(arr)):
    print(arr[i], end=" ")
    
for i in range (0,len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i] > arr[j]):
            temp = arr[i]
            arr[i] =arr[j]
            arr[j] = temp

print('Elements of array sorted in ascending order')
for i in range(0,len(arr)):
    print(arr[i], end= " ")
    
#########################################################################




#####(searching in the array )##########################################################
import array
arr = array.array('i',[1,2,3,1,2,5])
print('the new created array is:' , end=" ")
for i in range(0,6):
    print(arr[i], end=" ")
print('\r')
print(' the index of 1st occurrence of 2 is :' ,end = "")
print(arr.index(2))
print('the index of 1st occurence of 1 is:' ,end =" ")
print(arr.index(1))
#########################################################################





########(stack used)###############################################################333
stack= []
stack.append('welcome')
stack.append('to')
stack.append("greater learning ")
print(stack)

#####################################################################3
from queue import LifoQueue
stack = LifoQueue()

    