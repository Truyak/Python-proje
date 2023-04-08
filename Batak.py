# -- Trakya Ünviersitesi, Bilgisayar Mühendisliği Bölümü, Programlama Dillerine Giriş Dersi --
# Bir iskmabil destesinin 4 oyuncuya rastgele dağitilmasi ve Batak (Spades) oyunu için temel
# kurallarin tanimli olduğu bir program kodu verilmiştir. Oyunu oynamamiş olan öğrenciler
# çeşitli internet sitelerinden veya videolardan kurallari öğrenebilirler.

# Program kodunun aşağidaki yönlerden eksiklerinin öğrenciler tarafindan giderilmesi beklenmektedir:
# + Bu kodda sadece 1 tur oynanmaktadir. Önceden belirlenen sayida tur adedi ile oynanmasi sağlanmalidir.
# + Her oyuncunun tur başinda kaç el alacağini tahmin etmesi eklenmelidir. Bu 3 farkli şekilde yapilabilir:
#   1) Her oyuncu için rastgele belirlenebilir (mantikli değil)
#   2) Oyuncunun kartlarina göre bilgisayar karar vermeye çalişabilir (yapmasi zor)
#   3) Kullanici her oyuncu için bu değeri girebilir (yapmasi kolay)
# + Puanlama sistemi eklenmeli ve her tur sonunda güncel puan tablosu gösterilmelidir:
#   - Oyuncu tahmin ettiği eli alirsa "tahmin x 10" puan kazanir (3 tahmin edip tam 3 el almişsa 30 puan)
#   - Fazladan aldiği her el için 1 puan eklenir (3 tahmin edip 5 aldiysa: 32)
#   - Tahmininden az el alirsa "tahmin x 10" puan kaybeder (3 tahmin edip 2 aldiysa: -30)

# Program kodunda aşağidaki yönlerden geliştirmeler de yapilabilir (şart değil ama ek puan kazandirir):
# + Oyuncular bu kodda genel olarak elindeki o tipten en büyük karti atmaktadir (sadece Maça kartini bir koz
#   olarak kullanacaği zaman en küçüğünü atmaktadir). Çoğu durumda bu mantikli bir seçim değildir (Kod içinde
#   bununla ilgili bir NOT yazilmiştir). Oyuncularin daha mantikli kart atmalari için kontroller eklenebilir.
# + Kodun içinde fonksiyonlar veya siniflar kullanilmamiştir. Öğrenciler sonraki derslerde görecekleri bu
#   tür yapilari da kullanarak kodu daha güzel hale getirebilir.

import random

A = ['♠', '♣', '♥', '♦']
B = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

tur_sayisi = int(input("Kaç Tur oynanmasini istiyorsunuz : \n"))
deste = []
oyun_skor = {} # Her turun sonunda oyun_kazanma_tur listesine ve tahminlere bağlı olarak ekleme yapılacak liste
oyuncular = {}
oyuncu_sira = []  # oyuncu isimleri girilecek ise boş liste olmali
print("OYUNCULARIN İSİMLERİNİ GİRİN:") # oyuncu isimleri girilecek ise bu satir açilmali
for i in range(4):
    oyuncular.setdefault(input("Oyuncu " + str(i+1) + ": "), {}.fromkeys(A)) #isimler girilmeyecek ise bu kapatilmali, alttaki açilmali
    # oyuncular.setdefault(oyuncu_sira[i], {}.fromkeys(A)) #isimler girilecek ise bu kapatilmali, üstteki açilmali
for oyuncu in oyuncular:
    oyuncu_sira.append(oyuncu)
tahminler = {}
print("Bu turda kaç tane el alacağini tahmin et")

