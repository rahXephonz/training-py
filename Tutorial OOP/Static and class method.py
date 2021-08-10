class Ojek():
    #private class variabel
        __jumlah = 0

        def __init__(self,nama):
            self.__nama = nama
            Ojek.__jumlah += 1

        def ambilnama(self):
            return self.__nama

        #tidak bisa diambil karena berbentuk sendiri
        def getJumlah(self):
            return Ojek.__jumlah

        #method ini berfungsi untuk mengambil value dan string dari class tapi tidak untuk objek
        #def getJumlah1():
        #    return Ojek.__jumlah

        #method static (DECORATOR) berlaku untuk objek dan class
        #tidak memakai argumen
        @staticmethod
        def getJumlah2():
            return Ojek.__jumlah
        
        #polymorphism bisa ke objek dan class sama kaya method static
        #bisa memakai argumen juga
        @classmethod
        def getJumlah3(objek):
            return objek.__jumlah


User1 = Ojek('Ujang') #ini adalah objek
print("Nama Ojek : ",User1.ambilnama()) #inisialisasi pengambilan nama pada function name self
print("User ke : ",Ojek.getJumlah2())
print("\n")

User2 = Ojek('Hyakimaru')
print("Nama Ojek : ",User2.ambilnama())
print("User ke : : ",User2.getJumlah2())
print("\n")

User3 = Ojek('Donald Trump')
print("Nama Ojek : ",User3.ambilnama())
print("User ke : ",Ojek.getJumlah3())
print("User ke : ",User3.getJumlah3())
print("\n")


        