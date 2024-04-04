''' aaray is an liner data structure
    * contiguous memory locations
    * acces elements randomly
    * homogeneous elements(similar elements ) '''




##### one dimension array ##############
my_array = []

# Ask the user for input
n = int(input("Enter the number of elements: "))

# Loop to enter elements
for i in range(n):
    element = input("Enter element {}: ".format(i + 1))
    my_array.append(element)

# Print the array
print("Array:", my_array)







########## 2D aaray  #################################
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
    
    
    
############################


##########deleting aaray###
my_array = []

# Ask the user for input
n = int(input("Enter the number of elements: "))

# Loop to enter elements
for i in range(n):
    element = input("Enter element {}: ".format(i + 1))
    my_array.append(element)

# Print the array
print("Array:", my_array)


##########enter value to be deleted
val = input('enter value to be deleted')

if val in my_array:
    my_array.remove(val)
    print("after deletion",end= "")
    for i in range (len(my_array)):
        print(my_array[i],end=' ')
    
else :
    print('value not found')
    
    
    
############shorting an array in asending order#############################
temp = 0
array = []
# Ask the user for input
n = int(input("Enter the number of elements: "))
# Loop to enter elements
for i in range(n):
    element = input("Enter element {}: ".format(i + 1))
    array.append(element)
# Print the array
print("Array:", array)


for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i] > array[j]:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            
            
for i in range (0,len(array)) :
    print (array[i] , end= ' ')          



##################################################



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




##############searching and finding occurance of an aaray##############

def find_occurrences(arr, target):
    count = 0
    for element in arr:
        if element == target:
            count += 1
    return count

# Example usage:
arr = [1, 2, 3, 4, 2, 2, 5, 2, 6]
target = 2
occurrences = find_occurrences(arr, target)
print(f"The target element {target} occurs {occurrences} times in the array.")






############searching for 2 occurance in aaray ##########################################

def check_occurrence(arr, check):
    count = 0 
    indices = []
    for index, element in enumerate(arr):
        if element == check:
            count += 1
            indices.append(index)
            if count == 2:
                return indices[-1], indices[-2]
    
    return None, None

arr = [1, 2, 3, 4, 4, 5, 6, 5, 5]
check = 4
second_occurrence_index, previous_index = check_occurrence(arr, check)
if second_occurrence_index is not None:
    print(f"The second occurrence of {check} is found at index {second_occurrence_index}.")
    print(f"The previous index of the second occurrence is {previous_index}.")
else:
    print(f"The second occurrence of {check} is not found in the array.")



""" advantges of array 
    random acces elements 
    replacement of multiple variables"""
    
    
    
    
""" disadvantages  
    * size is fixed 
    *  difficult to insert and delete 
    *  if capcity is more and occure less ,most of the array gets wasted
    *  needs contiguous memory """

