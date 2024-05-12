
#################funtiona overloding##################################################
class O1 :
    
    
    def call(self):
        print("calling 15")
        
    
    def getNotification(self):
        print("Notification on top 15")
        
        
class OS2(O1):
    def getNotification(self):
        print("notification at the bottom ,16")
        
        
class IPHONE:
    
    def getOSVersion(self,os):
        os.getNotification()
    
    # def call(self,os):
    #     os.call()

    
    
        

a1 =OS2()
# a1.getNotification()

a2 = IPHONE()
a2.getOSVersion(a1)
