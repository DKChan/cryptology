def mpow(a, d, n):
    res = 1
    while d > 0:
        if d&1:
            res = res * a % n
        a = a*a%n
        d = d//2
    return res

def gcd(a, b):
    return a if b==0 else gcd(b, a%b)

def exgcd(a, b):
	if b==0:
		return 1,0
	x, y=exgcd(b, a%b)
	return y, x-(a//b)*y