# Mendeklarasikan variabel "terbesar" bertipe data interger.
terbesar = 0

print("Masukan bilangan 0 untuk berhenti: ")

# Membuat perulangan terjadi terus-menerus.
while True:
    # Mendeklarasikan variabel n sebagai input dengan tipe data integer.
    n = int(input("Masukan bilangan: "))
    # Kondisi untuk berhenti.
    if n == 0:
        break
    # Kondisi untuk menyimpan nilai terbesar.
    elif n > terbesar:
        # Menyimpan nilai dari variabel n.
        terbesar = n

# Mencetak input dengan nilai terbesar.
print("Bilangan terbesar adalah: ", terbesar)