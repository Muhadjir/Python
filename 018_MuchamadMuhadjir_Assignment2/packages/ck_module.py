'''
Pada Module ini berisi 1 function yang digunakan untuk convert kelvin ke celcius atau celcius ke kelvin. Cara untuk
memanggilnya harus import terlebih dahulu lalu memanggil function nya. 
Contoh import:
from packages import ck_module as ckm
Contoh panggil function:
value = ckm.KC_formula(input, type)
pada function KC_formula terdapat 2 parameter, yaitu 'input' yang digunakan untuk menerima value yang di masukkan user
sedangkan 'type' merupakan kondisi yang menentukan apakah dia masuk ke menu kelvin to celcius atau celcius to kelvin.
Dan function yang saya gunakan memberikan return value berupa float.
'''
def KC_formula(input, type):
    if type == 'ktc':
        print('The Formula K to C: Celcius = Kelvin - 273.15')
        return input - 273.15
    elif type == 'ctk':
        print('The Formula C to K: Kelvin = Celcius + 273.15')
        return input + 273.15