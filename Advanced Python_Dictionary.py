#Dictionary

fruit_dict = {'nama' : 'pisang',
              'jenis' : 'batu',
              'kode' : 234,
              'harga' : 10000}

#Memanggil/mencetak dictionary
print(fruit_dict)

#Memanggil satu key value tertentu
print(fruit_dict['kode'])

#Mengganti key value tertentu
fruit_dict['jenis'] = 'kepok'
print(fruit_dict)

fruit_dict['harga'] = 20000
print(fruit_dict)

for key,value in fruit_dict.items():
    print(key,value)

for key in fruit_dict.keys():
    print(key,fruit_dict[key])


# BAHAN LATIHAN DICTIONARY
# Buatlah 2 buah dictionary yang memuat informasi 10 murid dan informasi 10 karyawan
dict_murid={'murid1':'Andi',
            'murid2':'Budi',
            'murid3':'Cecep',
            'murid4':'Dodo',
            'murid5':'Erik',
            'murid6':'Faldo',
            'murid7':'Gema',
            'murid8':'Hiro',
            'murid9':'Ivan',
            'murid10':'Jerome'}

dict_karyawan={'karyawan1':'Anto',
               'karyawan2':'Beni',
               'karyawan3':'Chiko',
               'karyawan4':'Daniel',
               'karyawan5':'Egi',
               'karyawan6':'Fatimah',
               'karyawan7':'Gani',
               'karyawan8':'Hasan',
               'karyawan9':'Indah',
               'karyawan10':'Jehan'}

# Lalu cetak data murid dan karyawan yang berada di-index 2 dan 9
print(dict_murid['murid2'],dict_karyawan['karyawan9'])

# Setelah itu cetak semua data yang ada di dictionary tersebut dengan for loop
for key,value in dict_murid.items():
    print(key,value)

for key,value in dict_karyawan.items():
    print(key,value)