#import berfungsi untuk memanggil program yang telah dibuat
#misalkan program itu mempunyai banyak baris ex : 1000 baris

#import modul

#modul.contoh_modul()
#print("\n")
#modul.ini_chara()
#print("\n")

#import modul as math

#math.contoh_modul()
#print("\n")
#math.ini_chara()
#print("\n")

#from modul import pangkat, kuadrat
#Ini secara spesifik memanggil nilai function

#from modul import *

from modul import pangkat as p,kuadrat as k
#Lebih spesifik tetapi khusus integer,float kayanya

p(3)
k(3)
