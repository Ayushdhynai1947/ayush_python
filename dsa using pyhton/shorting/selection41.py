def selectionsort(list1):
    n= len(list1)
    for i in range(n):
        min_index =i
        for j in range(i+1,n):
            if list1[j]<list1[min_index]:
                min_index  =j
        list1[i],list1[min_index] = list1[min_index],list1[i]    
                
l = [21,31,23,43,12,41,14]
selectionsort(l)
print(l)

