print ('== PROGRAM MENAMPILKAN BILANGAN RANDOM KURANG DARI 0.5 ==')
import random
jumlah = int(input('Masukkan Jumlah Bilangan N : '))
a = 0
for i in range (jumlah):
	a +=1
	i = random.uniform(0.0,0.5)
	print( "Data ke -", a, "==>", i)
print ('====== PROGRAM SELESAI =====')