#################################
#  İ S T İ N Y E   K O M B A T  #
#################################
import sys
import os
import random

# Kahramanlara ait bilgilerin tutulacağı global değişkenler
firstChampName = ""
secondChampName = ""
firstChampHp = 100
secondChampHp = 100
hpBars = "||||||||||||||||||||||||||||||||||||||||||||||||||"
maxHp = 100
headsOrTailsResult = 0


# varsayılan sıfır. Kod bloku içerisinde değer atanacaktır.
# random değerinin dönüşü 0 için 1. kahraman, 1 için 2. kahraman başlayacaktır.


def headsOrTails():
    return random.randint(0, 1)





# Dövüşteki her hamlede kahramanların azalan barlarını gösterebilmek için kullanılan kısım
# Amaç 50 bar varsa (kahramanın sağlık puanı * (bar sayısı / max. sağlık puanı)) formülü ile görüntülemek
# Bu mantığa göre 100 HP ile 50 bar varsa 50 HP kalınca şampiyon 25 bar kalacaktır.
# Buradaki (" " * sayı) olarak gösterilen işlemler tamamen konsol ekranında uygun görüntü olması için eklenmiştir.
def printCurrentHps(firstChampHp, secondChampHp):
    firstChampHp = firstChampHp if firstChampHp > 0 else 0
    secondChampHp = secondChampHp if secondChampHp > 0 else 0
    firstChampHpBar = hpBars[0: int(firstChampHp * (len(hpBars) / maxHp))]
    secondChampHpBar = hpBars[0: int(secondChampHp * (len(hpBars) / maxHp))]

    # Yazı tura sonucuna göre ekranda listeleme
    if headsOrTailsResult == 0:
        print("{}{}{}".format(
            firstChampName, " " * (int(firstChampHp * (len(hpBars) / maxHp)) + 12), secondChampName))
        print("HP[{}]{}{}HP[{}]{}".format(firstChampHp,
                                          firstChampHpBar, " " * (60 - len(hpBars)), secondChampHp, secondChampHpBar))
    else:
        print("{}{}{}".format(
            secondChampName, " " * (int(secondChampHp * (len(hpBars) / maxHp)) + 12), firstChampName))
        print("HP[{}]{}{}HP[{}]{}".format(secondChampHp,
                                          secondChampHpBar, " " * (60 - len(hpBars)), firstChampHp, firstChampHpBar))


# Saldırının başarılı olup olmadığını dönen metot
# Burada başarı oranının random üretilen sayıdan büyük ya da eşit olması durumunda başarılı değilse başarısız dönmesi sağlandı
# Örneğin 30 hitPoint için şans 70 ise ve rastgele üretilen sayı 43 ise başarılı bir vuruş eğer üretilen sayı 87 ise başarısızdır.


def isSuccessfulHit(champName, hitPoint):
    successRate = 100 - hitPoint
    randomRate = random.randint(1, 100)
    hasSuccess = successRate >= randomRate
    if hasSuccess:
        print("{} {} hasar verdi !!".format(champName, hitPoint))
    else:
        print("Ooopsy! {} saldırıyı kaçırdı!".format(champName))
    return hasSuccess


# Kahramanın vurma işlemlerine ait mantık bu bölümde yer almaktadır.
def selectHitRate(champName):
    hitRate = -1
    print("———– {} Saldırı !! ———–".format(champName))
    while hitRate > 50 or hitRate < 1:
        print("Saldırı Büyüklüğünüzü 1 ile 50 arasında seçin: ")
        hitRate = int(input())
        if hitRate > 50 or hitRate < 1:
            print("Saldırı Saldırı büyüklügü 1 ile 50 arasında olmalıdır.")
    return hitRate


# Oyun sonucu


def printGameWinner(gameWinner):
    print("########################################################")
    print("################# {} kazandı! ###################".format(gameWinner))
    print("########################################################")




