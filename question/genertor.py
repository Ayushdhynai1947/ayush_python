def genertar(n):
    for  x in range(n):
        yield x**2
        
p = genertar(8)
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())

    
    

    