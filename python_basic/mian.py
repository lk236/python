#ctrl+/-->一键注释
# coding=utf-8 | gbk '第一行'
"""
a=100
b=50
print(a)
print(a,b)
print(chr(98))
print('98')
print(ord('21271'))
"""
'''
fp=open('note.txt',"w")
print('北京欢迎你',file=fp)
fp.close()
'''
'''
print('beijing',end='-->')
print('欢迎你')
print('北京欢迎您'+'2025')
'''
'''
name=input('请输入您的姓名：')
print('我的姓名是：'+name)
num=input('数字：')
num=int(num)
print(num)
'''
# 你好
'''
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
lk=123
print(type(lk))
lk=pk=444
print(lk,pk)
print(id(lk))
print(id(pk))
PI=3.1415926  #常量
'''
'''
num1=123
num2=0b10111
num3=0o7654
num4=0xfae
print(num1,num2,num3,num4)
x=1.99E1413
print(x)
print(0.1+0.2)
print(round(0.1+0.2,1))
x=123+456j
print(x.real)
print(x.imag)
'''
'''
print(info)
print('nihao')
print('beijing')
print('\'\'\"\"')
print(r'\'\'\"\"')
print(R'\'\'\"\"')
'''
'''
s='helloworld'
print(s[0],s[-10])
print('hello'[1])
print(s[2:7])#2开始不包含7
x='2022年'
y='2022年你好'
print(x+y)
print(x*3)
print(x in y)
print("北京" in y)
'''
'''
x=True
print(x)
print(x+10)
print(False+10)
print(bool(10))
print(bool(x))
print(bool(0.0))
print(bool('你好'))
print(bool(''))
print(int(3.14))
print(ord('杨'))
print(chr(26472))
print(hex(15)) #10->16
print(oct(15)) #10->8
print(bin(15)) #10->2
'''
'''
s='3.14+4'
print(s,type(s))
x=eval(s)#去引号,转类型
print(s,type(x))
hello="你好"
print(hello)
print(eval('hello'))
'''
#print(1+2,2-1,2*2,10/3,10//3,2**3,10%3)
#+=，-=，/=，//=，*=，**=
#>,<,>=,<=,!=,==
#and,or,not
#位与&，位或|，位异或^(同0异1),位取反~，左移位<<,右移位>>
'''

a=b=c=d=100
a,b,c,d='book'
print(a)
print(b)
print(c)
print(d)
a=100
if a%2 == 0:
    print('a是偶数')
answer = input('请问你喝酒了吗？输入\'y\'或\'n\')：')
if answer == 'y':
    num = eval(input("请输入酒精含量:"))
    if num < 20:
        print('没酒驾')
    elif num < 80:
        print('构成酒驾')
    else:
        print('构成醉驾')
elif answer == 'n':
    print('没事了')
name=input('输入用户名：')
pwd=input('输入密码：')
if name=='lk' and pwd=='12345':
    print('成功登录！')
else:
    print('失败，请重试！')
score=input('输入成绩：')
match score:
    case 'A':
        print('优秀')
    case 'B':
        print('良好')
    case 'C':
        print('及格')     
for i in 'hello':
    print(i)
    s=0
for i in range(1,11) :
    s+=i#1到10
    if i%2==0:
        print(i,"是偶数")
    else :
        print('累加和为：',s)
s=0
i=1
while i<=100:
    s+=i
    i+=1
print("累加和",s)
'''
'''
for i in range(1,4):
    for j in range(1,5):
        print('*',end='')
    print()
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print()
for i in range(1,6):
    for j in range(1,7-i):
        print('*',end='')
    print()
for i in range(1,6):
    for j in range(1,6-i):
        print(' ', end='')
    for k in range(1, i * 2):
        print('*', end='')
    print()
s=0
i=1
while i<10:
    s+=i
    if s>20:
        print("当前i为：",i)
        break
    i+=1
'''
'''
#break,continue,pass
for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+'*'+str(i)+'='+str(i*j),end='\t')
    print()
import random
rand=random.randint(1,100)
count=0
while count<10:
    num = eval(input('请输入一个数：'))
    if num == rand:
        print('猜对了')
        count += 1
        break
    elif num < rand:
        print('猜小了')
    else:
        print('猜大了')
    count+=1
print('猜了',count,'次')
'''
"""
s='helloworld'
for i in range(0,len(s)):
    print(i,s[i],end='\t\t')
print()
for i in range(-len(s),0):
    print(i,s[i],end='\t\t')
print()
s1=s[0:5:1]
print(s1)
s2=s[::-1]
print(s2)
s3=s[-1:-11:-1]
print(s3)
fw=s.index('l') #第一次出现位置
print(fw)
c=s.count('l')  #出现次数
print(c)
"""
"""
#列表
lst1=['hello','world',123,10]
lst2=list('helloworld')
lst3=list(range(1,10,2))
print(lst1)
print(lst2)
print(lst3)
print(lst2*2)
print(lst1+lst2+lst3)
del lst3
for item in lst2:
    print(item)
for i in range(0,len(lst1)):
    print(1,'->',lst2[i])
for index,item in enumerate(lst1) :
    print(index,item)
for index,item in enumerate(lst1,start=1) :#start可省略
    print(index,item)
"""
import random
# lst=[item for item in range(1,11)]
# print(lst)
# lst=[random.randint(1,100) for _ in range(10)]
# print(lst)
# lst=[i for i in range(10) if i%2==0]
# print(lst)
# lst=[
#     ['城市','环比','同比'],
#     ['北京','102','504'],
#     ['上海','104','504'],
#     ['深圳','100','39']
# ]
# print(lst)
# for row in lst:
#     for item in row:
#         print(item,end='\t')
#     print()
# lst2=[[j for j in range(5)]for i in range(4)]
# print(lst2)
'元组'
# t=('hello',[10,20,30],'python')
# print(t)
# t=tuple('helloworld')
# print(t)
# t=tuple([10,20,30,40,10])
# print(t)
# print(10 in t)
# print(max(t))
# print(t.index(10))
# print(t.count(10))
# t1=(10)#int
# t2=(10,)#元组
# del t
# t=('hello','good','python')
# print(t[0])
# print(t[0:3:2])
# for item in t:
#     print(item)
# for i in range(len(t)):
#     print(i,t[i])
# for index,item in enumerate(t):
#     print(index,'---->',item)
# for i,j in enumerate(t):
#     print(i,'--->',j)
# t=(i for i in range(1,4))
# print(t)
# t=tuple(t)
# print(t)
# for item in t :
#     print(item)
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())
'字典'
# d={10:'cat',20:'dog',20:'dog'}
# print(d)
# lst1=[10,20,30,40]
# lst2=['cat,''dog','pet','zoo','car']
# zipobj=zip(lst1,lst2)
# print(zipobj)   #<zip object at 0x0000025C88A63140>
# print(list(zipobj)) # [(10, 'cat,dog'), (20, 'pet'), (30, 'zoo'), (40, 'car')]
# d=dict(zipobj)
# print(d)        # {10: 'cat,dog', 20: 'pet', 30: 'zoo', 40: 'car'}
# d=dict(cat=10,dog=20)
# print(d)
# t=(10,20,30)
# print({t:10})#元组可以作字典
# lst=[10,20,30]
# print({lst:10})#列表不行
# d={10:'cat',20:'dog',20:'dog'}
# print(d[10])#key不存在会报错
# print(d.get(10))#可以指定默认值，None
# print(d.get(12,'不存在'))#输出不存在
# for item in d.items():
#     print(item)
# for key,value in d.items():
#     print(key,'-->',value)
# d={10:'cat',20:'dog',30:'pig'}
# print(d)
# d[40]='duck'
# print(d)
# keys=d.keys()
# print(keys)#dict_keys([10, 20, 30, 40])
# print(list(keys))#[10, 20, 30, 40]
# print(tuple(keys))#(10, 20, 30, 40)
# values=d.values()
# print(values)
# print(list(values))
# print(tuple(values))
# lst=list(d.items())
# print(lst)
# d=dict(lst)
# print(d)
# print(d.pop(20))
# print(d)
# print(d.pop(50,'不存在'))
# print(d.popitem())#随机删除
# print(d)
# d.clear()#清空
# print(d)
# print(bool(d))
# import random
# d={item :random.randint(1,100) for item in range(4)}
# print(d)
# lst1=[10,20,30,40]
# lst2=['cat,''dog','pet','yes']
# d={key:value for key,value in zip(lst1,lst2)}
# print(d)
'集合'
# s={10,20,30,40}
# print(s)#{40, 10, 20, 30}无序,不能存储列表
# s=set()
# print(s)#set()空集合
# s={}
# print(s,type(s))#{} <class 'dict'>,创建的是字典
# s=set('helloworld')
# print(s)#{'w', 'l', 'd', 'e', 'r', 'h', 'o'},无序不重复
# s=set([10,20,30])
# print(s)#{10, 20, 30}
# s=set(range(1,10))
# print(s)
#{1, 2, 3, 4, 5, 6, 7, 8, 9}
#max,min,len,in,not in,del
#交&，并|，差-，补^
# A={10,20,30,40,50}
# B={30,50,66,77,20}
# print(A&B)
# print(A|B)
# print(A-B)
# print(A^B)
# s={10,20,30,40,50}
# s.add(60)
# print(s)
# s.remove(10)
# print(s)
# s.clear()
# print(s)
# s={10,20,30,40,50}
# for item in s:
#     print(item)
# for index,item in enumerate(s):
#     print(index,"-->",item)
# s={i for i in range(1,10)}
# print(s)
# s={i for i in range(1,10) if i%2==1}
# print(s)
