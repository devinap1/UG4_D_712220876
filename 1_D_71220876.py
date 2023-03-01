print('=========baris aritmatika==========')
def aritmatika(nilaia, selisih, suku):                           #nilaia = nilai awal
    s = selisih - nilaia                                     #s = bedanya
    sun = nilaia + (suku - 1) * s                               #sun = suku n
    tot = (suku / 2) * (nilaia + sun)                               #tot= total
    return tot
bilangan_a = int(input("masukkan bilangan awal: "))
selisihnya = int(input("masukkan selisih bilangan anda: "))
suku = int(input("masukkan banyaknya suku: "))
tot = aritmatika(bilangan_a, bilangan_a + selisihnya, suku)
print("Total dari deret aritmatika tersebut adalah:", tot)
