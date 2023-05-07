# varsayılan deger:normlade 4 parametre alan fons a ilk anda 3 unu vermek için kullanılabilir.

def add_account(name="it ısnt gived",surname="it ısnt gived",age="ıt ısnt gived",job="it ısnt gived"):

    """
    burda deger girmese bile(kullanıcı) varsayılan deger ile degiskenlerle fonk calısır
    eger verilmemiş olsa(varsayılan deger) fonk calısmaz

    """
    print("your account is adding")

    print("your name:{}\n your surname:{}\n your age:{}\n your job:{}".format(name,surname,age,job))

    print("your account opened :)")


add_account(name="selim",age=20) # python da sıra sistemi ile karısmaması için özellikle belirterek arada soyad eklenmeden verilebilir.

add_account("selim","eminoglu")


