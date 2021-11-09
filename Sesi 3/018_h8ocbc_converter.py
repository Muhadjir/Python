from os import system
def KC_formula(input, type):
    if type == 'ktc':
        print('The Formula K to C: Celcius = Kelvin - 273.15')
        return input - 273.15
    elif type == 'ctk':
        print('The Formula C to K: Kelvin = Celcius + 273.15')
        return input + 273.15

def fahren_formula(type):
    if type == 'tf':
        kelv= int(input('Input Kelvin: '))
        celc= int(input('Input Celcius: '))
        ktf = (kelv * ( 9 / 5 )) - 459.67
        ctf = (( 9 / 5 ) * celc) + 32
        print('The Formula K to F: Fahrenheit = (Kelvin * 9 / 5) - 459.67 ')
        print(f'Result: {ktf}° Fahrenheit')
        print('')
        print('The Formula C to F: Fahrenheit = ((9 / 5) * Celcius) + 32 ')
        print(f'Result: {ctf}° Fahrenheit')

    elif type == 'ff':
        fahr= int(input('Input Fahrenheit: '))
        celc = (fahr - 32) * 5 / 9
        kelv = (fahr + 459.67) * 5 / 9
        print('The Formula F to K: Kelvin = (Fahrenheit + 459.67)  * 5 / 9')
        print(f'Result: {kelv}° Kelvin')
        print('The Formula F to C: Celcius = (Fahrenheit - 32) * 5 / 9')
        print(f'Result: {celc}° Celcius')


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
        kelv= int(input('Input Kelvin: '))
        celc= KC_formula(kelv, 'ktc')
        print(f'Result: {celc}° Celcius')
    elif pilih == 2:
        print('Conversion Menu: Celcius to Kelvin')
        celc= int(input('Input Celcius: '))
        kelv= KC_formula(celc, 'ctk')
        print(f'Result: {kelv}° Kelvin')
    elif pilih == 3:
        print('Conversion Menu: Conversion to Fahrenheit')
        fahren_formula('tf')
    elif pilih == 4:
        print('Conversion Menu: Conversion from Fahrenheit')
        fahren_formula('ff')
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