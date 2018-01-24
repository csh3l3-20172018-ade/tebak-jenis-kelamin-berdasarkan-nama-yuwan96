#untuk menghitung berapa banyak huruf pada gender cowok

def cowok(asma):
    y = 0
    for i in range(len(asma)):
        if asma[i] == 'b':
            y += 1
        if asma[i] == 'B':
            y += 1
        elif asma[i] == 'd':
            y += 1
        if asma[i] == 'D':
            y += 1
        elif asma[i] == 'o':
            y += 1
        elif asma[i] == 'O':
            y += 1
        elif asma[i] == ' ':
            break
    return y


#untuk menghitung berapa banyak huruf pada gender cewek

def cewek(asma):
    y = 0
    for i in range(len(asma)):
        if asma[i] == 't':
            y += 1
        if asma[i] == 'T':
            y += 1
        elif asma[i] == 'l':
            y += 1
        if asma[i] == 'L':
            y += 1
        elif asma[i] == 'u':
            y += 1
        if asma[i] == 'U':
            y += 1
        elif asma[i] == 'a':
            y += 1
        if asma[i] == 'A':
            y += 1
        elif asma[i] == 'e':
            y += 1
        if asma[i] == 'E':
            y += 1
        elif asma[i] == 'i':
            y += 1
        if asma[i] == 'I':
            y += 1
        elif asma[i] == ' ':
            break
    return y

asma = input ("Masukkan nama anda : ")
laki=cowok(asma)
perempuan=cewek(asma)
print(laki,perempuan)

# Untuk Menampilkan output
if (perempuan > laki ):
    print('Jenis Kelamin : Perempuan')
else:
    print('Jenis Kelamin : Laki - Laki')

#untuk hasilnya, saya masukkan nama panggilan saya "Wawan" itu hasilnya perempuan.
#henri : perempuan
#erik : perempuan
#sopin : laki - laki
#bram : laki - laki