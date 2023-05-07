"""
veri tabanı:
satır ve sütunlardan oluşan ve bilgiyi depolayan tabloları tutan merkez.
örnek olarak sosyal hesaba girerken kendı bılgılerımızın o sosyal mecranın veri
tabanındaki bilgilerle eşleşmesini kontrol edilmesi gibi
her sütun bır özelliği ifade ediyor

Sqlıte databases internetsiz calışma özelliğine sahipken diğer databases ler internet
yani sunucusuz calışmıyor(örnek MySql).

"""

# Sqlite databases için içeriye aktarmamız gereken modul
import sqlite3
# içindeki tum fonklar kullanılabilir.

#databases oluşturmak için

con =sqlite3.connect("ismi.db")
# burda bır degişkene fonksiyonla databases ismi verilerek oluşturuyoruz.
# eger aynı isimde yoksa dizine oluşturur varsa onla baglantı kurar.
"""
Sqlıte aslında başka bir dildir .Sorgulama dilidir cünkü veritabanında
komutlar sorgulama yaparak calışır.

Başka bir seriden detaylar alınabilir.

burda con degişkeni ile sorguları yapıcaz.
ve databases da cursor ile baglantı yapıcaz (2. adım)

"""
cursor =con.cursor()

def createtable():
    cursor.execute("CREATE TABLE IF NOT EXISTS students (ad TEXT,soyadı TEXT,numara INT,students number INT)")
  #  con.commit() #bu içerdeki sorguların çalışması için gerekli !!!!
  #  con.close() #zorunlu degil ama olması guzeldir.

createtable()

"""
içindeki degerlere bakabilmek için tools gerekli (araç)
onu da internete db browser for Sqlite
diyerek bulup indirebiliriz.(github logosu)

ve tekrar run a basınca cıkan hatayı gidermek için create table ın yanına if not exısts yazılabilir.

cursor.execute("CREATE TABLE students (ad TEXT,soyadı TEXT,numara INT,students number INT)")
NORMALİ YUKARDA
"""
def ınsertvalue():
    cursor.execute("INSERT INTO students VALUES ('selim','eminoglu',765,88.36)")
    con.commit()
    con.close()
#burda tek close yeter yukarda kapatıp acmasın diye ve commıt sonda toplu olarak yapılabilceği için simdi yazdık.
# önceki fonk yukarda cagrıldı.
ınsertvalue()
