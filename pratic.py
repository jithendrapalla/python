#1. in=AABCAAADA PO='AB' 'CA' 'AP'
'''
s=input("enter")
k=int(input("enter k value"))
a=''
for i in range(0,len(s)):
    if i%k==0 and i!=0:
        print(a)
        a=''
    if s[i] not in a:
        a+=s[i]
print(a)
'''
#find the prime numbers in a given range
'''
num=int(input("enter"))
for i in range(2,num+1):
    count=0
    for j in range(1,i):
        if i%j==0:
            count+=1
    if count==1:
        print(i)
        '''
#function without args and without return
#s='abc' out={'a':['a','A',97],'b':['b','B',98],'c':['c','C',99]}
'''
def s():
    a=input("enter")
    i=0
    out={}
    while i<len(a):
        out[a[i]]=[a[i],chr(ord(a[i])-32),ord(a[i])]
        i+=1
    print(out)
s()
'''
#s='hello' out={'h':'H','e':'E','i':'L','o',:O}
'''
def a():
    s=input("enter")
    i=0
    out={}
    while i<len(s):
        out[s[i]]=chr(ord(s[i])-32)
        i+=1
    print(out)
a()
'''
#s='hai' out={'h':'H104','a':'A97','i':'I105'}
'''
def a():
    s=input("enter")
    i=0
    out={}
    while i<len(s):
        out[s[i]]=chr(ord(s[i])-32)+str(ord(s[i]))
        i+=1
    print(out)
a()
'''
#2)function with argus and with out reun
#s='abc' out={'a':['a','A',97],'b':['b','B',98],'c':['c','C',99]}
'''
def a(s):
    i=0
    out={}
    while i<len(s):
        out[s[i]]=[s[i],chr(ord(s[i])-32),ord(s[i])]
        i+=1
    print(out)
st=input("enter")
a(st)
'''
#s='hello' out={'h':'H','e':'E','i':'L','o',:O}
'''
def a(s):
    i=0
    out={}
    while i<len(s):
        out[s[i]]=chr(ord(s[i])-32)
        i+=1
    print(out)
a(input("enter"))
'''
#s='hai' out={'h':'H104','a':'A97','i':'I105'}
'''
def a(s):
    i=0
    out={}
    while i<len(s):
        out[s[i]]=chr(ord(s[i])-32)+str(ord(s[i]))
        i+=1
    print(out)
a(input("enter"))
'''
#3)function with out argument and with retun
#s='abc' out={'a':['a','A',97],'b':['b','B',98],'c':['c','C',99]}
'''
def a():
    s=input("emter")
    i=0
    out={}
    while i<len(s):
        out[s[i]]=[s[i],chr(ord(s[i])-32),ord(s[i])]
        i+=1
    return out
print(a())
'''
#s='hello' out={'h':'H','e':'E','i':'L','o',:O}
'''
def a():
    s=input("enter")
    i=0
    out={}
    while i<len(s):
        out[s[i]]=chr(ord(s[i])-32)
        i+=1
    return out
print(a())
'''
#s='hai' out={'h':'H104','a':'A97','i':'I105'}
'''
def a():
    s=input("enter")
    i=0
    out={}
    while i<len(s):
        out[s[i]]=chr(ord(s[i])-32)+str(ord(s[i]))
        i+=1
    return out
print(a())
'''
#4)function with arrgument and with retun
##s='abc' out={'a':['a','A',97],'b':['b','B',98],'c':['c','C',99]}
'''
def a(s):
    i=0
    out={}
    while i<len(s):
        out[s[i]]=[s[i],chr(ord(s[i])-32),ord(s[i])]
        i+=1
    return out
print(a(input("enter")))
'''
#s='hello' out={'h':'H','e':'E','i':'L','o',:O}
'''
def a(s):
    i=0
    out={}
    while i<len(s):
        out[s[i]]=chr(ord(s[i])-32)
        i+=1
    return out
print(a(input("enter")))
'''
#s='hai' out={'h':'H104','a':'A97','i':'I105'}
'''
def a(s):
    i=0
    out={}
    while i<len(s):
        out[s[i]]=chr(ord(s[i])-32)+str(ord(s[i]))
        i+=1
    return out
print(a(input("enter")))
'''
