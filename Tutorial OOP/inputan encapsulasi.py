class Hero():
        __jumlah = 0

        def __init__(self,name,health,attpower,armor):
            self.name= name #global bisa diubah self.__name = private
            self.healthStandar = health
            self.attpowerStandar = attpower
            self.armorStandar = armor


        @property
        def info(self):
            return "Nama Hero Baru : {}\nHealth : {}\nAttackPower : {}\nArmor : {}".format(self.name,self.healthStandar,self.attpowerStandar,self.armorStandar)


NewHero = Hero("Ex : Udin",1000,500,200)
inputan = (input("Tambah Hero? Y/N > "))
if inputan == 'Y':
    NewHero.name = (input("Nama Hero > "))
    NewHero.healthStandar = int(input("Health nya > "))
    NewHero.attpowerStandar = int(input("Attack nya > "))
    NewHero.armorStandar = int(input("Armornya > "))
    print("\n")
    print(NewHero.info)
if inputan == 'N':
    print("Nothing to do")
    pass


