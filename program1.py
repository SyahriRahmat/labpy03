print (' === PROGRAM HITUNG LABA PERUSAHAAN ===')
print('')
print ('Note : ')
print('Bulan Pertama Dan Ke 2	= 0%')
print('Pada Bulan Ke 3		= 1%')
print('Pada Bulan Ke 5		= 5%')
print('Pada Bulan Ke 8		= 2%')
print ('')
a=100000000
for x in range(1,9):
	if (x>=1 and x<=2):
		b= 0*a
		print('Laba Bulan Ke - ',x, 'Sebesar =', b)
	if (x>=3 and x<=4):
		c=a*0.1
		print('Laba Bulan Ke - ', x, 'Sebesar =', c)
	if (x>=5 and x<=7):
		d=a*0.5	
		print('Laba Bulan Ke - ', x, 'Sebesar =', d)
	if (x==8):
		e=a*0.2
		print('Laba Bulan Ke - ', x, 'Sebesar =', e)
total=b+b+c+c+d+d+d+e
print ('\nTotal Laba Adalah	= ', total)