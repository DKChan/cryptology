from math import *

F = lambda x, y, z: (((x) & (y)) | ((~x) & (z)))
G = lambda x, y, z: (((x) & (z)) | ((y) & (~z)))
H = lambda x, y, z: ((x) ^ (y) ^ (z))
I = lambda x, y, z: ((y) ^ ((x) | (~z)))
RL = lambda x,n: (((x) << (n)) | ((x) >> (32-(n))))

#FF= lambda a,b,c,d,x,s,ac:func

def FF(a, b, c, d, x, s, ac):
    a = (a+F ((b), (c), (d)) + (x) + (ac)&0xffffffff)&0xffffffff
    a = RL ((a), (s))&0xffffffff
    a = (a+b)&0xffffffff
    return a

def GG(a, b, c, d, x, s, ac):
    a = (a+G ((b), (c), (d)) + (x) + (ac)&0xffffffff)&0xffffffff
    a = RL ((a), (s))&0xffffffff
    a = (a+b)&0xffffffff
    return a

def HH(a, b, c, d, x, s, ac):
    a = (a+H ((b), (c), (d)) + (x) + (ac)&0xffffffff)&0xffffffff
    a = RL ((a), (s))&0xffffffff
    a = (a+b)&0xffffffff
    return a

def II(a, b, c, d, x, s, ac):
    a = (a+I ((b), (c), (d)) + (x) + (ac)&0xffffffff)&0xffffffff
    a = RL ((a), (s))&0xffffffff
    a = (a+b)&0xffffffff
    return a

FUNC=[FF,GG,HH,II]

S_DATA=[[7,12,17,22],[5,9,14,20],[4,11,16,23],[6,10,15,21]]
T_DATA=[0xd76aa478,0xe8c7b756,0x242070db,0xc1bdceee,0xf57c0faf,0x4787c62a,
		0xa8304613,0xfd469501,0x698098d8,0x8b44f7af,0xffff5bb1,0x895cd7be,
		0x6b901122,0xfd987193,0xa679438e,0x49b40821,0xf61e2562,0xc040b340,
		0x265e5a51,0xe9b6c7aa,0xd62f105d,0x2441453,0xd8a1e681,0xe7d3fbc8,
		0x21e1cde6,0xc33707d6,0xf4d50d87,0x455a14ed,0xa9e3e905,0xfcefa3f8,
		0x676f02d9,0x8d2a4c8a,0xfffa3942,0x8771f681,0x6d9d6122,0xfde5380c,
		0xa4beea44,0x4bdecfa9,0xf6bb4b60,0xbebfbc70,0x289b7ec6,0xeaa127fa,
		0xd4ef3085,0x4881d05,0xd9d4d039,0xe6db99e5,0x1fa27cf8,0xc4ac5665,
		0xf4292244,0x432aff97,0xab9423a7,0xfc93a039,0x655b59c3,0x8f0ccc92,
		0xffeff47d,0x85845dd1,0x6fa87e4f,0xfe2ce6e0,0xa3014314,0x4e0811a1,
		0xf7537e82,0xbd3af235,0x2ad7d2bb,0xeb86d391]

buf=[0x67452301,0xefcdab89,0x98badcfe,0x10325476]

def inFill(data):
	mul = ceil((len(data) + 16)/128)
	firlen = len(data)
	#print('mul : ', mul)
	if (len(data) + 16)%128 != 0:
		mul *= 128
		add = mul - len(data) - 16 - 1
		#print('add : ', add+3)
		data += '8'
		for cnt in range(add):
			data += '0'
	data += '%.2x'%(firlen*4)
	while(len(data)%128 != 0):
		data += '0'
	#print('data : ', data)
	#print('data len : ', len(data))
	return data

#_spilt = lambda st, wid: [st[i:i+wid] for i in range(0, len(st), wid)]
def _spilt(st, wid):
	return [st[i:i+wid] for i in range(0, len(st), wid)]
#getIntData = lambda lst: [int(item) for item in lst]
def getIntData(lst):
	return [int(item, 16) for item in lst]
def revData(lst):
	ret = []
	for item in lst:
		temp = _spilt(item, 2)
		temp.reverse()
		ret.append("".join(ch for ch in temp))
	return ret
def revInt(num):
	return ((num&0xff)<<24)|((num&0xff00)<<8)|((num&0xff0000)>>8)|(num&0xff000000)>>24
def showAns(tbuf):
	for i in tbuf:
		out = revInt(i)
		print("%.8x"%out, end='')
		#print('count 1 : ',bin(out).replace('0b','').count('1'))
		#print(bin(out).replace('0b','').zfill(32))

if __name__ == '__main__':
	inner = input("input > ")
	#in_data = getData(inner)
	#print(type(in_data))
	in_data = ''.join("%.2x" %ord(i) for i in inner)
	in_data = inFill(in_data)
	#print('in_data : ', in_data)
	in_data = _spilt(in_data, 128)
	for x in in_data:
		in_buf = _spilt(x, 8)
		in_buf = revData(in_buf)
		#print('in_buf : ', in_buf)
		#print('in_buf len : ', 	len(in_buf))
		in_buf = getIntData(in_buf)
		temp_buf = buf[:]
		for i in range(4):
		    for j in range(16):
		        inbufn=(i==0)*j+(i==1)*(1+5*j)%16+(i==2)*(5+3*j)%16+(i==3)*(7*j)%16
		        #print(-j%4, (1-j)%4, (2-j)%4, (3-j)%4, 16*i+j, inbufn)
		        temp_buf[-j%4]=FUNC[i](temp_buf[-j%4],temp_buf[(1-j)%4],temp_buf[(2-j)%4],temp_buf[(3-j)%4],in_buf[inbufn],S_DATA[i][j%4],T_DATA[i*16+j])
		        #print(hex(temp_buf[0]), hex(temp_buf[1]), hex(temp_buf[2]), hex(temp_buf[3]))
	#print('ans : ', hex(temp_buf[0]), hex(temp_buf[1]), hex(temp_buf[2]), hex(temp_buf[3]))
	for cnt in range(len(temp_buf)):
		temp_buf[cnt] += buf[cnt]
	showAns(temp_buf)
