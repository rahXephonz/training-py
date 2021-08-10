bahan_pokok = []
minuman1= []

def menu():
    print("Pilih : ")
    print("[1].Bahan Pokok")
    print("[2].Keluar")
    print("\n")

    while(True):
        pilihan = input("Silahkan Pilih Nomornya! : ")
        if pilihan == '1':
            bahan_nya()
            break
        elif pilihan == '2':
            exit()
        else : 
            print("Masukan Input dengan Benar!")

def minuman():
    while(True):
        print("Ingin Menambahkan minum?")
        quest = input("YES/NO : ")
        if quest == "YES":
            minum = input("Nama Minuman : ")
            minuman1.append(minum)
        elif quest == "NO":
            print("Anda Mempunyai Makanan : ")
            for bhn in range (len(bahan_pokok)):
                print([bhn],bahan_pokok[bhn])
            print("Dan Minuman : ")
            for mnm in range (len(minuman1)):
                print([mnm],minuman1[mnm])
            break
        else : 
            print("Masukkan input dengan Benar!")



def bahan_nya():
    makanan = input("Masukan Nama Makanan : ")
    bahan_pokok.append(makanan)
    while(True):
        quest = input("Ingin Menambah lagi? (Y/N) : ")
        if quest == "Y":
             makanan = input("Masukan Nama Makanan : ")
             bahan_pokok.append(makanan)
        elif quest == "N":
             minuman()
             break
        else:
            print("Masukan input dengan Benar!")
      
menu()