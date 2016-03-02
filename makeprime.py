from quickPow import *

ckset = [2, 3, 5, 61]

def test(n, a, d):
    if n == 2:
        return True
    if n == a:
        return True
    if n&1 == 0:
        return False
    while( d&1 == 0):
        d = d>>1
    t = mpow(a, d, n)
    while d!=n-1 and t!=1 and t!=n-1:
        t = t*t%n
        d = d<<1
    return t==n-1 or (d&1)==1

def checkPrime(num):
    for item in ckset:
        if test(num, item, num-1) == False:
            return False
    return True

while True:
    a = ''
    vis = []
    for i in range(1024):
        if random.random() > 0.5:
            a += '1'
        else:
            a += '0'
    num = int(a, 2)
    if num in vis or num == 0:
        continue
    vis.append(num)
    if checkPrime(num):
        print(num)
        break
    #print('bad')