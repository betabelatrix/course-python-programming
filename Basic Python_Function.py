#Fungsi Non Parameter
def halo_python():
    var =f'Halo python, halo dunia!'
    print(var)

halo_python()


#Fungsi Parameter
def selamat_datang(nama):
    var=f'Halo {nama}, welcome!'
    print(var)

selamat_datang('Aldwin')

#Fungsi Parameter
def selamat_datang(nama, asal):
    var =f'Halo {nama} dari {asal}, welcome!'  #jangan lupa pakai huruf (f) krn kita mau menggunakan tanda kurung kurawa utk bikin parameter
    print(var)

selamat_datang('Beta', 'San Francisco')
selamat_datang(nama='Beta', asal='Depok')

#Fungsi parameter dengan jumlah tidak menentu
def selamat_datang(*daftar_nama):    #parameter diawali dengan tanda bintang
    var = 'Halo '                    #di sini gapapa gapake huruf (f) gitu di depan halo krn kita cuma mau tulisan/string aja
    for nama in daftar_nama:
        var+= nama + ', '
    var += 'welcome!'
    print(var)

selamat_datang('Alka, Alika, Gianna')



#Fungsi Anonim menggunakan lambda
double = lambda x: x*2   #Kita buat contoh di sini adalah perkalian, nilai X dikali 2
print (double(5))
print (double(10))


#Menggunakan Docstring
def selamat_datang(nama):             #di bawah ini ditambahkan komen dengan cara menggunakan tanda petik 3x
    '''
    ini adalah fungsi untuk menyapa
    nama yang telah disebutkan
    '''
    var=f'Halo {nama}, welcome!'
    print(var)

selamat_datang('Aldwin')
print(selamat_datang.__doc__)   #cara panggil docstring


#Scope & Return

x = 22081995
y = 20111995

def operasi(a,b,c):
    op1 = a + b
    op2 = op1 // c
    op3 = op2 * 2

    print('nilai a di dalam function adalah', a)
    print('nilai b di dalam function adalah', b)
    print('nilai c di dalam function adalah', c)
    
    print('tanggal lahir Beta adalah', x)
    print('tanggal lahir Aldwin adalah', y)

    return op3
hasil = operasi(a=10,b=5,c=3)
print(hasil)

print(x)
print(y)



#Bahan Latihan Function
def cek_modulus(angka1,angka2):
    mod = angka1*angka2

    return mod
hasil = cek_modulus(angka1=12,angka2=8)
print(hasil)
