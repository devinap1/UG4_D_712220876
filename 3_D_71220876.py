def mencari_kata_terpanjangnya(kalimatnya):
    kata_tiap_kata = kalimatnya.split()
    terpanjang = max([len(kata) for kata in kata_tiap_kata])
    kater = [kata for kata in kata_tiap_kata if len(kata) == terpanjang]
    return kater

kalimatnya = input("masukkan kalimat: ")
kater = mencari_kata_terpanjangnya(kalimatnya)

if len(kater) == 1:
    print("Kata terpanjang pada kalimat tersebut adalah:", kater[0])
else:
    print("Kata terpanjang pada kalimat tersebut adalah:", ", ".join(kater))
