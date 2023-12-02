# # greeting = 'Helo world'
# # print(greeting)
# # addition = 2+2
# # result = addition -1
# # print(result)

# # input
# greeting = input('Masukan nama Anda: ')
# print(greeting)
 
# """
# Output:
# Masukan nama Anda: Perseus Evans
# Perseus Evans
# """

## Data typing checking functions
# age = 19
# salary = 5000000.0
# print(type(age))
# print(type(salary))

## python as dynamic typing checking functions
# x = 10
# print(type(x))
# x = "10"
# print(type(x))

## type data at python
# string  
# number
# bolean 

# Tipe Data Primitif
# number float(bulat/decimal) and integer(bulat)
# x = 6
# print(type(x))

# x = 6.0
# print(type(x))

# x = 1+2j
# print(type(x))

# var = 10
# print(var)
# print(id(var))
# var = 11
# print(var)
# print(id(var))

# bolean
# x = True
# print(type(x))

# x = False
# print(type(x))

# string
# x = """ lorem ipsum dolor sit amet
# consetetur adipiscing elit
# lorem ipsum dolor sit am
# """
# print(x)

# acces string by index
x = 'Dicoding'
print(x[2:])

# Transformasi Angka, Karakter, dan String
# upper() => like toUppercase js
# kata = 'dcoding'
# kata = kata.upper()
# print(kata)
# lower() => like tolowercase js 
# kata = 'DICODING'
# kata = kata.lower()
# print(kata)
# rstrip() delete white space in end
print("Dicoding          ".rstrip())
# lstrip() delete awal space 
print("           Dicoding".lstrip())
# strip() delete awal and end space & delete string
kata = 'CodeCodetesCodeCode'
print(kata.strip('Code'))  
print("         Dicoding          ".strip())
# read doc!
# startswith() check awalan return boleaan
# endswith() check end return bolean
# join() merge 
# split() memisahkan
# replace() replace string
# isupper() check string uppercase or not
# islower() check string lowercase or not
# isalpha() check string is alphabet or not
# isalnum()check string is alphabet have number return true
# isdecimal() return true if just number
# isspace() return true if just have whitespace
# istitle() return true if  just have capital letter
# zfill() add 0 in beginning string 
# rjust() Metode rjust() berguna untuk merapikan pencetakan teks. 
# ljust() antonim rjust method
# center() string to center

# string literals
# \' Single quote
# \" Double quote
# \t Tab
# \n Newline (line break)
# \\ Backslash

# raw string 
# print(r'Dicoding\tIndonesia')

# """
# Output:
# Dicoding\tIndonesia

# """


# Operasi pada List, Set, dan String
# len() => check length
# min() dan max() => min and max value check
# count check object beberapa kali muncul
# In dan Not In => check value has in variabel or not

# give value mutiple variable => like array destructring
# data = ['shirt', 'white', 'L', 'red']
# apparel, color, size, background = data

# Sort 
# car = ["avansa", 'brio', 'cherry']
# car.sort(reverse= True)

# print(car)

# # expresion
# Ekspresi aritmetika: jenis ekspresi yang memiliki operan bertipe numerik dan menghasilkan numerik.
# Ekspresi relasional: jenis ekspresi yang memiliki operan bertipe numerik dan menghasilkan nilai boolean/logika.
# Ekspresi logika: jenis ekspresi yang memiliki operan bertipe boolean/logika dan menghasilkan nilai boolean/logika.
# print(2+2)
# print(3<10)
# print(True or False)

# """
# Output:
# 4
# True
# True
# """
# aritmatika operator
# Penjumlahan (+)

# Menambahkan nilai dari kedua operan.

# x + y = 16

# Pengurangan (-)

# Mengurangi nilai dari kedua operan.

# x - y = 6

# Perkalian (*)

# Mengalikan nilai dari kedua operan.

# x * y = 55

# Pembagian Bulat (//)

# Membagi nilai dari kedua operan. Jika operan adalah integer, hasil operasi adalah bilangan bulat.

# x // y = 2

# Pembagian Riil (/)

# Membagi nilai dari kedua operan. Jika operan adalah float, hasil operasi adalah bilangan riil.

# x / y = 2.2

# Modulo (%)

# Sisa hasil pembagian nilai dari dua operan.

# x % y = 1

# Pangkat (**)

# Memangkatkan nilai dari dua operan.

# x ** y = 161051

# Operator Relasional
# ==, != , >, <, >=, <= like js operator

# assignment operator
# +=
# x = 11
# x += 5
# print(x)

# # -=
# x = 11
# x -= 5
# print(x)

# # *=
# x = 11
# x *= 5
# print(x)

# # /=
# x = 11
# x /= 5
# print(x)

# #%=
# x = 11
# x%= 5
# print(x)


