import random
from quickPow import *
'''
12660080856507330260014884760386366843818805754161383450900446633781098831208888
02885434855597079715400065966280055005929629760575260374176115165232947386571381
24552956768709033944974483081794159473703111610835333589367651586071626134225995
377042174764790658312866772106872794279239506995907063253507125030121
'''
'''
49990954709687956273580143810396846563076522717075236701033710039653677556970137
72450142867564305447864836199030419588286510513872973371883966331022248427410891
71155091492297611144356818310228239033976130119972313778607088684288949833479979
92823634288080678744140234522891126943796371837343757490572414397027
'''

def getE(ln):
    while True:
        dev = round(random.uniform(1, 100000))
        e = ln//dev
        if gcd(e, ln) == 1:
            return e

def main(p, q):
    N = p*q
    lN = (p-1)*(q-1)//gcd(p-1, q-1)
    e = getE(lN)
    #d = mpow(e, lN-2, lN)
    d, tt = exgcd(e, lN)
    #print('d * e : ', (d*e)%lN)
    print('e : %x, N : %x'%(e, N))
    with open('rsa.dat', 'w') as f:
        f.write(str(e) +' ' + str(N))
    with open('pri.dat', 'w') as f:
        f.write(str(d))

if __name__ == '__main__':
    print("please put the key in the key.txt!")
    with open('E:\cryptology\key.dat') as f:
         context = f.read()
         context = context.split('\n')
         num = []
         for i in context:
            num.append(int(i))
         main(num[0], num[1])