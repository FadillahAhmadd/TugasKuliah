# Variabel inputan
tugas = float(input("Masukkan nilai tugas : "))
uts = float(input("Masukkan nilai UTS : "))
uas = float(input("Masukkan nilai UAS : "))

# Variabel menentukan nilai
nilai = (0.25 * tugas) + (0.35 * uts) + (0.40 * uas)

# Menentukan grade dari nilai
if nilai > 85 :
    grade = "A"
elif nilai > 80 : 
    grade = "A -"
elif nilai >= 75 : 
    grade = "B +"
elif nilai >= 70 : 
   grade = "B"
elif nilai >= 65 : 
    grade = "B -"
elif nilai >= 60 : 
    grade = "C +"
elif nilai >= 55 : 
    grade = "C"
elif nilai >= 50 : 
    grade = "C -"
elif nilai >= 30 : 
    grade = "D"
elif nilai == 30 : 
    grade = "E"

# Lulus atau tidak lulus
if nilai > 75 :
    status = "LULUS"
else :
    status = "TIDAK LULUS"
    
# Tampilan output
print ("-------------------------")
print ("Nilai akhir : ",nilai)
print ("Nilai Huruf : {} ".format(grade))
print ("Status : {}".format(status))
