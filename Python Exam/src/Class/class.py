geometry = []


class mahasiswa(): 
    nama = "nama" #atribut nama
    
    def belajar(self,kondisi):
        print(self.nama,"Sedang belajar",kondisi)

class bangun_ruang():
    name = "name" #atribut nama
    
    def panggil(self):
        print(self.name,"adalah Bangun ruang!")

    def error(self):
        print(self.name,"Itu bukan Bangun ruang!")


#mendeklarasikan otong variabel sebagai kelas mahasiswa
otong = mahasiswa()
zasviel = mahasiswa()
kuro = mahasiswa()

#inisialisasi nama mahasiswa dengan atribut nama di class
otong.nama = "otong surotong"
zasviel.nama = "Zasvieel"
kuro.nama = "Kuro chloe"

#panggil inisialisasi dan fungsi secara bersamaan
#otong.belajar()
#zasviel.belajar()

#panggil inisialisasi dan fungsi dengan argumen
otong.belajar("dengan giat")
zasviel.belajar("dengan malas")

#inisialisasi bangun ruang itu sebagai kelas bangun ruang
bangun_ruang = bangun_ruang()

while(True):
    bangun_ruang.name = input("masukan nama bangun ruang : ")
    geometry.append(bangun_ruang.name)
    if bangun_ruang.name == "segitiga":
        bangun_ruang.panggil()
    elif bangun_ruang.name == "jajar genjang":
        bangun_ruang.panggil()
    elif bangun_ruang.name == "trapesium":
        bangun_ruang.panggil()
    elif bangun_ruang.name == "exit":
        for indeks in range (len(geometry)):
            print([indeks],geometry[indeks])
        exit()
    else : 
        bangun_ruang.error()