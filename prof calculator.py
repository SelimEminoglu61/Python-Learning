from math import *

def toplama(x,y):
    toplam = x + y
    return toplam

def çıkarma(x,y):
    çıkar=x-y
    return çıkar

def çarpma(x,y):
    çarp=x*y
    return çarp

def bölme(x,y):
    if ( y == 0):
        # sayılar 0 a bölünmez ondan kontrol yapılıyor.
        a = print("bilinmiyor,0 a bölüm olmaz.")
        return a
    böl=x/y
    return böl

def karekök(sayı1):
    a=pow(sayı1,0.5)
    return a

def karesinial(sayı2):
    b=pow(sayı2,2)
    return b

def faktöriyel(sayı3):
     c=factorial(sayı3)
     return c
if __name__=='__main__':

    while True:
        print("-"*60)
        print("Hesap Makinesine Hoşgeldiniz!!!!")
        print("Yapacağınız işlemi seçip işleme göre sayı veriniz.")
        print("1.Topla","2.Çıkar","3.Çarp","4.Böl","5.Karekök al",
              "6.Karesini al","7.Faktöriyel bul","8.Çıkış",sep ='\n')
        print("-"*60)

        işlem=input()


        if (int(işlem) not in range(8) or int(işlem) == 0):
            print("Lütfen geçerli bir sayı giriniz!!")
            continue

        if (int(işlem) == 1):
            print("Sayılarınızı giriniz.\n")
            say1=int(input())
            say2=int(input())
            print("Sonucunuz: ",toplama(say1,say2))

        elif (int(işlem) == 2):
            print("Sayılarınızı giriniz.\n")
            say1 = int(input())
            say2 = int(input())
            print("Sonucunuz: ", çıkarma(say1,say2))

        elif (int(işlem) == 3):
            print("Sayılarınızı giriniz.\n")
            say1 = int(input())
            say2 = int(input())
            print("Sonucunuz: ", çarpma(say1,say2))

        elif (int(işlem) == 4):
            print("Sayılarınızı giriniz.\n")
            say1 = int(input())
            say2 = int(input())
            print("Sonucunuz: ", bölme(say1,say2))

        elif (int(işlem) == 5):
            print("Sayınızı giriniz.\n")
            say1 = int(input())
            print("Sonucunuz: ", karekök(say1))

        elif (int(işlem) == 6):
            print("Sayılarınızı giriniz.\n")
            say1 = int(input())
            print("Sonucunuz: ", karesinial(say1))

        elif (int(işlem) == 7):
            print("Sayılarınızı giriniz.\n")
            say1 = int(input())
            print("Sonucunuz: ", faktöriyel(say1))
