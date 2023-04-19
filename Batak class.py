import random
class Batak:
      
    A = ['♠', '♣', '♥', '♦']
    B = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    oyuncular = {}
    oyuncu_sira = []
    oyun_skor = {}
    oynanan_kartlar = []
    tahminler = {}
    ilk_kart_kontrol = {}
    for i in A:
        ilk_kart_kontrol.setdefault(i,[])
    def __init__(self,isim,deste=[]):
        self.isim = isim
        self.deste = deste
        self.oyun_skor.setdefault(self.isim, 0)
        self.oyuncular.setdefault(self.isim, {}.fromkeys(self.A))
        self.oyuncu_sira.append(self.isim)
        for _ in range(4):
            self.oyuncular.setdefault(self.isim, {}.fromkeys(self.A))
    
    def deste_olusturma(self):
        print("\nDAĞITILAN KARTLAR:\n")
        deck = []
        for i in Batak.A:
            for j in Batak.B:
                deck.append(i+j)
        for oyuncu in self.oyuncular:    
            for i in Batak.A:
                Batak.oyuncular[oyuncu][i] = []
            for i in range(13):
                kart = random.choice(deck)
                Batak.oyuncular[oyuncu][kart[0]].append(kart[1:])
                deck.remove(kart)
            
            print(oyuncu + ":")
            for karttip in self.oyuncular[oyuncu]:
                self.oyuncular[oyuncu][karttip].sort(key=Batak.B.index)  # kartlar B listesindeki siraya göre dizilir
                print(karttip, self.oyuncular[oyuncu][karttip])
    
    def tahmin_et(self):
        self.tahmin = int(input(f"{self.isim}: "))
        Batak.tahminler.setdefault(self.isim)
        Batak.tahminler[self.isim] = self.tahmin
    
    def oyun(self):
        oyun_kazanma_tur = {}
        for oyuncum in Batak.oyuncu_sira:
            oyun_kazanma_tur.setdefault(oyuncum, 0) # kaç el kazandığını tur başına gösterecek
        print("\nOYUN BAŞLADI...")
        sira = random.randrange(4)  # oyuna başlayacak oyuncu rastgele belirleniyor
        for el in range(13):  # 13 el oynanacak
            print(str(el+1) + ". el:")
            oynayan = 0
            Batak.oynanan_kartlar = []  # bu liste içine kimin hangi karti attiği yazilacak
            while oynayan < 4:
                oyuncu = Batak.oyuncu_sira[sira]
                if oynayan == 0:  # ilk kart atacak oyuncu ise kart tipi belirlenecek (rastgele)
                    while True:
                        kart_tipi = random.choice(Batak.A)
                        if len(Batak.oyuncular[Batak.oyuncu_sira[sira]][kart_tipi]):  # o tipte karti yoksa döngü devam edecek
                            break
                    oyuncu_kart = (oyuncu, kart_tipi, Batak.oyuncular[oyuncu][kart_tipi].pop()) # o tipteki en büyük karti atiyor
                    Batak.ilk_kart_kontrol[oyuncu_kart[1]].append(oyuncu_kart[2])
                    buyuk_kart = oyuncu_kart 
                else:  # diğer oyuncular ilk oyuncunun belirlediği kart tipinde kart atacak
                    if len(Batak.oyuncular[oyuncu][kart_tipi]): # eğer elinde o kart tipinde kart varsa atılan en büyük karttan daha büyük veya elindeki en düşük kartı atacak 
                        if self.B.index(self.oyuncular[oyuncu][kart_tipi][-1]) > Batak.B.index(buyuk_kart[2]):
                            oyuncu_kart = (oyuncu, kart_tipi, Batak.oyuncular[oyuncu][kart_tipi].pop())
                            buyuk_kart = oyuncu_kart
                        else:
                            oyuncu_kart = (oyuncu, kart_tipi, Batak.oyuncular[oyuncu][kart_tipi].pop(0))
                    else:
                        kart_tipleri = Batak.A.copy()  # Bütün kart tiplerini elinde var mı diye kontrol etmek için yeni liste oluşturuldu
                        kart_tipleri.remove(kart_tipi)  # oynanan kart tipi oyuncuda olmadiği için silindi
                        kartlar = kart_tipleri.copy()
                        for kart in kartlar: # Elinde o kart tipinden hiç kartı yoksa o kartı listeden çıkarıyoruz
                            if not len(Batak.oyuncular[oyuncu][kart]):
                                kart_tipleri.remove(kart)
                        if len(kart_tipleri) == 1:
                            oyuncu_kart = (oyuncu, kart_tipleri[0], Batak.oyuncular[oyuncu][kart_tipleri[0]].pop(0)) # Eğer sadece 1 tane kart tipinde kartı varsa o kart tipinden en küçük kartı atacak
                        elif len(kart_tipleri) == 2: # eğer iki tane varsa hangisinin en küçüğü daha küçükse onu atacak
                            if Batak.B.index(Batak.oyuncular[oyuncu][kart_tipleri[0]][0]) > Batak.B.index(self.oyuncular[oyuncu][kart_tipleri[1]][0]):
                                oyuncu_kart = (oyuncu, kart_tipleri[0], Batak.oyuncular[oyuncu][kart_tipleri[0]].pop(0))
                            else:
                                oyuncu_kart = (oyuncu, kart_tipleri[1], Batak.oyuncular[oyuncu][kart_tipleri[1]].pop(0))
                        else:
                            len00 = Batak.B.index(Batak.oyuncular[oyuncu][kart_tipleri[0]][0])
                            len10 = Batak.B.index(Batak.oyuncular[oyuncu][kart_tipleri[1]][0])
                            len20 = Batak.B.index(Batak.oyuncular[oyuncu][kart_tipleri[2]][0])
                            
                            mini = min(len00,len10,len20) # Aralarındaki en küçük sayıyı bulmak için hepsinin indexinden en küçüğünü seçiyoruz
                            if mini == len00:    # En küçük sayı hangisinin en küçüğüne eşitse onu kullanacağız
                                oyuncu_kart = (oyuncu, kart_tipleri[0], Batak.oyuncular[oyuncu][kart_tipleri[0]].pop(0))
                            elif mini == len10:
                                oyuncu_kart = (oyuncu, kart_tipleri[1], Batak.oyuncular[oyuncu][kart_tipleri[1]].pop(0))
                            else:
                                oyuncu_kart = (oyuncu, kart_tipleri[2], Batak.oyuncular[oyuncu][kart_tipleri[2]].pop(0))

                print(oyuncu_kart[0], oyuncu_kart[1] + oyuncu_kart[2])
                Batak.oynanan_kartlar.append(oyuncu_kart)
                
                oynayan += 1
                sira += 1
                if sira >= 4:
                    sira -= 4
                # atilan 4 karta göre eli kazanani bulma:
            en_buyuk = Batak.oynanan_kartlar[0]   # ilk atilani en büyük kart kabul et
            for kart in Batak.oynanan_kartlar[1:]:
                if kart[1] == en_buyuk[1] and Batak.B.index(kart[2]) > Batak.B.index(en_buyuk[2]):
                    en_buyuk = kart  # en büyük ile ayni kart tipinde daha büyük atildi ise en büyük kart kabul et
            print("eli kazanan:", en_buyuk[0])
            sira = Batak.oyuncu_sira.index(en_buyuk[0])
            oyun_kazanma_tur[en_buyuk[0]]= oyun_kazanma_tur.setdefault(en_buyuk[0], 0)+ 1
        print(oyun_kazanma_tur)
        print("\nSkor Tablosu: \n")
        for key, value in oyun_kazanma_tur.items(): # Her oyuncunun teker teker kaç kez kazandığını tahminleri ile karşılaştırıp puan tablosuna ekliyor.
            if value == Batak.tahminler[key]:
                eklenecek = 10*Batak.tahminler[key]
            elif value > Batak.tahminler[key]:
                eklenecek = 10*Batak.tahminler[key]+(value-Batak.tahminler[key])
            else:
                eklenecek = -10*Batak.tahminler[key]
            print(f"{key}: ({Batak.oyun_skor[key]}) + ({eklenecek}) = {Batak.oyun_skor[key]+eklenecek}")
            Batak.oyun_skor[key] += eklenecek

print("BATAK OYUNUNA HOŞGELDİNİZ! ")
dis_oyuncular = []                           #Oyuncu isimlerini class dışında da bir
for i in range(4):                           #listeye eklemek için boş liste açıp
    oyuncu = Batak(input(f"Oyuncu{i+1}: "))  #her elemanı o listeye de ekliyoruz.
    dis_oyuncular.append(oyuncu)

tur_sayisi = int(input("Kaç tur oynamak istiyorsunuz?\n(Bir tur 13 elden oluşur.): \n"))
while tur_sayisi > 0:
    dis_oyuncular[0].deste_olusturma()
    print("\nBu turda kaç tane el alacağini tahmin et") 
    for i in dis_oyuncular:
        i.tahmin_et()

    dis_oyuncular[0].oyun()
    tur_sayisi -= 1




