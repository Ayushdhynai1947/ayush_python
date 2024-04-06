def sumofsquare(n):
    if n ==1:
        return 1
    return n*n +sumofsquare(n-1)

print ("sum is ",sumofsquare(10))
    