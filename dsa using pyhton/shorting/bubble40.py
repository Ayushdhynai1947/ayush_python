def bubble_sort(data_list):
    for r in range(1,len(data_list)):
        for i in range(len(data_list)-1):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                
                
                
                
def modifybubble_sort(data_list):
    flag = False
    for r in range(1,len(data_list)):
        flag = False
        for i in range(len(data_list)-1):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                flag = True
        if not flag:
            break
                                   
                
                
                
                
                
                

l=[23,34,32,43,56,65,54,21,31]
modifybubble_sort(l) 
print(l)            
                