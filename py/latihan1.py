import random

# Mendeklarasikan variabel n sebagai input dengan tipe data integer
n = int(input("Masukan nilai N: "))
# Perulangan untuk mencetak berapa baris yang dibuat berdasarkan variabel n
for i in range(n):
    # Mencetak perulangan, ditambah 1 setiap perulangan terjadi, untuk menjadikan baris pertama = 1,
    # dan mencetak angka acak dengan tipe data float.
    print("data ke",i+1,":" , random.uniform(0, 0.5))
print("Selesai")
