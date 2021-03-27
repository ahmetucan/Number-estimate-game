import random
x = 5 #random.randint(1,100)
can = int(input("hak sayınızı giriniz:"))
hak = can
sayac = 0
while hak > 0:
    hak -= 1
    sayac += 1
    girilensayi = int(input("tahminizi giriniz: ")) 

    if girilensayi==x:
        print(f"{sayac}. defada doğru tahmin ettiniz.Puanınız: {100-(100/can)*(sayac-1)}")
        break
    elif girilensayi>x:
        print("aşağı")
    else:
        print("yukarı")    


    if hak == 0:
        print(f"hakkınız bitti sayı: {x} ")    
