"""
internetten bilgi cekmek için 2 tane modul kullanıcaz
1.request modulu:netten veriyi bu cekiyor.http moduludur.

2.beautıfulSoup modulu:bu kutuphane ile işlenmesi yapılacak.

html formatında olcagı için az da olsa html bilmek gerekebilir.

pycharmda file kısmında settings bölmesi ve ınterpreter da packet yazılacak
beautıfulsoup4 inecek.

yapılacaklar:
cmd den python arayuzune geliriz(python yazınca sadece)
orda modulleri import ederiz
import requests
from bs4 import BeautifulSoup
şeklinde olucak
r=requests.get("url yazılacak")
yukarda değişkene modulden fonk sonucu atandı sayfanın html formunu alır bu fonk.
r.content ise kaynagı görüntülemek için kullanılır.

güzelleştirme için:
soup =BeautifulSoup(r.content) şeklinde class a yollanır.
böylece soup degişkeni kaynak kodu almış oldu.
print(soup.prettify()) ile de girdileri duzgun sekilde kodu yazdırırız.

soup.find_all("a") bu kaynak kodu içinde belli etiketleri almamızı saglıyor.
bilgi:html de a ile olan etiketler linkler için kullanılıyor.
find all bize bunları liste içinde veriyor bizde bunu bir listeye atıyoruz.

linkler =soup.find_all("a")
sonra for ile gösteririz.
for i in linkler:
    print(i)

sırayla gösteriyor bize bu for dongusu.
eger print de şöyle yazarsak gercek linkleri alır:
print(link.get("href")) sadece gercek linkler

print su sekilde olursa:
print(link.text) olursa hangi yazıya basılırsa hangisine gideri
gösteriyor. bunları yan yana yazınca (gets href ve text) neye basınca ne linkine gideri
daha guzel gösterıyor.
"""