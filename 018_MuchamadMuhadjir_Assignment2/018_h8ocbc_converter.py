from os import system
from packages import ck_module as ckm
from packages import fahren_module as fm

'''
import system from package os digunakan untuk memanggil fungsi 'cls' yang berguna untuk menghapus tampilan terminal
import ck_module digunakan untuk memanggil function KC_formula dari modul 'ck_module' di package 'packages' 
import ck_module digunakan untuk memanggil function to_fahren dan from_fahren dari modul 'fahren_module' di package 'packages' 

Pada Assignment 2 saya menggunakan program menu untuk pemilihan function mana yang akan dikerjakan, dan menu tersebut
terdapat pilihan untuk mengulang atau tidak. Disini saya menggunakan while untuk looping menu nya. Dan if elif untuk
pemilihan menu. Tidak lupa juga untuk pemilihan nya saya menggunakan user input dari terminal. Setelah itu 
tinggal memanggil function yang berada pada packages yang telah disediakan sesuai dengan pilihan dari user input.
'''

loop = True
while(loop):
    system('cls')
    print('Assignment 2 Python')
    print('Nama : Muchamad Muhadjir')
    print('Kode : FSDO001ONL018')
    print('Conversion Menu:')
    print('1. Kelvin to Celcius')
    print('2. Celcius to Kelvin ')
    print('3. Conversion to Fahrenheit')
    print('4. Conversion from Fahrenheit')
    print('5. About Me')
    pilih = int(input('Choose Menu (ONLY NUMBER): '))
    if pilih == 1:
        print('Conversion Menu: Kelvin to Celcius')
        kelv= float(input('Input Kelvin: '))
        celc= ckm.KC_formula(kelv, 'ktc')
        print(f'Result: {celc}° Celcius')
    elif pilih == 2:
        print('Conversion Menu: Celcius to Kelvin')
        celc= float(input('Input Celcius: '))
        kelv= ckm.KC_formula(celc, 'ctk')
        print(f'Result: {kelv}° Kelvin')
    elif pilih == 3:
        print('Conversion Menu: Conversion to Fahrenheit')
        kelv= float(input('Input Kelvin: '))
        celc= float(input('Input Celcius: '))
        fm.to_fahren(kelv, celc)
    elif pilih == 4:
        print('Conversion Menu: Conversion from Fahrenheit')
        fahr= float(input('Input Fahrenheit: '))
        fm.from_fahren(fahr)
    elif pilih == 5:
        print('About Me')
        print('Hallo My Name is Muchamad Muhadjir')
        print('My Code is FSDO001ONL018')
        print('I\'m from Surabaya')
        print('I\'m participant at bootcamp OCBC NISP with Hacktiv8')
    else:
        print('I\'m Sorry, choose right menu!')
    
    if(input('Back to Menu [y/n]?') == 'y'):
        loop=True
    else:
        system('cls')
        loop=False