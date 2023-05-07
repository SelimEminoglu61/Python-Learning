import _sqlite3
import random
import time
import datetime

con =_sqlite3.connect("örnek.db")

cursor=con.cursor()

def createtable():
    cursor.execute("CREATE TABLE IF NOT EXISTS  Tablo1 (zaman REAL,tarih TEXT,anahtar_kelime TEXT,deger REAL)")

def randominsertvalue():
# burası rastgele degerleri tabloya eklemek için yapıldı.
    tıme=time.time()
    dates=str(datetime.datetime.fromtimestamp(tıme).strftime("%Y-%m-%d  %H:%M:%S"))
    keyword="Selim Eminoğlu"
    values=random.randrange(0,10)
    cursor.execute("INSERT INTO Tablo1 (zaman,tarih,anahtar_kelime,deger) VALUES(?,?,?,?)",(tıme,dates,keyword,values))
    con.commit()


def takevalue():
    #cursor.execute("SELECT *FROM Tablo1") #buraya * yerine zaman,tarih yazarsak sadece onlar gelir.
    # burda select from için daha da özelleştirmek için where bize belli kısmı almayı saglıyor.
    cursor.execute("SELECT *FROM Tablo1 WHERE deger = 4")
    data =cursor.fetchall() # bu fonk execute den gelen degeri degişkene atamayı saglar.
    #print(type(data)) #tablodam gelen degerlerin ne tipte oldugu gorulur.
    # list biçiminde geldiği görüldü.
    #daha düzgün görmek için
    for i in data:
        print(i)
"""
burda tablodaki degerleri silmeyi ve guncellemeyi yapıcaz
bunun için alttaki fonktan yapılacak sorgular olucak.

"""
def deleteandupdate():
    cursor.execute("SELECT *FROM Tablo1")

    data = cursor.fetchall()
    print("ilk degerler--------------------")

    for i in data:
        print(i)

    cursor.execute("DELETE FROM Tablo1 WHERE deger = 2")
    cursor.execute("SELECT *FROM Tablo1")

    data = cursor.fetchall()
    print("guncel degerler--------------------")

    for i in data:
        print(i)

"""
burda guncelleme için update sorgusunu kullanıyoruz.
bu sorgu ile devamında istedigimiz sütunu belirtiyoruz.
set ile
ve yine where komutu ile hangileri oldugunu soyluyoruz.

ve silme işlemi için delete sorgusu kullanıldı ve ayrıca
bu işlemlerin kaydının kesin olması için sonuna commit yapılması sart yoksa geciçi oluyor.

"""
"""
    cursor.execute("UPDATE Tablo1 SET deger = 61 WHERE deger = 4")

    cursor.execute("SELECT *FROM Tablo1")

    data = cursor.fetchall()
    print("guncel degerler--------------------")

    for i in data:
        print(i)
"""

deleteandupdate()
con.close()
