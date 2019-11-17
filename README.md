# PRAKTIKUM 3
## 1. Tampilkan nilai n bilangan acak yang lebih kecil dari 0.5
**Kode :**

![Lat_1](https://github.com/antonmartinus72/labpy03/blob/master/img/Lat_1.PNG)

***

***Algoritma***

Kode berikut digunakan untuk melakukan **input** data berupa tipe data integer :

    n = int(input("Masukan nilai N: "))
 
Selanjutnya fungsi `for` loop digunakan untuk melakukan perulangan berdasarkan input `n`:

    for i in range(n):
	    print("data ke",i+1,":" , random.uniform(0, 0.5))

Fungsi `print` di atas berfungsi untuk mencetak perulangan yang terjadi dan  fungsi `range(n)` berfungsi untuk membuat list dari variabel n. Terdapat `i+1`yang digunakan untuk memulai penomoran yang dimulai dari 1, karena secara default penomoran dalam statement print diatas dimulai dari 0.

    random.uniform(0, 0.5)
Kode di atas digunakan untuk mendapatkan nilai acak dengan tipe data float yang di mulai dari  0 sampai 0,5.

Fungsi `for` loop akan terus mencetak baris baru sesuai nilai yang di masukan ke dalam input `n` yang akan menghasilkan **output** berupa string dan nilai acak. Jika input `n` belum terpenuhi atau tercetak, perulangan akan terus terjadi.

**Output :**

![Lat_1_Output](https://github.com/antonmartinus72/labpy03/blob/master/img/Lat_1_Output.PNG)

## 2. Buat program untuk menampilkan bilangan terbesar dari n buah data yang diinputkan. Masukkan angka 0 untuk berhenti.

**Kode :**

![Lat_2](https://github.com/antonmartinus72/labpy03/blob/master/img/Lat_2.PNG)

***Algoritma***

Nilai terbesar di definisikan terlebih dahulu :

    terbesar = 0

Perulangan yang digunakan untuk membuat perulangan berjalan terus menerus :

    while True:

Input variabel `n` :

    n = int(input("Masukan bilangan: "))
Kondisi jika n = 0 maka perulangan akan berhenti :

    if n == 0:
	    break
Jika nilai `n` lebih besar dari variabel `terbesar`, nilai dari variabel `terbesar` akan digantikan dengan variabel `n`.

    elif n > terbesar:
	    terbesar = n

Hasil akhir dengan input terbesar akan dicetak seperti ini :

    print("Bilangan terbesar adalah: ", terbesar)
    
**Output :**

![Lat_2_Output](https://github.com/antonmartinus72/labpy03/blob/master/img/Lat_2_Output.PNG)
    
## 3. Buat program sederhana dengan perulangan. 
<p align=center>"Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan modal awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba. pada bulan ketiga baru mulai mendapatkan laba sebesar 1% dan pada bulan ke 5, pendapatan meningkat 5%, selanjutnya pada bulan ke 8 mengalami penurunan keuntungan sebesar 2%, sehingga laba menjadi 3%. Hitung total keuntungan selama 8 bulan berjalan usahanya."<p>

**Kode :**

![Pro_1](https://github.com/antonmartinus72/labpy03/blob/master/img/Pro_1.png)

***Algoritma***
Kode berikut berfungsi sebagai perulangan dan digunakan untuk mencetak berapa baris yang akan di cetak yang mewakili jumlah bulan.

    for i in range(1,9)
Kondisi untuk menentukan bulan apa saja yang akan masuk dalam perhitungan :

    if (i <= 2):
Statement di dalam kondisi di atas akan di **proses** menggunakan operator untuk membuat hasil dari persentase yang di tetapkan :

    persentase = 5  
    laba = modal * persentase / 100
    keuntungan = keuntungan + laba
Variabel persentase di atas di definisikan terlebih dahulu agar lebih **mudah** dilihat berapa persentase yang digunakan. Dan jika ada **pengurangan persentase**, maka akan jadi seperti ini :

    persentase = persentase - 2

Kemudian hasil laba di cetak seperti ini :

    print ( "Bulan ke-", i, "sebesar: ", laba)

Total **keuntungan** didapatkan dengan cara menambahkan setiap keuntungan yang terus ditambah di setiap hasil kondisi dalam kode :

    keuntungan = keuntungan + laba

**Output :**

![Pro_1_Output](https://github.com/antonmartinus72/labpy03/blob/master/img/Pro_1_Output.PNG)

<p align=center>
Anton Martinus A.A.Y
<br>
TI.19.A.1
<br>
https://github.com/antonmartinus72/labpy03