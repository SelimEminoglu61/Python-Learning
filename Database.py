import sqlite3 as sp


class Database:
    def __init__(self,Username,Surname,Birthdate,Email:str,Password):
        self.Username = Username
        self.Surname = Surname
        self.Birthdate = Birthdate
        self.Password = Password
        self.Email = Email
        self.createdatabase()

    def createdatabase(self):
         self.sbt1 = sp.connect("EmailApp.sqlite")
         self.cursor = self.sbt1.cursor()
         self.cursor.execute("CREATE TABLE IF NOT EXISTS User_list (Username,Surname,Birthdate,Email,Password)")
