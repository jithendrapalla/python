#1. s=saravi is a good girl op={'saravi': ['aai', 3], 'is': ['i', 1], 'a': ['a', 1], 'good': ['oo', 2], 'girl': ['i', 1]}
'''
s=input("enter")
out={}
for i in s.split():
    voal=''
    for j in i:
        if j in 'aeiouAEIOU':
            voal+=j
    out[i]=[voal,len(voal)]
print(out)
'''
'''
111. Wap to get the following output. without length function. S=’power star’ Out={‘power’:5,’star’:4} 
112. Wap to get the following output. S=’power star’ Out={‘power’:2,’star’:1} (no of vowels is key) 
113. Wap to get the following output. S=’kabab is love’ Out={‘kabab’:[‘babak’,2,’kbb’],’is’:[‘si’,1,’i’],
’love’:[‘evol’,2,’lv’]} [reverse,no of vowels,char at even index] 
114. Wap to get the following output. S=’kabab is love’ Out={‘kb’:(‘kbb’,3,’bbk’),’is’:(‘s’,1,’s’),’le’:(‘lv’,2,’vl’)}
{ 1st+last char: (consonant,no of consonant,rev of consonant)} 
115.Wap to get the following output. In=[100,200,35,40,60] Out=[335,235,400,395,375] (total sum-value)
116. Wap to get the following output. In=’bacbcaabbaa’ Out=’b4a5c2’ 
117. Wap to get the following output In=[100,200,50,400,300] N=300 Out=[[100,200],[300]] 
118.Wap to check whether the number is strong or not. 
119.Wap to get the following output. In={10:’star’,20:’bye’,30:’moon’,40:’apple’} Out={10:’a’,20:’e’,30:’oo’,40:’ae’}
120. Wap to get the following output. In=[‘hello’,227,3.4,’last’,189,34] Out=[722,981,43]
'''
#2. Wap to get the following output. without length function. S=’power star’ Out={‘power’:5,’star’:4}
'''
s=input("enter")
out={}
for i in s.split():
    count=0
    for j in i:
        count+=1
    out[i]=count
print(out)
'''
#112. Wap to get the following output. S=’power star’ Out={‘power’:2,’star’:1} (no of vowels is value)
'''
s=input("enter")
out={}
for i in s.split():
    count=0
    for j in i:
        if j in 'aeiouAEIOU':
            count+=1
    out[i]=count
print(out)
'''
#113. Wap to get the following output. S=’kabab is love’ Out={‘kabab’:[‘babak’,2,’kbb’],’is’:[‘si’,1,’i’],
#’love’:[‘evol’,2,’lv’]} [reverse,no of vowels,char at even index]
'''
s=input("enter")
out={}
for i in s.split():
    count=0
    for j in i:
        if j in "AEIOUaeio":
            count+=1
        out[i]=[i[::-1],count,i[0::2]]
print(out)
'''
#114. Wap to get the following output. S=’kabab is love’ Out={‘kb’:(‘kbb’,3,’bbk’),’is’:(‘s’,1,’s’),’le’:(‘lv’,2,’vl’)}
#{ 1st+last char: (consonant,no of consonant,rev of consonant)}
'''
s=input("enter")
out={}
for i in s.split():
    count=0
    vow=''
    for j in i:
        if j not in 'AEIOUaeiou':
            vow+=j
            count+=1
        out[i[0]+i[-1]]=(vow,count,vow[::-1])
print(out)
'''        
#115.Wap to get the following output. In=[100,200,35,40,60] Out=[335,235,400,395,375] (total sum-value)
'''
e=eval(input("emter list"))
out=[]
for i in e:#[100,200,35,40,60]
    su=0
    for j in e:
        if j!=i:
            su+=j
    out=out+[su]
print(out)
'''
#116. Wap to get the following output. In=’bacbcaabbaa’ Out=’b4a5c2’
'''
s=input("ener")
out=''
for i in s:
    if i not in out:
        cout=0
        for j in s:
            if i==j:
                cout+=1
        out=out+i+str(cout)
print(out)
'''
#117. Wap to get the following output In=[100,200,50,400,300] N=300
#Out=[[100,200],[300]]
'''
l=eval(input("enter"))
n=int(input("enter"))
out=[]
for i in l:
    if i==n:
        out+=[[i]]
    for j in l:
        if i<j and i+j==n:
            out+=[[i,j]]
print(out)
'''
#118.Wap to check whether the number is strong or not.
'''
num=int(input("enter"))
temp=num
sum1=0
while num>0:
    ld=num%10
    pro=1
    for i in range(1,ld+1):
        pro*=i
    sum1+=pro
    num//=10
if sum1==temp:
    print("strong")
else:
    print("not")
'''
#119.Wap to get the following output. In={10:'star',20:'bye',30:'moon',40:'apple'}
#Out={10:’a’,20:’e’,30:’oo’,40:’ae’}
'''
s=eval(input("enter"))
out={}
for i in s:
    val=''
    for j in s[i]:
        if j in 'aeiouAEIOU':
            val+=j
    out[i]=val
print(out)
'''
#120. Wap to get the following output. In=['hello',227,3.4,'last',189,34]
#Out=[722,981,43]
'''
s=eval(input("ener"))
out=[]
for i in s:
    rev=0
    if type(i)==int:
        while i>0:
            ld=i%10
            rev=rev*10+ld
            i//=10
        out+=[rev]
print(out)
'''
                









        
