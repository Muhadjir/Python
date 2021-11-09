'''
Pada Module ini berisi 2 function yang digunakan untuk convert kelvin dan celcius ke fahrenheit atau fahrenheit ke 
celcius dan kelvin. Cara untuk memanggilnya harus import terlebih dahulu lalu memanggil function nya. 
Contoh import:
from packages import fahren_module as fm
Contoh panggil function:
fm.to_fahren(kelv, celc)
fm.from_fahren(fahr)
1. Pada function to_fahren terdapat 2 parameter, yaitu 'kelv' yang digunakan untuk menerima value yang di masukkan user
berupa input suhu kelvin sedangkan 'celc' merupakan value yang dimasukkan user berupa input suhu celcius.
pada function ini terdapat rumus convert dari kelvin dan celcius ke fahrenheit.
2. Pada function from_fahren terdapat 1 parameter, yaitu 'fahr' yang digunakan untuk menerima value yang di masukkan 
user berupa input suhu fahrenheitu yang akan dikonversi ke suhu kelvin dan celcius.
Kedua function yang saya gunakan pada module 'fahren_module' tidak memberikan return value seperti 'ck_module'.
'''
def to_fahren(kelv, celc):
    ktf = (kelv * ( 9 / 5 )) - 459.67
    ctf = (( 9 / 5 ) * celc) + 32
    print('The Formula K to F: Fahrenheit = (Kelvin * 9 / 5) - 459.67 ')
    print(f'Result: {ktf}° Fahrenheit')
    print('')
    print('The Formula C to F: Fahrenheit = ((9 / 5) * Celcius) + 32 ')
    print(f'Result: {ctf}° Fahrenheit')

def from_fahren(fahr):
    celc = (fahr - 32) * 5 / 9
    kelv = (fahr + 459.67) * 5 / 9
    print('The Formula F to K: Kelvin = (Fahrenheit + 459.67)  * 5 / 9')
    print(f'Result: {kelv}° Kelvin')
    print('The Formula F to C: Celcius = (Fahrenheit - 32) * 5 / 9')
    print(f'Result: {celc}° Celcius')