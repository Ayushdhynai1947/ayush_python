def printodd(n):
    if n >0:
        
        print(2*n-1 ,end=' ')
        printodd(n-1)
        
t =printodd(6)
print(t)
