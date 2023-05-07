import numpy as np
import pandas as pan
import matplotlib

# Numpy arrays matrix oluşumu
#print("\ntek boyutlu")
#List=[2,3,4]  # tek boyutlu liste
#print(np.array(List))
#print("\niki boyutlu")
#liste2=[[3,45],[56,78]]  # iki boyutlu liste
#print(np.array(liste2))
#print("\narange fonku") # bize istedğimiz aralıkta numpy dizisi verir
#print(np.arange(0,10))
#print("\nzeros fonku") # içinde sıfır olarak bize dizi verir
#print(np.zeros(6))
#print(np.zeros((2,2)))
#print("\n ones fonku") # içinde bir olarak bize dizi verir
#print(np.ones(2))
#print("\n linspace metodu") #bu range gibi davranır
#a=np.linspace(0,20,10)
#print(a)
#print("\n eye fonku") # köşe matrisi oluşturma
#print(np.eye(5))
#print("\n random fonku") # rastgele sayıları almamızı sağlar
#print(np.random.randn(4,5)) # tek değerde tek boyutlu
#print("\n randint ile tek değer yapılabilir")
#print(np.random.randint(1,10,5)) # 1 den 10 a kadar sayılardan biri
# 3. parametre kaç tane değer istediğimiz

# numpy dizi metodları

siralidizi=np.arange(20)
rastgeledizi=np.random.randint(0,100,30)

print(siralidizi.reshape(5,4)) # reshape ile yeniden şekillendirip matrix formuna getirebiliriz

# max ve min ile sayıların en büyüğü veen küçüğü bulunabilir
# argmax ve argmin ile de indexleri belli olur
#print(rastgeledizi.max())
#print(rastgeledizi.min())
#print(rastgeledizi.argmax())
#print(rastgeledizi.argmin())
#print("\n shape özelliği ") # ile dizini o anki şekli hakında bilgi alabiliriz
#print(rastgeledizi.shape)

# ÖNEMLİ eğer bir dizi üzerinde çalışma olucaksa kopyası ile yapılır çünkü alınan parça asıl olanı etkiler(listedeğiştirilebilir)
# copy() metdou ile dizi.copy() gibi
#matrix indeksiler
# dizi[1][2] ile dizi[1,2] aynı
#matrix[1:][2] gibi durumda 1 den sona kadar row ve 2. column alır
siralidizi2=siralidizi.reshape(5,4)
print(siralidizi2[[0,2,4]]) # 0-2-4 row larını alıp matrix verdi



