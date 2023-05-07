"""
burda dosyadaki veriyi belli bir yere kadar okuma gösterilecek.

!!!eger cok buyuk dosyalı veya fazla dosya bulunan bır programda yazarsak
kendi elimizle dosyaların hepsini kapatmayı unutmamak için python önerdiği daha ıyı bır
yontem vardır

with open("dosya.txt","r") as document:
    print(document.read())
"""
# istedigimiz byte a gitme için
with open("dosya.txt","r") as document:  # önemli !!!
    document.seek(20)
    #print(document.read())
    #document.seek(40) # burdaki satırda fonksiyon yine dosya basından alır ustune 40 ekleyip 60 ileri gitmez.
    # print(document.read())
# read fonksıyonu içinde kac tane karakter okumak istedigimizi gönderebiliriz.
    print(document.read(32)) # sadece 32 tane karakter alır