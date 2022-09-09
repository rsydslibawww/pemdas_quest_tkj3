# Program Sintaks Volume Bangun Ruang

print("\n1. Volume Balok")
P = int(input("Masukan nilai Panjang: "))
L = int(input("Masukan nilai Lebar: "))
T = int(input("Masukan nilai Tinggi: "))
volume_B = P * L * T 
print("Volume Balok adalah", volume_B)

print("\n2. Volume Kubus")
S = int(input("Masukan nilai Sisi: "))
volume_K = S * S * S
print("Volume Kubus adalah", volume_K)

print("\n3. Volume Tabung")
Phi = 22/7
r1  = int(input("Masukan nilai r1: "))
r2  = int(input("Masukan nilai r2: "))
t   = int(input("Masukan nilai t: "))
volume_T = Phi * r1 *r2 * t
print("Volume Tabung adalah", volume_T)

print("\n4. Volume Limas")
la  = int(input("Masukan nilai luas alas: "))
t   = int(input("Masukan nilai tinggi: "))
volume_l = 1/3 * la * t
print("Volume Limas adalah", volume_l)

# Celcious to reamur

print("\n1. Nilai Celcius ke reamur")
C = int(input("Masukkan nilai Celcius: "))
nilai_r = 4/5 * C
print("Nilai 1 Celcius adalah", nilai_r)
