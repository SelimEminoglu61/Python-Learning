"""

dosyalarda veri ekleme konusu bunlar:
-basına
-sonuna
-ve ortasında herhangi bir yere ekleme dir.

"""
#sonuna eklemek
#with open("dosya.txt","a") as document:
 #   document.write("Paris Saint Germain:Neymar")
# a modu ile yazınca otomatik sonuna ekliyor.

# basına eklemek için
# burda butun veriyi okuyup sonra string oldugu için yeni verimizle toplayabılırız
# bunun için daha fazla modlar var hem okuma hem yazma yapabılmemız için
"""
with open("dosya.txt","r+") as document: # burdaki r+ hem okuma hem yazma saglar.ve dosya yoksa yenı dosya yapmaz.
    data=document.read()                  # w+ ise aynıdır hem  okuma hem yazma yapar ama dosya yoksa dosya acar.
                                         # a+ ise hem okuma hem degisiklik için izin saglar dosya yoksa acar.
    document.seek(0)
    data="Bayern Munih:Robert Lewandowski\n" + data
    document.write(data) """
"""
burda ortaya eklemek için yeni bir fonksıyon var listelerle ilgili olarak
örnek:
liste = [1,2,3,4,5]
burda 1. indekse 15 yazalım.
liste.insert(hangi indeks,ne eklenıcek)

ile yapılabılır.
"""
#liste = [1,2,3,4,5]
#liste.insert(1,15)
#print(liste)
with open("dosya.txt","r+") as document:
    data =document.readlines() # her satırı liste yapmak için
    data.insert(1,"Trabzonspor:Jose Sosa\n")
    document.seek(0)
    document.writelines(data)
    # writelines listeyi yazmak için