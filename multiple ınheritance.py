"""
bircok sınıftan fonklarını almak için çoklu kalıtım kullanılıyor.

yazılımcı sınıfı hem ögrenci sınıfından hem de calısan sınıfından
fonkları alabilir.

coklu kalıtım cok önerilen bir yöntem değil java da bu yöntem yapılmıyor cok
sadece bilip bulunsun diye yapıldı
yerine önemli fonkları bir class a koyup o classtan her class ın bilgiyi çekmesi amaçlanıyor.

"""
class worker():
    def working(self):
        print("worker is working now")

class student():
    def studying(self):
        print("student is studying now")

class developer(worker,student):
    #def studying(self):
     #   print("developer is studying now")
    pass
# yine overriding yapabiriz.
Selim=developer()
Selim.studying()
Selim.working()



