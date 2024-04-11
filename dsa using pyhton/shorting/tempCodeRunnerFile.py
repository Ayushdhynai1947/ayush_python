def quick_short(list1):
    if len(list1)<=1:
        return list1
    else:
        pivot =list1[0]
        lesser = [x for x in list1[1:] if x<=pivot]
        greater  = [x for x in list1[1:] if x>pivot]
        return quick_short(lesser) +[pivot]+ quick_short(greater)
    
    
mylist =[23,21,12,43,54,14,51,35,34,91,19]
quick_short(mylist)
print(mylist)