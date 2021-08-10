nama_member = ['Jean','klee','Barbara','Ganyu','Ningguang']
nama_elemental = ['Anemo','Pyro','Hydro','Cryo','Geo']

#teknik biasa

i = 0
for total_member in nama_member:
    print("nomor",i,"nama member",total_member)
    i += 1

print("\n")

#enumerate
for indeks,total_member in enumerate(nama_member):
    print(indeks,":",total_member)

print("\n")

#zip = menggabungkan nama member dan nama elemental

for member,elemental in zip(nama_member,nama_elemental):
    print(member,"Mempunyai elemen",elemental)

print("\n")

#Metode sorted set sesuai dengan alphabet

kelas = {"Software Engineer","Web Developer","Data Science","Specialist UI/UX"}

for macam_kelas in sorted((kelas)):
    print(macam_kelas)

print("\n")

#dictionary

#jean sebagai keys
#anemo sebagai values

member_elemental = {'Jean': 'Anemo',
               'klee': 'Pyro',
               'Barbara': 'Hydro',
               'Ganyu': 'Cryo',
               'Ningguang': 'Geo'}

for indeks1,indeks2 in member_elemental.items(): #Mengambil nilai key dan values = items
    print(indeks1,"Mempunyai elemen",indeks2)

print("\n")


print(type(nama_member))
print(type(nama_elemental))
print(type(member_elemental))
print("\n")

#membalikan perulangan dari akhir ke awal

for i in reversed(range(1,10,1)):
    print(i)

print("\n")



