print (20*"=")
print (" PROGRAM KALKULATOR")
print (20*"=")

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    return x / y

print("Pilih Operasi Aritmatika: ")
print("1.Penjumlahan")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")

choice = input("Pilih nomor (1/2/3/4): ")
nomor1 = int(input("Masukkan Bilangan Pertama : "))
nomor2 = int(input("Masukkan Bilangan Kedua : "))

if choice == '1':
    print(nomor1,"+",nomor2,"=", tambah(nomor1,nomor2))

if choice == '4':
    print(nomor1,":",nomor2,"=", bagi(nomor1,nomor2))
