
def genertor(n):
    yield (x**2 for x in range(n))
    
p = genertor(8)
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())

    
    

    