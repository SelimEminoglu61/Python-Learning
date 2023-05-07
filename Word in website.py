"""
bir websitede yer alan bir kelimenin kaç kere tekrarlandığını bulmamızı sağlıyacak kod

burda Aziz Sancar ın nobel ödülü aldıgını söyleyen ntv sayfasının yapılmıştır.

-ilk olarak sayfa kaynagı görüntülenir.

bilgi:burda html de 'p' etiketi olanlar paragraf açmaya yarar onlardan yaralanıcaz.

yine aynı fonklar kullanılacak.

lower fonku harfleri küçük yapıyor ki büyük küçük ayrımı olmadan her istediğimizi alsın
split ise aradaki boşluklara bakarak kelimeleri ayıracak.
split büyük bir yazıyı liste şeklinde veriyor.
"""

import request
from bs4 import BeautıfulSoup
import operator

def sozlukolustur(tumkelimeler):
    kelimesayısı=()

    for kelime in tumkelimeler:
        if kelime in kelimesayısı:
            kelimesayısı[kelime]+=1
        else:
            kelimesayısı[kelime]=1
    return kelimesayısı



def sembolleritemizle(tumkelimeler):
    sembolsuzkelimeler=[]
    semboller="arada olan bozuk semboller ve yandaki klavyede yok ascı den sayısı ile"+chr(775)
    for kelime in tumkelimeler:
        for sembol in semboller:
            if sembol in kelime:
                kelime =kelime.replace(sembol,"")
                #burda o sembol ile boş karakter yer değiştiriyor.
        if (len(kelime)>0):
            sembolsuzkelimeler.append(kelime)
    return sembolsuzkelimeler


url1="adres yazılacak................."

tumkelimeler=[]

r= requests.get(url1)

soup=BeautıfulSoup(r.content,"html.parser")

for kelimegrupları in soup.find_all("p"):
    icerik=kelimegrupları.text
    kelimeler = icerik.lower().split()

    for kelime in kelimeler:
        tumkelimeler.append(kelime)
        #print(kelime)
# buraya kadar her bir kelimeyi liste yapıp bastırdık.
# burdn sonrası bozuk gelen kelimeleri duzeltmekle ilgili olucak.
"""
-sembolleri temizle fonku yapılıyor.

"""
tumkelimeler=sembolleritemizle(tumkelimeler)
kelimesayısı=sozlukolustur(tumkelimeler)

for anahtar,deger in sorted(kelimesayısı.items(),key= operator.itemgetter(0)):
    print(anahtar,deger)

"""
for kelime in tumkelimeler:
    print(kelime)
   """
# burda yine sembol gözükür yukardaki print iptal edelim:)
# simdi duzenli liste elde ettik.
# sırada kelime tekrarlarına bakıcaz.
"""
-sozlukolustur fonku yazılıyor.
-operator kütüphanesi eklendi ve onunla ilgili fonk kullanıldı.
-itemgetter iki pararmetre alabilirdi 0 anahtar için 1 deger için hangisi yazılırsa ona göre sıralar.
-items hepsini almak için
-sorted sıralamak için
sözlükler konusunda görüldü.
"""

