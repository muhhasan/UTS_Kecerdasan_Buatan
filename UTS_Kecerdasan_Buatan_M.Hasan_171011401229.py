#Nama : Muhammad Hasan
#NIM : 171011401229
#LOOPING

#Ini Contoh Looping di Python secara umum dari list array
print("Ini Contoh Looping di Python secara umum dari list array")
nama_motor = ["suzuki", "yamaha", "kawasaki"]
for x in nama_motor:
    print(x)

print("\n")

#Fungsi range() mengembalikan urutan angka, mulai dari 0 secara default, dan bertambah 1 (secara default), dan berakhir pada nomor tertentu
print("Ini Contoh Hasil Looping dengan Fungsi Range()")
for x in range(4):
    print

print("\n")

#Fungsi range() default ke 0 sebagai nilai awal , namun dimungkinkan untuk menentukan nilai awal dengan menambahkan parameter: range(2, 6),yang berarti nilai dari 2 hingga 6 (tetapi tidak termasuk 6):
print("Ini Contoh Hasil Looping dengan Fungsi Range() dengan 2 parameter")
for x in range(2, 6):
    print(x)

print("\n")

#Fungsi range() default untuk meningkatkan urutan dengan 1, namun dimungkinkan untuk menentukan nilai kenaikan dengan menambahkan parameter ketiga: range(2, 30, 3):
print("Ini Contoh Hasil Looping dengan Fungsi Range() dengan 3 parameter")
for x in range(2, 30, 3):
    print(x)

print("\n")

#Loop bersarang
#Looping bersarang adalah loop di dalam loop. "Loop dalam" akan dieksekusi satu kali untuk setiap iterasi "Loop luar":
print("Ini Contoh Hasil Looping bersarang")
adj = ["yellow", "big", "tasty"]
fruit = ["bannana", "mango", "grape"]

for x in adj:
    for y in fruit:
        print(x, y)

print("\n")

#Ini adalah cara looping dan akan berhenti pada kondisi tertentu, perulangan akan berhenti ketika variabel x berisi kata "realme"
print("Ini Contoh Hasil Looping dengan break")
hp = ["samsung", "realme", "sony"]
for x in hp:
    print(x)
    if x == "realme"
    break