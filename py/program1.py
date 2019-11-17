# Mendifinisikan variabel
modal = 100000000
laba = 0
keuntungan = 0

# Perulangan for menggunakan fungsi range().
for i in range(1, 9):
    # Kondisi pertama
    if i <= 2:
        persentase = 0
    # Kondisi kedua
    elif i <= 4:
        persentase = 1
    # Kondisi ketiga
    elif i <= 7:
        persentase = 5
    # Kondisi terakhir
    elif i <= 8:
        persentase = persentase - 2

    # keuntungan & laba diletakan disini agar lebih simpel
    laba = modal * persentase / 100
    keuntungan = keuntungan + laba
    print ( "Bulan ke-", i, "sebesar: ", laba)

# Mencetak hasil akhir
print("Total laba adalah: ", keuntungan)