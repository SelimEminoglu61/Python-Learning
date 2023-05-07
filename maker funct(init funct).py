"""
yapıcı fonksiyonlar sınıflarda oluşan nesnelerin farklı özelliğe
sahip olmasını saglıyor.

init fonksıyonu nesnelere farklı özellikler vermeyı saglıyor.

burdaki self için:
bu self nesnenin kendisini ifade ediyor onun için
sadce self olan fonka parametre yollamak gerekmiyor.
ve self aracılığla içerde nesne adına işlem saglanıyor.


class içinde özel init fonku def ile cagrılır ve
normalde ortak ozellikler içine yazılır.
ama içine self. olmadan yazarsak normal degişken gibi algılanacagı için
hata verir.class degişkeni oldugunu self ile ifade ederiz.

sonrasında değişim için fonka parametre yollamak gerekir(self kısmı)
"""

class Enemy:
    def __init__(self,isim="dusman",kalancan=1000,saldırıgucu=220,kalanmermi=50):
        self.name = isim
        self.healhty = kalancan
        self.power_of_attack = saldırıgucu
        self.numberbullet = kalanmermi
    def print(self):
        print("name: ",self.name)
        print("healhty: ",self.healhty)
        print("power of attack: ",self.power_of_attack)
        print("number of bullets: ",self.numberbullet)
# burda dusman classının içine init fonku ile farklı parametreler alabiliyoruz.
# nesne yapılırken degerleri parametre olarak yollanır.
dusman1 =  Enemy("Selim",5000,750,500)
dusman2 = Enemy("Yavuz",2500,250,200)
#burda parametre yollamazsak hata verir.bunu engellemek için varsayılan degerler
#kullanılır.
dusman3 = Enemy()
print("dusman1 ------------------")
dusman1.print()
print("dusman2 ------------------")
dusman2.print()
print("dusman3 ------------------")
dusman3.print()


# burda ne kadar nesne yapılırsa yapılsın hepsinin özelliği aynı olucak.
# bunu degiştirmek için class ta init fonku kullanılır.
#dusman1 =  Enemy()
#dusman2 = Enemy()
#print("dusman1 ------------------")
#dusman1.print()
#print("dusman2 ------------------")
#dusman2.print()

