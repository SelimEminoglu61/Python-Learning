document =open("dosya.txt","r")

# eger dosya olmasa try except ile dosya bulunamadı yazdırmak
"""
try:
    document =open("C:/Users/Selim/Desktop/dosya.txt","r")
except FileNotFoundError:
    print("dosya bulunamadı")

"""

"""
3 tane fonksiyon var
read()
readline()
readlines()

read():içindeki herseyi almayı saglar.

readline(): en bastaki satırı alır.

readlines():butun satırları alır ama listeye alır.

"""
#print(document.read()) # hepsini gösterdi
#print(document.readline())
#print(document.readline()) # iki tane olursa ilk iki satırı alıyor.
#print(document.readlines())

# burda iki bosluk hem print den hem de yazarken alta gecmek boşluk yaratıyor.(\n ondan yazar son fonkta)


# dosya kapatma işlemi
document.close()