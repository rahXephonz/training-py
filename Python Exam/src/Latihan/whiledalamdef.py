char = []

def coba_doang():
    while True:
        char_baru = input("Masukan Nama Char : ")
        char.append(char_baru)

        quest = input("Ingin menambah Char lagi? (y/t) : ")
        if quest == 't':
            break

coba_doang()
        