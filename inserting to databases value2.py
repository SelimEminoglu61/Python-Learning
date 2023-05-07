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
"""
burda yeni bır sorgu var
SELECT sorgusu bu tablodaki degerleri almamızı saglıyor
yazısı:
SELECT *FROM tablename
burda tum tabloyu alır ama istege baglı dusurulebılır.

yeni bir def fonksıyonu ile veri alıp işleme yapılacak
"""
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

takevalue()
con.close()
