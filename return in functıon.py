def factorıal(value):
    const=1
    for i in range(1,value+1):
        const*=i
    print("result:",const)
    return const

# fonsiyondan cıkan degerleri kullanmak için kullanılır
# return olması degerı fonsk cıkısı almamızı saglar.
# return olmazsa degeri alamaz ve cıkısı "none" verir
# fonksıyon deger dondurmuyor.
# return aynı zamanda fonksıyonu bitirir.

b=factorıal(5)
print(b)


# ax^2+bx+c=0 için  kök bulma fonksiyonu
def find_root(first,second,third):
    delta=second**2-4*first*third

    if(delta<0):
        print("there isnt real root")
        return

    x1=(-second- delta**0.5)/2*first
    x2=(-second+delta**0.5)/2*first

    return (x1,x2)


a=int(input("first value:"))
b=int(input("second value:"))
c=int(input("third value:"))

result=find_root(a,b,c)

print(result)





