
def gcd(a ,b):
	if b == 0:
		return a
	else:
		return gcd(b, a%b)

Z = '计算机学院网络工程信息安全，我们热爱中华人民共和国。大家'

if __name__ == '__main__':
    #C = input('input > ')
    C = '和院程安我爱计'
    for i in range(28):
        p = -1
        if gcd(i, 28) == 1 :
            for j in range(28):
                if i*j%28 == 1:
                    p = j
                    break
            for j in range(28):
                out = ''
                for ch in C:
                    wh = Z.find(ch)
                    out += Z[(p * (wh - j)) % 28] # check the regarive
                print('%d ans : %s'%(j+1, out))

    
