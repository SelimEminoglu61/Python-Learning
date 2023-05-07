import _sqlite3
import random
import time
import datetime

"""
burda deger ekleme yaptıgımız için farklı moduller de kullanım var.
time
datetime
random

bu moduller bize gercek zamanı gun ay yıl ve saat dakika saniye cinsinden veriyor.

"""

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
burda öncelikle yenı fonklarla datetime ve time içindekilerler işlemler yapıldı.
strftime sırayı belırlerken fromtimestamp diğer değişkene göre deger ataması yaptı(kesin degil)
randrange belli aralıktan bır deger secti
ve execute fonksıyonunun ikinci parametresi ile values içine nasıl yazılacagı anlatıldı.
values içine kesin deger girmeden bu sekilde değişkenli degerler ataması yapılabilir.

"""

createtable()
# burda ikinci fonk için istedigimiz kadar deger almak istersek
i=0
while(i<5):
    randominsertvalue()
    time.sleep(1) #bu fonk dongunun 1 sn beklemesini saglar.
    i+=1

con.close()