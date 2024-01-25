
from typing import Any


class Mobil:
    
    def __init__(self, plat):
        self.__plat = plat
        self.__tipe = 'Avanza'
        self.__bensin = 40 #liter

    #Getter
    def lihatMaksimumBensin(self):
        print(f'Maksimum bensin yaitu: {self.__bensin} liter')
        #karna udah diproteksi, cara panggilnya pun jadi seperti panggil
        #method, yaitu tulislah avanza.getMaksimumBensin()


    #Setter
    def aturMaksimumBensin(self,bensin):
        self.__bensin = bensin
        
avanza = Mobil(plat='B 1900 UA') #ini udah jadi satu objek mobil avanza

#print(avanza.plat)
#print(avanza.tipe)
#print(avanza.bensin) 

avanza.__bensin = 30 #misal kita ada modifikasi langsung ada info spt ini
print(avanza.__bensin) #ketika kita print hasilnya akan menjadi 30 (seharusnya 40 kan)

avanza.lihatMaksimumBensin()

avanza.aturMaksimumBensin(100)

avanza.lihatMaksimumBensin()
