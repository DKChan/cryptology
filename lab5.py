from quickPow import *
import lab2
import random

p = 49990954709687956273580143810396846563076522717075236701033710039653677556970137724501428675643054478648361990304195882865105138729733718839663310222484274108917115509149229761114435681831022823903397613011997231377860708868428894983347997992823634288080678744140234522891126943796371837343757490572414397027
g = 61
x = 1024


def sign(m):
	while True:
		k = round(random.uniform(0, 99999999999))
		if gcd(k, p-1) == 1 and k <= p-2:
			break
	r = mpow(g, k, p)
	#nk = mpow(k, p-3, p-1)
	nk, tt = exgcd(k, p-1)
	#print("chek : ", (nk * k) % (p-1))
	s = (nk * (m - r*x)) % (p-1)
	return r, s
def check(m, r, s, y):
	left = (mpow(y, r, p) * mpow(r, s, p) % p)
	right = mpow(g, m, p)
	#print("left : %d right : %d"%(left, right))
	if left == right:
		print('Accepted!')
	else:
		print('Bad!')

def ELGamal():
	y = mpow(g, x, p)
	m = lab2.md5(m)
	m = int(m, 16)
	r, s = sign(m)
	check(m, r, s, y)

if __name__ == '__main__':
	m = '111'
	ELGamal(m)
	