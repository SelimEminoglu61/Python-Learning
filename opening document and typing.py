"""
dosyada ikinci virgullu yer modları dır 3 tanedir
ilki ise dosya adı (hepsi fonk cagırırken yazıyor)
Modlar:
w(write)=bu eger dosya bulundugumuz dizinde yoksa onu yaratır ve icine yazmamızı saglar.
eger dosya dizinde varsa onu siler ve aynı adda yeni bos dosya yaratır.
!!!tehlikeli olabilir.
r(read)=olan bır dosyadan okuma yapma ve degişik bilgileri almamızı saglıyor bu mod
a(append)=eger dosya varsa içicdeki bilgileri degistirmemizi saglıyor.
eger yoksa dosya acarak bıseyler yazmamızı saglıyor.


eger istedgimiz yere kayıt yapmak istiyorsak
document =open("C:/User/Selim/Desktop/yazılım.txt","r")
bu sekilde yazarak dosyayının yazılan konuma kaydolmasını saglıyor.bu denemede sadece oldugumuz dizin kullanılacagı için
sadece adını yazıyoruz.

"""


#dosya acmak  yazma modu ile
#document = open("dosya.txt","w")
# a modu ile
document = open("dosya.txt","a")

# içine bişeyler yazmak için
document.write("iyi misin")
# eger farklı bişey yazarak calıstırırsak onu silip yenisinde sadece o kelimeyi yazar.(w ile)
# eger yoksa oluşturup yazıyor varken onceki yazıya dokunmayıp ekleme yapıyor.(a ile)


