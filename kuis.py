# # Kuis Coding: Ekspresi
# """
# TODO:
# Anda diharuskan membuat program diskon untuk sebuah toko belanja dengan ketentuan berikut.
# - Jika pelanggan berbelanja lebih dari 500.000 ribu, mereka akan mendapat potongan harga 10%.
# - Seorang pelanggan bernama Dico telah berbelanja senilai 750.000 ribu.
# - Buat operasi aritmetika untuk menghitung total harga belanja Dico setelah mendapatkan diskon, 
#   dan simpan dalam variabel bernama "total_harga".

# Tips:
# - Ingat yang dicari adalah total harga belanja setelah diskon, bukan besaran potongan harga.
# """
# # Jangan ubah kode ini
# dico = 750000 
# # TODO: Silakan buat kode Anda di bawah ini.
# # check = 750000 * 0.10
# # total_harga = dico - check
# # alternative solution
# # total_harga = dico - (dico * 0.10)
# total_harga = dico * .9
# print(total_harga)

# Kuis Loop
# """
# TODO:
# Buatlah sebuah variabel bertipe list bernama "evenNumber" dengan ketentuan:
# - variabel tersebut menampung bilangan genap dari 0 hingga 500 (ingat 0 dan 500 termasuk).

# Tips:
# Anda bisa menggunakan loop dan if atau list comprehension untuk memudahkan.
# """

# # TODO: Silakan buat kode Anda di bawah ini.
# evenNumber = []
# for n in range(501):
#   if n % 2  == 0:
#     evenNumber.append(n)
    
# print(evenNumber)

# Kuis Coding: Array atau List

"""
TODO:
Sebuah variabel array diberikan dengan ketentuan berikut.
- Variabel array bernama "var_array" dengan nilai dari 0 hingga 100.
- Hitung nilai rata-rata dari elemen array tersebut.
- Simpan hasil perhitungan dalam variabel bernama "result".

Tips:
- Rumus menghitung rata-rata adalah jumlah seluruh elemen (len) dibagi banyaknya elemen.
- Gunakan percabangan dan perulangan untuk mempermudah, 
  Anda tidak diperbolehkan memberikan nilai secara langsung.
"""
# Jangan ubah kode ini
var_array = [i for i in range(101)]

# TODO: Silakan buat kode Anda di bawah ini.
result = []

for i in var_array:
    result.append(i+ len(i))


print(result)