'''Bangun datar
    - Persegi
    - Segitiga
    - Jajargenjang
    - Lingkaran'''


# Rumus Persigi Sisi * Sisi

sisi1 = 10
sisi2 = 10
luas_p = sisi1 * sisi2

print("Luas persegi adalah", luas_p)

# Rumus segitiga A * T / 2\

alas = 20
tinggi = 10
luas_s = alas * tinggi / 2

print("Luas seigitia adalah", luas_s)

# Rumus jajar genjang A * T

alas = 10
tinggi = 7
luas_j = alas * tinggi

print("Luas jajargenjang adalah", luas_j)

# Rumus Lingkaran 22/7 * r * r

phi = 22/7
r    = 14
r    = 14
luas_l = phi * r * r

print("Luas lingkaran adalah", luas_l)

# Progam Dinamis

print("\n1. Luas Persegi")
sisi = int(input("Masukan nilai sisi: "))
luas_P = sisi * sisi
print("Luas Pesegi adalah", luas_P)

