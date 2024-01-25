hargalaptop = 200
hargahp = 100

if hargahp <=200:
    print('saya akan mempertimbangkan lagi')
elif hargalaptop >=200:
    print ('saya tidak akan membelinya')


#CATATAN NESTED IF
kelas = 3
score = 95

if kelas > 1:
    if score >= 85:
        print('A')
    elif score >=75:
        print('B')
    else:
        print('Tidak Lulus')
else:
    if score >= 80:
        print('A')
    else:
        print('Tidak Lulus')
