print ('== Menampilkan Bilangan Terbesar, Berhenti ketika 0 ==')
max = 0
while True :
	a=int(input("Masukkan Bilangan : "))
	if max < a:
		max = a
	if a == 0:
		 break 
print('=== Bilangan Terbesar Adalah : ',max, '===')
print ('===== Program Selesai =====')