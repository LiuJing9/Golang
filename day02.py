# _*_ -coding:utf8-


# pow(x,y,z) and the z "(x**y)%z"
# max :: 1.single args 2. iter 
# round(x,y) :: 
# use tsinghua yuan install pip
# pip install xxx -i https://pypi.tuna.tsinghua.xxxxm, 
# math.log :: e  
# math.log(10,10)
# math.sin()  input huduzhi
# EP1:
'''
import math
:
x1, y1 = eval(input('输入A点坐标：'))
x2, y2 = eval(input('输入B点坐标：'))
x3, y3 = eval(input('输入C点坐标：'))

a = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
b = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
c = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)

A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

print('三角形的三个角分别为', A, B, C)

     
'''
a = '''
ajshbdfkajs
askhfbajsf
ashbfkajsb
aksfjbkj
'''
# 
# print(type(a))
# ord() input string, return ascii value
# chr()
# from __future__ import print_function
# loading  future package in print function
'''
res = ''
for i in 'maomaochong@163.com':
    res = res +  chr(ord(i) + 1)
    # print(res,end='')
print(res)'''


'''
import hashlib
str1 = 'this is a test.'
h1 = hashlib.md5()
h1.update(str1.encode(encoding = 'utf-8'))
print('MD5', h1.hexdigest())
'''


'''
import cv2  # 计算机视觉中的库 opencv
import hashlib # MD5 的hash 库
# 读取图片IMREAD_GRAYSCALE，以灰度打开
img = cv2.imread('/Users/huwang/Documents/other/photo/noePiece.jpg',cv2.IMREAD_GRAYSCALE)
print(img.shape) # 图片的形状
#显示转换为标准一维python bytearray
bytearray1 = bytearray(img)  # 将图片转换成字节型
# print(bytearray1)
# md5化
h1 = hashlib.md5()
h1.update(bytearray1)
print('MD5加密之后为：', h1.hexdigest())
'''
'''
a = "He said:\"Johon's program is easy to read\""  #z正则表达式中常用转义字符\
print(a)
'''
'''
str()   change typr to string
int()   ....        to int
float   ....        to float 
bool()  ....           bool

'''

'''
string:
    +   string +
    ''.join()
    ".join()" str class function
    join(iter):: 
        example:tuple(),list[],dict{key:value}
    print(str(8)+'mins'+','+str(20)+'seconds')

EP2:
    1.将 “Welcome” “to” "Python" 拼接
    2.将int型 100 与 “joker is a bad man” 拼接
    3.从控制台读取字符串输入一个名字返回夸奖此human

    answer:
        'welcome' + 'to' + 'Python'
        str(100) + 'joker is a good man'
        name = input('>>')  #return string
        print(name + 'ni zhen shi yi ge xiao tian cai')
'''



