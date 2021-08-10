Member1 = {"ID":1001,"Nama":"Sineza Jubir","Kelas":"Web Developer"}
Member2 = {"ID":1002,"Nama":"Valerian Trifa","Kelas":"Data Science"}

memberlist = {1001:Member1,1002:Member2}

print(Member1["Nama"])
print(Member1.keys())
print(Member1.values())

print("="*20)

print("Ini Member 1 : ")
print(memberlist[1001])
print("Ini Member 2 : ")
print(memberlist[1002])


