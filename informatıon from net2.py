"""
yine internetten veri çekmek için bu sefer ımdb kullanılıyor.filmlerin tablosu alınıp
film bilgileri alınıcak.

burda html kodları parcalana parcalana en son isim kısmına kadar gelmiş olduk
"""

import requests # indirilecek modul

from bs4 import BeautıfulSoup #indirilecek modul

#url bilgisi bir degişkene atanıyor ve o sayfanın tüm kaynagı ona veriliyor.

imbdurl="http://www.imdb.com/chart_top"

r=requests.get(imbdurl) #burda kaynagı verildi

soup=BeautıfulSoup(r.content,"html.parser")
#duzenli olması için
#gecen kodda burda hata vermişti html parse yazımı sart hata olmaması için

gelen_veri=soup.find_all("table",["class":"chart full-width"])
#burda veriyi atadık ve istediğimiz tablo için ayırt edici bir özelliği sözlük olarak verdik.

print(gelen_veri) # ile bu kodları yazdırabiliriz.

print(gelen_veri[0].contents)
print(len(gelen_veri[0].contents))
#burda ise html daki contentleri ayrı ayrı ele almak var yani table içinden belli kısmı almak
#gelen veri dizisinin ilk elemanı alındı ve onun içindeki contentler ayrıldı
#bundaki tehlike ise contents ?n leri de elemandan sayıp ik eleman onu alabilir
#o yuzden daha iyi ayırma yöntemleri uygulamak gerekir.

film_tablosu=(gelen_veri[0].contents) [len(gelen_veri[0].contents)-2]
#burda sadece filmler için tbody kısmı listede sırası bulundu ve o cağrıldı.

print(film_tablosu)# yazdırmak için

film_tablosu=film_tablosu.find_all("tr")
#bu etiket ile sadece filmlerin oldugu kısmı aldık koyduk içine

for film in film_tablosu:
    filmbaslıkları=film.find_all("td",["class":"tittleColumn"])
    filmismi=filmbaslıkları[0].text
    #burası ile sadece yazı kısımlarını alıyoruz.
    print(filmismi)
    print("**********************")
    #sadece isimler ile ayırmak için yıldız çizgisi
    #\n leri atmak için orda cıkan şu yazılır.
    filmismi=filmismi.replace("\n","")
    #karakter değişimi yapıldı