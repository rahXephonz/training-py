print("Ini adalah program Pembagian")

while(True):
    try :
        penyebut = int(input("Masukan nilai penyebut : "))
        pembilang = int(input("Masukan nilai pembilang : "))
        hasil = penyebut/pembilang
        break
    except Exception as error:
        print(error)

""" 
    type of exception errors:
    1.IOError #biasanya error ketika file corrupt
    2.ImportError #belum install modul package
    3.ValueError #Nilai bukan value melainkan string
    4.Division by zero #nilai pembagi tak terhingga ex: 10/0
    5.KeyboardInterupted
    6.EOFError

"""


print("berhasil,hasil pembagian adalah", hasil)
