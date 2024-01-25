#Latihan List
list1=['apple','banana','orange']
list2=[1,2,3,4,5,6,7,8,9]
list3=[True,False,False]
list4=['apple',9,True,'banana']

#Mebuat list di dalam list
list5=[list1,list2,list3,list4]  
print(list5)

#Menggabungkan list
List_gabung=[list1 + list2]
print(List_gabung)

#Mengurutkan list
list_angka=[5,3,6,8,1]
list_angka.sort()
print(list_angka)

#Mengcopy list
list_nomor=list_angka.copy()
print(list_nomor)

#Membalikkan urutan list
list_nomor.reverse()
print(list_nomor)

#Menghitung jumlah elemen yang ditanya dalam suatu list
print(list1.count('apple'))

#Latihan mengakses list
fruit_list=['apple','orange','mango','banana','watermelon','cherry','pear','grape']
print(fruit_list[2])    #print indeks ke-2
print(fruit_list[1:4])  #print indeks ke-1 sampai 3, 4 hanya sebagai batas ga ikut keprint
print(fruit_list[-3])   #print indeks ke-3 dari belakang. notesnya di sini adalah kalau dari belakang itungnya gak dari 0, cek aja
print(fruit_list[-4:])  #print indeks ke-4 dari belakang terus lanjut sampai ke akhir

#Mengganti/mengedit indeks ke-5 yaitu cherry menjadi avocado
fruit_list[5]='avocado'
print(fruit_list)

#Membership test   --->>>   di sini kita mau ngecek apakah ada durian di dalam fruit list.
#Hasil yang diprint akan dalam bentuk boolean yaitu true or false
print('durian' in fruit_list)
print('apple' in fruit_list)
print('blueberry' not in fruit_list)

#Menambahkan elemen ke dalam sebuah list yang udah dibuat
fruit_list2=['apple','orange']
fruit_list2.append('watermelon')
print(fruit_list2)
fruit_list2.insert(0,'durian')
print(fruit_list2)

#Menghapus elemen di dalam sebuah list
fruit_list4=['apple','orange','mango','banana','watermelon','cherry','pear','grape']
fruit_list4.remove('apple')
fruit_list4.pop(3)
print(fruit_list4)

fruit_list4.clear()
print(fruit_list4)