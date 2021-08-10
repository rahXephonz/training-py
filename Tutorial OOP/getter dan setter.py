class Hero():

    def __init__(self,name,health,armor):
        self.name = name #global method variable
        self.__health = health #private variable
        self.__armor = armor #private variable
        #self.__info = "name : {} \n\thealth : {} \narmon : {}".format(self.name,self.__health,self.__armor)
    
    #mengubah method seperti variabel
    @property
    def info(self):
        return "name : {} \n\thealth : {} ".format(self.name,self.__health)
    @property
    def armor(self):
        pass
    @armor.getter
    def armor(self):
        return self.__armor
    @armor.setter
    def armor(self,input):
        self.__armor = input    
    @armor.deleter
    def armor(self):
        print("Armor di Delete!")
        self.__armor = None


print("\nMerubah Info")
User = Hero('Sniper',2000,1000)
print(User.info)
User.name = 'Samuel' #mengambil variable global
print(User.info)
User.name = (input("Nama Hero Baru? > "))
print(User.info)
print("\n")

print("getter dan setter untuk __armor")
print("Armor Hero : ",User.armor)
User.armor = int(input("Buff Armor sampai : "))
print("Armor Hero Setelah di Buff : ",User.armor)

inputan = (input("Ingin Mendelete Armor? (Y/N) > "))
if inputan == 'Y' :
    del User.armor
    print("Armor Menjadi : ",User.armor)
if inputan == 'N' :
    print("Armor tidak di Delete")



