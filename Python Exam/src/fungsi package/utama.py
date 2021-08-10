
def aritmatika():
    print("\nIni adalah bagian dari aritmatika")
    print("\n[1].Pertambahan")
    print("[2].Pengurangan")
    print("[3].Pembagian")
    print("[4].Perkalian")
    print("[5].Kuadrat")
    print("[6].Pangkat")
    
    menu = input("\nSilahkan Pilih Angka 1/2/3/4/5/6 > ")
    if menu == '1':
        pass


def main_menu():
    print("\nSelamat datang di Terminal Aplication")
    print("\n[1].Aritmatika")
    print("[2].Fisika")
    print("[3].Geometry")
    print("[4].Exit")
    
    menu = input("\nSilahkan Pilih Angka 1-2-3-4 > ")
    if menu == '1':
        print("ini adalah aritmatika")
        aritmatika()
    elif menu == '2':
        print("Ini adalah Fisika")
    elif menu == '3':
        print("ini adalah Geometry")
    elif menu == '4':
        exit()
    else :
        print("pilih menu yang benar!")

main_menu()