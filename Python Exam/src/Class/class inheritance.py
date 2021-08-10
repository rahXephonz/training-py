user = []
sim = []

class contoh_Ojek():
    
    def __init__(self,input_name,input_sim):
        self.name = input_name
        self.sim = input_sim

    def cek_id_abang(self):
        print('nama :',self.name,'\nsim : ',self.sim)

class Gojek(contoh_Ojek):
    #pass kalau ada pass maka isinya tidak dirubah atau inheritance dari kelas contoh_Ojek

    def cek_id_abang(self): #ini dioverdrive atau ditimpa
        print("Cek Aplikasi Gojek")

print("Example of Users :")
ojek1 = contoh_Ojek("Mario","168011882")
ojek2 = Gojek("Liberty","168112238")

ojek1.cek_id_abang()
ojek2.cek_id_abang()

class tambah_input_from_user():
    name = "name"
    sim = "sim"

    def nama(self):
        print(self.nama)
    def sim_motor(self):
        print(self.sim)
    

def question():
    tambah_user.name = input("Siapa Nama kamu? : ")
    user.append(tambah_user.name)
    tambah_user.sim = input("Nomor sim kamu? : ")
    sim.append(tambah_user.sim)


tambah_user = tambah_input_from_user()
question()

while(True):
    quest = input("Tambah lagi? : (y/n)")
    if quest == "y" :
        print("Okay siap!")
        question()
    elif quest == "n" :
        break
    else :
        print("Input name didn't found!")

print("Daftar User Baru: ")
for i in range (len(user)):
        print([i],user[i])

print("="*30)
print("Daftar sim User Baru: ")
for i in range (len(sim)):
        print([i],sim[i])


