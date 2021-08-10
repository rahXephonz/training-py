mondo = []
liyuee = []

class mondstadt():
    __nilai = 0 #private atribute

    def __init__(self,input_nama): #langsung muncul dan tidak bisa diinput dari terminal
        self.nama = input_nama
    
    def uas(self,input_nilai):
        self.__nilai += input_nilai
    
    def uts(self,input_nilai):
        self.__nilai += input_nilai
    
    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama,"Tidak Lulus")
        else:
            print(self.nama,"Lulus")


class liyue():
    def __init__(self,input_nama):
        self.nama = input_nama

#Mondstadt
print("="*20)
print("Character in Mondstadt : ")
chara1 = mondstadt("Jean")
print("Nama : ",chara1.nama)

chara1.uts(70)
chara1.uas(50)
chara1.check_status()

print("="*20)
print("Character in Liyue : ")
chara1 = liyue("Zhong Li")
print("Nama : ",chara1.nama)

