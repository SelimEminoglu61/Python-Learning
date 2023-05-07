"""
dictionary={"ronaldo":"en iyisi","selim":"idol alan","yavuz":"selimin kardesi"}

# print(type(dictionary)) # bu satır yazılacak degişkenın tıpını gösterır


print(dictionary["ronaldo"]) # burdada sozlukte ıstedıgımız anahtar kelımeyı secip degerini alabiliyoruz.

# hepsini gostermek için
for i in dictionary.items(): # items fonksıyonu gerekli.
    print(i)

# eger daha duzenlı,ayrı ayrı yazmak istersek araya bosluk ve liste gıbı oldugu için duzenleme yapıyoruz.

for i in dictionary.items():
    print(i[0] + " " + i[1])

# 2.yol duzenlı yazmak için

for i,j in dictionary.items():
    print(i + " " + j)
# iki degişken kullsnılarak yapıldı.
"""
training={"selim":{"guc","hız","dayanıklılık"},"yavuz":{"kosma","savunma"},"yusuf":{"kalecilik","refleks"}}

wantining_person=input("type your wanting person:")

for i in (training[wantining_person]):
    print(i)
# yazılınca istenen kişinin antrenmanını yazan program







