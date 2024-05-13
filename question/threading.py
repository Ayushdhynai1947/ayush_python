from threading import *
class hello(Thread):
    
    def run(self):
        for i in range(500):
            print("heelow world")
            
            
            
class hi(Thread):
    def run(self):
        for i in range(355):
            print("hi")
            
ob1 = hello()
ob2 = hi()

ob1.start()
ob2.start()
        