from quickPow import *
def encode(data, e, N):
	return mpow(data, e, N)

def main(e, N):
	data = input('input > ')
	out = ''.join("%.2x" %ord(i) for i in data)
	num = int(out, 16)
	print('data encode : %X' %encode(num%N, e, N))

with open('rsa.dat', 'r') as f:
	context = f.read()
	context = context.split(' ')
	num = []
	for i in context:
		num.append(int(i))	
	e = num[0]
	N = num[1]
	main(e, N)