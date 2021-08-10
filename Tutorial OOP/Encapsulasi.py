#Encapsulasi standar

class Heroes():
    
    def __init__(self,name,power,health):
        self.__nama = name
        self.__kekuatan = power
        self.__darah = health
    
    #getter untuk merubah nilai string atau variabel didalam init

    def getName(self) :
        return self.__nama
    
    def getHealth(self):
        return self.__darah

    #setter untuk merubah nilai string atau variabel dalam proses

    def Attacking(self,AttPower):
        self.__darah -= AttPower
    
    def setHealth(self,nilaiBaru):
        self.__darah = nilaiBaru



Hero1 = Heroes("Nizar Korabelnikob",1000,500) #Hero1
Hero2 = Heroes("Nikolai Unmeldov",2000,1000) #Hero2

print("Nama Hero : ",Hero1.getName())
print("Darah Hero : ",Hero1.getHealth())

#Merubah nilai health
Hero1.Attacking(200)
print("Darah Hero Setelah diserang : ",Hero1.getHealth())
Hero1.setHealth(3000)
print("Darah Hero Setelah di Buff : ",Hero1.getHealth())