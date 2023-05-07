import sqlite3 as sp

class Database:
    def __init__(self,Username,Surname,Birthdate,Email:str,Password):
        self.Username=Username
        self.Surname=Surname
        self.Birthdate=Birthdate
        self.Password=Password
        self.Email=Email
        self.createdatabase()

    def createdatabase(self):
        self.sbt1=sp.connect("EmailApp.sqlite")
        self.cursor=self.sbt1.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS User_list (Username,Surname,Birthdate,Email,Password)")

    def adddatabase(self):
        self.__deneme=('g','m','a','i','l','.','c','o','m')
        self.__number1=0
        self.__find=0
        for i in range(len(self.Email)):
            self.__number1+=1
            if(tuple('@')==tuple(self.Email[i])):
                self.__find=len(self.Email)-self.__number1
                if(tuple(self.Email[-self.__find:])==self.__deneme):
                    print("kabul edildi")
                    self.cursor.execute("INSERT INTO User_list VALUES(?,?,?,?,?)",(self.Username, self.Surname, self.Birthdate, self.Email, self.Password))
                else:
                    print("yanlış mail denemesi")

    def inemail(self):
        self.cursor.execute("SELECT Email FROM User_list")
        self.__lookmail=self.cursor.fetchall()
        for i in range(len(self.__lookmail)):
            if( tuple(self.Email) == tuple(self.__lookmail[i-1][0])):
                print("kayıt var")
            else:
                print("kaydınız yok!!!")

#iki alt çizgi ile encapsulation yapılır. örnek __hızlan  fonku veya __hız değişkeni

#ad=input("adınız:\n")
#soyad=input("soyadınız:\n")
#dogma=input("dogum tarihiniz:\n")
mail=input("emailniz:\n")
#sifre=input("sifreniz:\n")

x=Database("selim","eminoglı",16,mail,234)
x.adddatabase()
x.inemail()
x.sbt1.commit()
x.sbt1.close()