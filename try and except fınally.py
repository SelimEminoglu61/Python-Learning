"""

kodda hata olsun olmasın yağmak istedigimiz seyler için kullanılacak seyler

konu:fınally
bu try exceptin sonunda yer alan ve nolursa olsun uygulanan adımları yazarız
dosya acma örnegı gibi acıldıktan sonra kapanması bu işlemle olur
kodun guvenliği de artar
"""
try:
    document=open("tasarım.txt","r")

except IOError:
    print("there ısnt  document")

finally:
    document.close()


