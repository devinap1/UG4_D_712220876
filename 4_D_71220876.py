bil = list(map(int, input("silahkan masukkan sekumpulan bilangannya (pisahkan dengan koma): ").split(',')))  #bil = bilangan
tebe = max(bil, key=lambda x: x)               #tebe= bilangan terbesarnya
teke = min(bil, key=lambda x: x)               #teke = bilangan terkecilnya 
print("bilangan yang terbesar adalah" , tebe)            
print("bilangan yang terkecil adalah" , teke)