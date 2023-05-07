"""

burda konu python nın bize karsşı gosterdiği hataları elle kontrol
uzerıne bır konu console da gözuken hatalara karsı programa ne yapacagını
soyleyebılıyoruz.

try ve except bır blok try da olabılecek hataları yazarız excepte hatalara gelince ne yapması gerektıgını.

"""

number1=input("gıve fırst number:")
number2=input("gıve second number:")

try :
    number2=int(number2)
    number1=int(number1)
    print(number1/number2)

except ValueError:
    print("please gıve your number")


except ZeroDivisionError:
    print("anynumber to 0 cant divided")



# hataların bırleşmıs hali ise söyle

except (ValueError,ZeroDivisionError):
    print("error")