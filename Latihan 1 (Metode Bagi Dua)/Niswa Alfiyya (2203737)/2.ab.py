#No. 2
#a. Buatlah modifikasi fungsi ketika kriteria program berhenti adalah sudah mencapai pada iterasi ke-n
#b. Buatlah modifikasi agar user dapat menginputkan fungsi maupun batas akar dan galatnya

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
