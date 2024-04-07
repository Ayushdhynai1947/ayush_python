def printodd(n):
    if n >0:
        printodd(n-1)
        print(2*(n-1) ,end=' ')
        
t =printodd(6)
print(t)
