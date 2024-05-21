from threading import *
from time import sleep

# heelo 
# hi
#main



class hello(Thread):
    
    def run(self):
        for i in range(500):
            print("hello world")
            sleep(2)
            
            
class hi(Thread):
    def run(self):
        for i in range(355):
            print("hi")
            sleep(1)
            
ob1 = hello()
ob2 = hi()

ob1.start()
sleep(1)
ob2.start()


ob1.join()
ob2.join()
print("by")
