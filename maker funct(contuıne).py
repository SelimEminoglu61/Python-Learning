import random

class Enemy:

    def __init__(self,isim="dusman",kalancan=1000,saldırıgucu=220,kalanmermi=50):
        self.name = isim
        self.healhty = kalancan
        self.power_of_attack = saldırıgucu
        self.numberbullet = kalanmermi

    def saldır(self):
        print(self.name + " saldırıyor..")
        harcananmermi = random.randrange(0,50)
        if (int(harcananmermi) < self.numberbullet):
            harcananmermi =self.numberbullet
            print(str(harcananmermi) + "kadar harcandı(tüm mermisi harcandı)")
            return (harcananmermi ,self.power_of_attack)
        print(str(harcananmermi) + "kadar harcandı")
        self.numberbullet -= harcananmermi
        return (harcananmermi , self.power_of_attack)
    def saldırıyaugra(self,harcananmermi,saldırıgucu):
        print(self.name + " saldırıya ugradı")
        cankaybı=harcananmermi*saldırıgucu
        if (cankaybı > self.healhty):
            print(self.name + " hayatını kaybetti")
        else:
            print(self.name + " nin şu kadar canı var" + str(self.healhty-cankaybı))
    def print(self):
        print("name: ",self.name)
        print("healhty: ",self.healhty)
        print("power of attack: ",self.power_of_attack)
        print("number of bullets: ",self.numberbullet)

dusmanlar = []

i=0
while (i<10):
    rastgelecan =random.randrange(500,2000)
    rastgelesaldırıgucu=random.randrange(300,1000)
    rastgelemermi = random.randrange(20,30)
    yenıdusman = Enemy("dusman"+str(i+1),rastgelecan,rastgelesaldırıgucu,rastgelemermi)
    dusmanlar.append(yenıdusman)
    # burda listeye ekleme
    i += 1
# burası dusmanları listelemek için
#for Enemy in dusmanlar:
#    Enemy.print()

i=0
while(i<3):
    randomenemy1attack  = random.randrange(0,10)
    randomenemy2defense = random.randrange(0, 10)
    dönendeger= dusmanlar[randomenemy1attack].saldır()
    dusmanlar[randomenemy2defense].saldırıyaugra(dönendeger[0],dönendeger[1])
    print("round bitti...")
    i+=1