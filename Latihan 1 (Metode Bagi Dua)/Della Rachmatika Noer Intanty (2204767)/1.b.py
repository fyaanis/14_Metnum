#No 1
#Buatlah sebuah fungsi penyelesaian yang tepat baik dengan menggunakan metode Bagi Dua ketika
#b. f(x) = e^x - x

import numpy as np #panggil library
def my_bisection(f, a, b, e):
  if np.sign(f(a)) == np.sign(f(b)):
    raise Exception('Tidak ada akar pada interval a dan b')
  m = (a + b)/2
  if np.abs(f(m)) < e:
    return m
  elif np.sign(f(a)) == np.sign(f(m)):
    return my_bisection(f, m, b, e)
  elif np.sign(f(b)) == np.sign(f(m)):
    return my_bisection(f, a, m, e)

#pada library numpy np.e adalah bilangan euler yaitu bilangan yang bernilai 2,71828
f = lambda x:  np.e**x - x

#fungsi 'try' dan 'except' untuk menangani pengecualian yang mungkin muncul saat iterasi maksimum tercapai.
try:
    r1 = my_bisection(f, -1, 1, 0.1)
    print("r1 =", r1)
    print("f(r1) =", f(r1))
except Exception as exc:
    print(exc)
