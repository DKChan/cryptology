from quickPow import *
pki = []

def getCer(name, pk):
	new_cer = {}
	new_cer['name'] = name
	new_cer['pk'] = pk
	pki.append(new_cer)
	return new_cer
def checkCer(cer):

def getQ(par):
	ans = 2
	while par!=1:
		if ans > 2160 and par%ans == 0:
			return ans
		while par%ans == 0:
			par = par//ans
			# print(par)
		ans += 1
	return -1

def sign(p, q, a, g):
	# ng = mpow(g, p-2, p)
	# v = mpow(ng, s, p)
	r = 7777
	s = round(random.uniform(0, q-1))
	ng = exgcd(g, p)
	v = mpow(ng, s, p)
	x = mpow(g, r, p)
	myCer = getCer(X, 'A')
	e, state = checkFir(myCer)
	if state == False:
		print('No!')
		return False
	y = (s*e+r)%q
	checkSec(y, v, g, e, p, x)

def checkFir(cer, q):
	e = round(random.uniform(0, q))
	if checkCer(cer):
		return e,True 
	else: 
		return e,False

def checkSec(y, v, g, e, p, x):
	right = mpow(g, y, p) * mpow(v, e, p) % p
	if right == x:
		print('Accepted!')
	else:
		print('No!')

def makeKey():
	p = 245404477
	q = 34603
	return p, q

if __name__ =='__main__':
	p, q= makeKey()
	a = 61
	g = a*(p-1)/q % q
	sign(p, q, a, g)