# Input validation (hatalı durumlarda kullanıcı adının tekrar istenmesi adına döngü kullanılmıştır.)
while firstChampName == "":
    print("———– Ilk Kahraman ———–")
    print("Lütfen kahramanınızın adını yazın: ")
    firstChampName = str(input())
print("———– Ikinci Kahraman ———–")
while secondChampName == "" or secondChampName == firstChampName:
    print("Lütfen kahramanınızın adını yazın: ")
    secondChampName = str(input())
    if secondChampName == firstChampName:
        print("{} alındı, lütfen başka bir isim seçin!".format(
            firstChampName))  # output formatting

# Yazı tura atılır ve sonuç kaydedilir. Sonrasında ilk kimin vuracağını hesaplarken kullanacağız.
headsOrTailsResult = headsOrTails()
print("Yazı tura sonucu: {} önce başlar".format(
    firstChampName if headsOrTailsResult == 0 else secondChampName))

# MORTALLL KOMMBBBAAATT (dövüş başlıyor...)
printCurrentHps(firstChampHp, secondChampHp)
while firstChampHp > 0 and secondChampHp > 0:
    if headsOrTailsResult == 0:
        # İlk kahraman başlar ve hamle yapar
        firstChampHitPoint = selectHitRate(firstChampName)
        # başarılı olup olmadığının kontrolü rand fonksiyonu ile denetlenir
        if isSuccessfulHit(firstChampName, firstChampHitPoint):
            # hamle başarılıysa ikinci şampiyonun canı düşer
            secondChampHp = secondChampHp - firstChampHitPoint

        printCurrentHps(firstChampHp, secondChampHp)

        # İkinci kahraman yenildi mi kontrolü gerekli. Çünkü eğer HP <= 0 gibi bir durum söz konusu ise ikinci kahraman artık hamle yapamamalı.
        if secondChampHp > 0:
            # Sıra ikinci şampiyonda
            secondChampHitPoint = selectHitRate(
                secondChampName)  # hamlenin boyutu hesaplanır
            # başarılı olup olmadığının kontrolü rand fonksiyonu ile denetlenir
            if isSuccessfulHit(secondChampName, secondChampHitPoint):
                # hamle başarılıysa ilk şampiyonun canı düşer
                firstChampHp = firstChampHp - secondChampHitPoint

            printCurrentHps(firstChampHp, secondChampHp)

    else:
        # İkinci kahraman başlar ve hamle yapar
        secondChampHitPoint = selectHitRate(secondChampName)
        if isSuccessfulHit(secondChampName, secondChampHitPoint):
            # hamle başarılıysa ilk şampiyonun canı düşer
            firstChampHp = firstChampHp - secondChampHitPoint

        printCurrentHps(firstChampHp, secondChampHp)
        # İlk kahraman yenildi mi kontrolü gerekli. Çünkü eğer HP <= 0 gibi bir durum söz konusu ise ilk kahraman artık hamle yapamamalı.
        if firstChampHp > 0:
            # Sıra ilk şampiyonda
            firstChampHitPoint = selectHitRate(firstChampName)
            # hamle başarılıysa ikinci şampiyonun canı düşer
            if isSuccessfulHit(firstChampName, firstChampHitPoint):
                secondChampHp = secondChampHp - firstChampHitPoint

            printCurrentHps(firstChampHp, secondChampHp)

printGameWinner(firstChampName if firstChampHp > 0 else secondChampName)

#oyunu yeniden oynamak istediğini sorup evet ise baştan başlatıyoruz hayır ise oyunu bitiriyoruz.
while firstChampHp <= 0 or secondChampHp <= 0:
    restartGame = input("Bir tur daha oynamak istermisiniz(Evet veya Hayır)?:")
    if restartGame == "Evet":
        os.system("python muhammet_aytac_ipekel.py")
    elif restartGame == "Hayır":
        print("Oynadığınız için teşekkürler! Tekrar görüşürüz!")
        break
