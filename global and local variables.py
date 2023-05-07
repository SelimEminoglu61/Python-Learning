
a=10 #olursa sonuc 5,10 seklinde olur


def functıon():
 #   global a #olunca ıcerde tanımladıgımız degeri global degısken yapıyor.ve yazınca 5 degerleri gozukuyor.kullanımı tehlikeli olabilir.
    a=5            # bu degişken sadece fonksıyon ıcınde calısır cunku orda tanımlandı.(yerel degişken)
    print(a)       # burda a=5 yazılmasa 10 degeri gozukur cunku fonksıyon o degeri farkedebılıyor.
functıon()

 #  print(a) burda yazılırsa hata verir.cunku fonksıyon ıcındekı degişkene etkisi yok.(a=10 yazılmadan)

print(a)