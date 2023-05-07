"""

RECURSION

1-BITIS DURUMU TANIMLAMAK GEREKLİ FONKSIYONUN SONSUZA KADAR KENDINI CAGIRMAMASI İÇİN
2-FONKSIYONUN BELLİ SARTLARDA KENDINI CAGIRMAMASI GEREKLİ

"""
"""
def addition(serie):
    const=0
    for i in serie:
        const+=i
    return const

print(addition({1,2,3,4}))
"""
# aynısını recursıon ıle yapılmısı asagıda

def addition2(serie2):
    if (len(serie2))==0:
        return 0
    else:
        return serie2[0] + (addition2(serie2[1:]))

print(addition2([1,2,3,4]))
"""
def topla(liste):
    if (len(liste)) == 0:
        return 0
    else:
        return liste[0] + (topla(liste[1:]))

print(topla([1,2,3,4]))

"""
