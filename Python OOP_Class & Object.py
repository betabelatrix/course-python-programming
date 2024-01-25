#MEMBUAT CLASS
class Cat:
    '''
    ini adalah class untuk membuat object kucing
    melalui class ini kita dapat mendefinisikan nama dan tipe dari kucing yang dibuat
    '''

    spesies='kucing'

    def __init__(self,nama,tipe):
        self.nama = nama
        self.tipe = tipe

    def run(self,speed):
        print(f"{self.nama} berlari dengan {speed}..")

    def play(self):
        print(f'Kucing {self.nama} bermain dengan kucing lainnya')

    def sleep(self,waktu):
        print(f'Kucing {self.nama} tidur di malam hari..')


#MEMBUAT OBJECT
kinako = Cat(nama='Kinako', tipe='Anggora')
kelepon = Cat(nama='Kelepon', tipe="Rumahan")

#print(f'Kinako adalah seekor {kinako.__class__.spesies}')
#print(f'Kelepon adalah seekor {kelepon.__class__.spesies}')

#print(f'{kinako.nama} merupakan kucing jenis {kinako.tipe}')
#print(f'{kelepon.nama} merupakan kucing jenis {kelepon.tipe}')

#kelepon.run('tercepot-cepot')
#kinako.play()

#print(kinako)
#print(kelepon)

#del kinako.tipe
#print(kinako.tipe)
#print(kinako)
kinako.run('kencang')