# """
# Output:
# 16
# 6
# 55
# 2.2
# 1
# """

# skensuial action
# print("Selamat datang dalam program Python!\n")
# print("Silakan masukkan data diri Anda.")
# nama = input("Masukkan nama Anda: ")
# tahun_lahir = input("Masukkan tahun lahir Anda: ")
# umur = 2023 - int(tahun_lahir)
 
# print(f"Selamat datang {nama} dalam program Python, per 2023 umur Anda adalah {umur} tahun.\n")
# print("Terima kasih telah menggunakan program Python!")
 
#  kesimpulan python as intepretier programming and menerapkan case sensitive serta sensitive terhadap whitespace

# control flow
# conditional if else & elif
# ketersediaan = "Daging bebekk"

# if ketersediaan == "Daging ayam":
#     print("Ibu membeli dan memasak ayam")
# elif ketersediaan == "Daging bebekk":
#     print("ibu masak bebek ")
# else:
#     print("Ibu membeli dan memasak tempe")

# Tenary Operator
# lulus = True
# # tenary tuples 
# kelulusan = ("Tidak lulus yaa", "lulus nak")[lulus]
# # print("selamat") if lulus else print("perbaiki")
# print(kelulusan)

# loop
# data = [1,2,3,4] 
# for i in data:
#     print(i) 
# use range & range(start, stop,step)
# for i in range(5):
#     print(i) 
# for i in range(1, 11, 2):
#     print(i) 
# while loop
# counter = 1
# while counter <= 5:
#     print(counter)
#     counter += 1    # Increment
# nested for
# for i in range(1, 3):
#     for j in range(1, 3):
#         print(i,j)
# break
# for i in range(2):  # Perulangan tingkat pertama
#     print("Perulangan luar:", i)
#     for j in range(10):  # Perulangan tingkat kedua
#         print("Perulangan dalam:", j)
#         if j == 1:
#             break  # Menghentikan perulangan dalam jika j = 1
# continu
# for huruf in 'Dico ding':
#     if huruf == ' ':
#         continue
#     print('Huruf saat ini: {}'.format(huruf))
# for with else
# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     if num == 6:
#         print("Angka ditemukan! Program berhenti!")
#         break
# else:
#     print("Angka tidak ditemukan.")
# while with else
# count = 0

# while count < 3:
#     print("Dicoding Indonesia")
#     count += 1
# else:
#     print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")
# Pass
# x = 10

# if x > 5:
#     pass
# else:
#     print("Nilai x tidak memenuhi kondisi")
# List Comprehension like array push in js
# angka = [1, 2, 3, 4]
# pangkat = []
# for n in angka:
#   if pangkat % 2:
#     print(pangkat)
# alternative method
# angka = [1, 2, 3, 4]
# pangkat = [n**2 for n in angka]
# print(pangkat)


# Erro handling use
# try:
# except:
# z=0
# try:
#     print(1/z)
# except ZeroDivisionError:
#     print("Anda tidak bisa membagi angka dengan nilai nol.")
# var_dict = {"rata_rata": "1.0"}

# try:
#     print(f"rata-rata adalah {var_dict['rata_rata']}")
# except KeyError:
#     print("Key tidak ditemukan.")
# except TypeError:
#     print("Anda tidak bisa membagi nilai dengan tipe data string")
# else:
#     print("Kode ini dieksekusi jika tidak ada exception.")
# finally:
#     print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")

# Raise Exception
# var = -1
# if var < 0:
#     raise ValueError("Bilangan negatif tidak diperbolehkan")
# else:
#     for i in range(var):
#         print(i+1)
    

# Fundamental array 
# x = [1, 2, 3, 4, 5]
# print(x)
# use library
# import array
# x = array.array('i', [1,2,3,4,5])
# print(x)
# print(type(x))

# implementasi array 
# Mendefinisikan Nilai Default
# var_arr = [0 for i in range(10)]
# print(var_arr)
# change value from default value
# var_arr = [0 for i in range(10)]

# for i in range(10):
#     var_arr[i] = i

# print(var_arr)

# akses array element
# var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# print(var_arr[0])

# skensuial array
# var_arr = [1, 2, 3, 4, 5]

# for i in range(len(var_arr)):
#     current_element = var_arr[i]
#     next_index = i+1
    
#     if next_index < len(var_arr):
#         next_element = var_arr[next_index]
#     else:
#         next_element = None
        
#     print(f"Current element: {current_element}, next elements: {next_element}")


# Latihan search big value with two pointer algoritma 
# var_arr = [1,7,2,89,3]
# left_pointer = var_arr[0]

# for i in range(1, len(var_arr)):
#     right_pointer = var_arr[i]
#     if right_pointer > left_pointer:
#         left_pointer = right_pointer

# print(left_pointer)
