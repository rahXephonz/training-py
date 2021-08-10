


#Kelas Kubus    
def volume_kubus(x,y,z):
    return x * y * z

def luas_permukaan_kubus(y,z):
    return 6 * y * z

def sisi_rusuk_kubus(x):
    return x ** 3

def volume_persegi(x,y,z):
    return x * y * z

#Kelas Persegi
def luas_permukaan_persegi1(x,y,z):
    return 2 * (x*y)+(x*z)+(y*z)

def luas_permukaan_persegi2(x,y,z):
    return 2 * (x*y+x*z+y*z)   

def panjang_persegi(x,y,z):
    return (x/2-y*z) / (y+z)

#Kelas Tabung
def volume_tabung(x,y):
    return (x*x*y)

def show_menu():
    print("\n========KALKULATOR BANGUN RUANG========")
    print("\nSilahkan Pilih Bangun Ruang: ")
    print("\n1.Kubus")
    print("2.Persegi")
    print("3.Tabung")
    print("4.Kerucut")
    print("5.Limas Segitiga")
    print("6.Bola")
    print("7.Prisma")
    print("8.Exit")

show_menu()


print("\n")
pilihan = input("Silahkan Pilih (1/2/3/4/5/6/7/8) : ")

if pilihan == '1':
    print("\nIngin mencari Apa? : ")
    print("A.Volume")
    print("B.Luas Permukaan")
    print("C.Sisi Rusuk")
    pilihan = input("Silahkan Pilih (A/B/C) : ")
    
    if pilihan == 'a':
        print("\nMasukan Nilai V : ")
        num1 = int(input("Masukkan Bilangan Pertama : "))
        num2 = int(input("Masukkan Bilangan Kedua : "))
        num3 = int(input("Masukkan Bilangan Ketiga : "))
        print("Volume kubus dari vol",num1,"x",num2,"x",num3,"= adalah",volume_kubus(num1,num2,num3))
    elif pilihan == 'b':
        print("\nMasukkan Nilai L :")
        num1 = int(input("Masukkan Luas Permukaan : "))
        num2 = int(input("Masukkan Volume : "))
        print("Luas Permukaan dan Volume dari 6 x",num1,"x",num2,"= adalah",luas_permukaan_kubus(num1,num2))
    elif pilihan == 'c':
        print("\nBerapakah nilai V?")
        num1 = int(input("Nilai volume : "))
        print("Nilai V : ",num1,"adalah",sisi_rusuk_kubus(num1))
        print(num1,"x",num1,"x",num1)
    else:
        print("Tidak ditemukan!")   

elif pilihan == '2':
    print("\nIngin mencari Apa? : ")
    print("A.Volume")
    print("C.Panjang")
    print("B.Luas Permukaan")
    pilihan = input("Silahkan Pilih (A/B/C) : ")

    if pilihan == 'a':
        print("\nMasukkan Nilai V : ")
        num1 = int(input("Masukkan Bilangan Pertama : "))
        num2 = int(input("Masukkan Bilangan Kedua : "))
        num3 = int(input("Masukkan Bilangan Ketiga : "))
        print("Volume persegi dari vol",num1,"x",num2,"x",num3,"= adalah",volume_persegi(num1,num2,num3))
    elif pilihan == 'b':
        print("\nBerapa nilai V dan LP?")
        num1 = int(input("Nilai 1 : "))
        num2 = int(input("Nilai 2 : "))
        num3 = int(input("Nilai 3 : "))
        print("Volume nilai dari",num1,",",num2,",",num3,"adalah",luas_permukaan_persegi1(num1,num2,num3))
        print("dan Luas Permukaan dari ",num1,",",num2,",",num3,"adalah",luas_permukaan_persegi2(num1,num2,num3))
    elif pilihan == 'c':
        print("\nBerapa Panjang Balok?")
        num1 = int(input("Nilai L : "))
        num2 = int(input("Nilai l : "))
        num3 = int(input("Nilai t : "))
        print("Panjang balok dari",num1,",",num2,",",num3,"adalah",panjang_persegi(num1,num2,num3))
    else:
        print("Tidak ditemukan!")

elif pilihan == '3':
    print("\nIngin Mencari Apa?")
    print("A.Volume")
    print("B.Luas Permukaan")
    print("C.Luas Selimut")
    print("D.Luas Alas")
    pilihan = input("Pilih (A,B,C,D) : ")
    if pilihan == 'a':
        print("Masukkan Nilai")
        num1 = int(input("Nilai r : "))
        num2 = int(input("Nilai t : "))
        print("Nilai dari",num1,",",num2,"adalah",volume_tabung(num1,num2))

elif pilihan == '8':
    exit()

else:
    print("Tidak ditemukan!")

