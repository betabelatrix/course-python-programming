class ValueTooSmallError(Exception):
    pass
class ValueTooLargeError(Exception):
    pass


Number=10
while True:
    try:
        i_num=int(input('Masukkan angka:'))
        if i_num<Number:
            raise ValueTooSmallError
        elif i_num>Number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print('Angka yang kamu tebak terlalu kecil, coba lagi!')
        print()
    except ValueTooLargeError:
        print('Angka yang kamu tebak terlalu besar, coba lagi!')
        print()
print('Betul!')