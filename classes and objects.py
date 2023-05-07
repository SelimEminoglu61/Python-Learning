"""
nesne tabanlı programlama :
bu konu temel konulardan biri programlamayı daha efektif hale getiren
bir durum.burda temel mantık nesne oluşturup bunlara ayırt edici özellikler
yuklemek sınıflar oluşturup özellikler vermek daha basit kod yazmak gibi temellerden
oluşuyor nesne tabanlı programlama(object-based programming)

örnek:
insanların sınıf olabilir herkesin ortak özelliklerinden ötürü
ama insanların kendi içinde barındırdıgı farklı özellikler sınıflardaki nesneleri temsil
edebilir.


önce sınıf oluşturma içinde genel özellik ve fonksiyon kullanımı
sonrasında o sınıftan nesne yapımı yazılacak.
"""
class enemy:
    healhty= 4 # burda sınıfın genel özelliği verildi.
    def attack(self):
        print("we make attack!!!!!")
        self.healhty -=1
    def doesıtlıve(self):
        if (self.healhty >= 0):
            print("we live")
        else:
            print("they died")
"""
burda fonksiyonlar ile işlemler yapıldı.burdaki self bizim fonksiyon içinde genel özelliğe ulaşmamızı saglıyor.
ve deger alırken kullanılıyor.

altta nesne oluşturuluyor dusman sınıfından
"""
enemy1 = enemy()
enemy2 = enemy()
# burda ise nesnenın sınıfı içindeki fonkların kullanımı gösteriliyor.
#aynı sistem listede vardı (liste.append gibi)
enemy1.attack()
enemy1.attack()
enemy1.doesıtlıve()