"""

kalıtım konusu:
bu konu gercekteki kalıtım gibi sınıflar arasında bırbırının
özelliğini almasını saglar .parent-child ilişkisi denir aynı zamanda
sınıflar arası .sınıflar arasında özellikler alabiliyor.

bir sınıf yapılacak(parent),diğer sınıfa tüm özellikleri aktarılıcak(child)

"""
#normlade boş parantez olup olmaması önemli degil ama kalıtımda gerekli
class worker():
    def __init__(self,name,money,deparment):
        #print("init functıon of working class")
        self.name = name
        self.money = money
        self.deparment = deparment
    def seeminginformation(self):
        print("Name:",self.name)
        print("Money:",self.money)
        print("Deparment:",self.deparment)
    def hikemoney(self,amonut_of_hike):
        print("hiking money...")
        self.money += amonut_of_hike
        print("worker s new money:",self.money)
    def changedeparment(self,new_deparment):
        print("changing deparment...")
        self.deparment = new_deparment


#worker = worker("selim",10000,"yazılım")
#worker.seeminginformation()

#şimdi yapılacak class ta yonetıcı ve butun calısan fonklarını almasını istiyorsak kalıtım kullanıyoruz.
# burda pass deyimi sınıfı doldurmadan gecmeyi sağlar.
# burda kalıtım için parantaz içine yazılır ve artık bütün degerleri alınabilir.
class boss(worker):
    def __init__(self,name,money,deparment,numberofperson):
        #print("init functıon of bossing class")
        super().__init__(name,money,deparment)
        self.numberofperson =numberofperson # ek özellik
    def seeminginformation(self):
        print("seeming boss information...")
        super().seeminginformation()
        print("Number of person:",self.numberofperson)
    def addingperson(self,amountofperson):
        print("adding person....")
        self.numberofperson += amountofperson
   # pass
"""
ve yeni fonklar eklemek mümkün yonetıcı ye yani child class a

yukarda önceki init fonkundan olanları da yazdık ve kalabalık bir kod oldu
ama super() anahtar sözcüğü ile parent olan fonktan o fonksiyonun özelliklerini
alabiliyoruz ve kod kalabalığından kurtulmuş oluyoruz.
"""
# burda şimdi yukardaki gibi değilde kendi yazdıgımız fonku kullanmak istersek
# o zaman pass deyimi kalkar ve overriding olayı yapılır
"""
overriding:bu bizim child class ta kendi fonkumuzu kullanmamızı saglayan bir yöntemdir.
bu yöntem kullanmak istedigimiz fonkun aynı adında bir fonk acarak sonra kendi özelliklerimizi
ekleyerek meydana gelir.
"""
# alttaki ile üstteki aynı sonucu verir.
#boss=boss("yavuz",3000,"araba")
# kendi yazdıgımız init ile 4 parametre gerekiyor.
# aynı zamanda bossing class yazdı.
boss=boss("yavuz",3000,"araba",40)
boss.seeminginformation()
boss.addingperson(60)
boss.seeminginformation()