class Animals(object):
    def Mammal(self,blood,lays_eggs):
        if blood=="warmth" and lays_eggs==False:
            return True
        

    def Reptile(self,blood,lays_eggs):
        if blood=="cold" and lays_eggs==True:
         return True
        

a=Animals()
blood=input("Enter The Blood::")
lays_eggs=input("Enter The Birth Sequence::")

if a.Mammal(blood,lays_eggs):
    print("Mammal")
    
elif a.Reptile(blood,lays_eggs):
    print("Reptile")
