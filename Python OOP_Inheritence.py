
# class parent

class Animal:
    def __init__(self):
        self.tipe = 'mamalia'
        self.kecepatan = 'cepat'

    def grow(self):
        print('Mamalia ini bertumbuh')

# class child

class Cat(Animal):
    def __init__(self, nama, tipe):
       
        super().__init__()

        self.nama=nama
        self.tipe=tipe
   
    def run(self):
        print(f'Kucing {self.nama} berlari..')

# objek
kinako=Cat (nama='Kinako', tipe='Anggora')
chiko=Cat (nama='Chiko', tipe='Persia')


# class child lainnya

class Dog(Animal):
    def __init__(self, nama, tipe):
        super().__init__()

        self.nama=nama
        self.tipe=tipe
    
    def eat(self):
        print(f'Anjing {self.nama} sedang makan..')

              
#objek
heli=Dog (nama='Heli', tipe='Husky')
rongrong=Dog (nama='Rongrong', tipe='Labrador')
              

# Coba run fungsi di atas
                            

print(kinako.kecepatan)
print(kinako.tipe)

kinako.run()
chiko.run()

print(heli.kecepatan)
print(heli.tipe)

rongrong.eat()