while tur_sayisi > 0: 
    oyun_kazanma_tur = {} # Her tur yenilenen her oyuncunun kaç el aldığını gösteren liste
    
    for i in A:
        for j in B:
            deste.append(i+j)

    for oyuncu in oyuncular:
        
        for i in A:
            oyuncular[oyuncu][i] = []
        for i in range(13):
            kart = random.choice(deste)
            oyuncular[oyuncu][kart[0]].append(kart[1:])
            deste.remove(kart)
        
    for oyuncum in oyuncu_sira:
        oyun_kazanma_tur.setdefault(oyuncum, 0)
        oyun_skor.setdefault(oyuncum,0)

    print("\nDAĞITILAN KARTLAR:")
    for oyuncu in oyuncular:
        print(oyuncu + ":")
        for karttip in oyuncular[oyuncu]:
            oyuncular[oyuncu][karttip].sort(key=B.index)  # kartlar B listesindeki siraya göre dizilir
            print(karttip, oyuncular[oyuncu][karttip])
    
    tahminler = {}                                     # Eğer test yapacaksanız bu 5 satırı yorum yapın ve 
    print("Bu turda kaç tane el alacağini tahmin et")  # While döngüsünün dışına bunları kopyalayıp bir
    for oyuncu_isim in oyuncular:                      # daha yazınız.
        tahmin = int(input(f"{oyuncu_isim} : "))       #
        tahminler.setdefault(oyuncu_isim, tahmin)      # 
    
    print("\nOYUN BAŞLADI...")  # Oyun sadece 1 tur (13 el) oynanacak
    
    sira = random.randrange(4)  # oyuna başlayacak oyuncu rastgele belirleniyor
    for el in range(13):  # 13 el oynanacak
        print(str(el+1) + ". el:")
        oynayan = 0
        oynanan_kartlar = []  # bu liste içine kimin hangi karti attiği yazilacak
        while oynayan < 4:
            oyuncu = oyuncu_sira[sira]
            if oynayan == 0:  # ilk kart atacak oyuncu ise kart tipi belirlenecek (rastgele)
                while True:
                    kart_tipi = random.choice(A)
                    if len(oyuncular[oyuncu_sira[sira]][kart_tipi]):  # o tipte karti yoksa döngü devam edecek
                        break
                oyuncu_kart = (oyuncu, kart_tipi, oyuncular[oyuncu][kart_tipi].pop()) # o tipteki en büyük karti atiyor
                buyuk_kart = oyuncu_kart 
                # NOT: Oyuncunun o tipteki en büyük karti atmasi çoğu durumda mantikli değil. Rastgele olarak seçilmesi veya
                # en küçüğü atmak da mantikli olmaz. Oyuncunun mantikli bir kart atmasini sağlamak için birçok ilave kontrol
                # eklenmesi gerekir (Daha önce 'A' çikti ise 'K' ile başlamak mantikli olabilir vb.). Bu programda o elin
                # ilk karti atilirken de, sonraki kartlar için de mantikli olmasina yönelik kontroller bulunmamaktadir.
            else:  # diğer oyuncular ilk oyuncunun belirlediği kart tipinde kart atacak
                if len(oyuncular[oyuncu][kart_tipi]): # eğer elinde o kart tipinde kart varsa atılan en büyük karttan daha büyük veya elindeki en düşük kartı atacak 
                    if B.index(oyuncular[oyuncu][kart_tipi][-1]) > B.index(buyuk_kart[2]):
                        oyuncu_kart = (oyuncu, kart_tipi, oyuncular[oyuncu][kart_tipi].pop())
                        buyuk_kart = oyuncu_kart
                    else:
                        oyuncu_kart = (oyuncu, kart_tipi, oyuncular[oyuncu][kart_tipi].pop(0))
                elif len(oyuncular[oyuncu]['♠']):  # o kart tipinde karti yoksa en küçük maça kartini atacak
                    oyuncu_kart = (oyuncu, '♠', oyuncular[oyuncu]['♠'].pop(0))
                else:  # maça karti da yoksa, diğer 2 tipin hangisinde daha çok kart varsa en küçük karti atacak
                    kart_tipleri = A[:].copy()  # Bütün kart tiplerini elinde var mı diye kontrol etmek için yeni liste oluşturuldu
                    kart_tipleri.remove(kart_tipi)  # oynanan kart tipi oyuncuda olmadiği için silindi
                    for kart in kart_tipleri: # Elinde o kart tipinden hiç kartı yoksa o kartı listeden çıkarıyoruz
                        if not len(oyuncular[oyuncu][kart]):
                            kart_tipleri.remove(kart)
                    if len(kart_tipleri) == 1:
                        oyuncu_kart = (oyuncu, kart_tipleri[0], oyuncular[oyuncu[kart_tipleri[0]]].pop(0)) # Eğer sadece 1 tane kart tipinde kartı varsa o kart tipinden en küçük kartı atacak
                    elif len(kart_tipleri) == 2: # eğer iki tane varsa hangisinin en küçüğü daha küçükse onu atacak
                        if B.index(oyuncular[oyuncu][kart_tipleri[0]][0]) > B.index(oyuncular[oyuncu][kart_tipleri[1]][0]):
                            oyuncu_kart = (oyuncu, kart_tipleri[0], oyuncular[oyuncu][kart_tipleri[0]].pop(0))
                        else:
                            oyuncu_kart = (oyuncu, kart_tipleri[1], oyuncular[oyuncu][kart_tipleri[1]].pop(0))
                    else:
                        len00 = oyuncular[oyuncu][kart_tipleri[0]][0]
                        len10 = oyuncular[oyuncu][kart_tipleri[1]][0]
                        len20 = oyuncular[oyuncu][kart_tipleri[2]][0]
                        
                        mini = min(B.index(len00),B.index(len10),B.index(len20)) # Aralarındaki en küçük sayıyı bulmak için hepsinin indexinden en küçüğünü seçiyoruz
                        if mini == len00:    # En küçük sayı hangisinin en küçüğüne eşitse onu kullanacağız
                            oyuncu_kart = (oyuncular, oyuncular[oyuncu[kart_tipleri[0]]], mini)
                        elif mini == len10:
                            oyuncu_kart = (oyuncular, oyuncular[oyuncu[kart_tipleri[1]]], mini)
                        else:
                             oyuncu_kart = (oyuncular, oyuncular[oyuncu[kart_tipleri[2]]], mini)

            print(oyuncu_kart[0], oyuncu_kart[1] + oyuncu_kart[2])
            oynanan_kartlar.append(oyuncu_kart)
            
            oynayan += 1
            sira += 1
            if sira >= 4:
                sira -= 4
        # atilan 4 karta göre eli kazanani bulma:
        en_buyuk = oynanan_kartlar[0]   # ilk atilani en büyük kart kabul et
        for kart in oynanan_kartlar[1:]:
            if kart[1] == en_buyuk[1] and B.index(kart[2]) > B.index(en_buyuk[2]):
                en_buyuk = kart  # en büyük ile ayni kart tipinde daha büyük atildi ise en büyük kart kabul et
        print("eli kazanan:", en_buyuk[0])
        sira = oyuncu_sira.index(en_buyuk[0])
        oyun_kazanma_tur[en_buyuk[0]]= oyun_kazanma_tur.setdefault(en_buyuk[0], 0)+ 1
    print(oyun_kazanma_tur)
    print("\nSkor Tablosu: \n")

    for key, value in oyun_kazanma_tur.items(): # Her oyuncunun teker teker kaç kez kazandığını tahminleri ile karşılaştırıp puan tablosuna ekliyor.
        if value == tahminler[key]:
            eklenecek = 10*tahminler[key]
        elif value > tahminler[key]:
            eklenecek = 10*tahminler[key]+(value-tahminler[key])
        else:
            eklenecek = -10*tahminler[key]
        print(f"{key}: ({oyun_skor[key]}) + ({eklenecek}) = {oyun_skor[key]+eklenecek}")
        oyun_skor[key] += eklenecek
    
    tur_sayisi -= 1
