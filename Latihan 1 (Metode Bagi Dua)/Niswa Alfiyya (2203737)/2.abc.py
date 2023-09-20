#No. 2
#a. Buatlah modifikasi fungsi ketika kriteria program berhenti adalah sudah mencapai pada iterasi ke-n
#b. Buatlah modifikasi agar user dapat menginputkan fungsi maupun batas akar dan galatnya
#c. Buatlah modifikasi agar akarnya dapat ditampilkan dalam bentuk grafik

import numpy as np #memanggil library numpy

#mencari akar dari fungsi yang sudah diinput sesuai dengan iterasi yang ditentukan
def my_bisection(f, a, b, e, max_iter):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception('Tidak ada akar pada interval a dan b')
    
    for i in range(max_iter):
        m = (a + b) / 2
        if np.abs(f(m)) < e:
            return m
        elif np.sign(f(a)) == np.sign(f(m)):
            a = m
        elif np.sign(f(b)) == np.sign(f(m)):
            b = m
        print(f'Iterasi {i + 1}: a = {a}, b = {b}, m = {m}, f(m) = {f(m)}')
    
    raise Exception('Iterasi maksimum telah tercapai')

# Input dari pengguna (fungsi, jumlah iterasi, interval, toleransi galat)
f_expr = input("Masukkan ekspresi fungsi f(x): ")
max_iter = int(input("Masukkan iterasi maksimal: "))
a = float(input("Masukkan batas interval pertama: "))
b = float(input("Masukkan batas interval kedua: "))
e = float(input("Masukkan besar galat: "))

# memproses fungsi yang diinput pengguna (merubah string yang diinput menjadi fungsi matematika)
f = lambda x: eval(f_expr)

#menjalankan fungsi pencarian akar
try:
    r1 = my_bisection(f, a, b, e, max_iter)
except Exception as exc:
    print(exc)

import numpy as np
import matplotlib.pyplot as plt

# Membuat array x dengan nilai dari a hingga b
x = np.linspace(a, b, 400)

try:
    # Mengevaluasi fungsi yang dimasukkan oleh pengguna untuk setiap nilai x
    y = eval(f_expr)

    # Mencari potongan akar (y=0)
    roots_x = x[np.where(np.diff(np.sign(y)))[0]]
    roots_y = [0] * len(roots_x)

    # Membuat plot
    plt.plot(x, y, '-')
    plt.scatter(roots_x, roots_y, color='red', label='Potongan Akar')
    plt.title(f'Grafik fungsi f(x) = {f_expr}')
    plt.axhline(0, color='grey', linestyle='--') # Menambahkan garis horizontal pada y dengan warna merah dan garis putus-putus
    plt.axvline(0, color='grey', linestyle='--') # Menambahkan garis vertikal pada akar dengan warna hijau dan garis putus-putus
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()

    # Menampilkan grafik
    plt.show()

except NameError:
    print("Fungsi yang dimasukkan tidak valid.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")

