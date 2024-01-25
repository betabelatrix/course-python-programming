

class Cat:
    def __init__(self):
       
        self.nama = 'Chiko'
        self.tipe = 'Anggora'
   
    def forward(self):
        print('Kucing berlari..')


class Bird:
    def __init__(self):

        self.nama = 'Tweety'
        self.tipe = 'Nuri'
    
    def forward(self):
        print('Burung terbang..')


# Buat fungsi umum

def melaju (objek):
    objek.forward()

Chiko = Cat(); Tweety = Bird()

melaju(Chiko)
melaju(Tweety)