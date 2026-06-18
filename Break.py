'''
us='jithu@123'
ps='123456'
a=0
while True:
    i_us=input("enter us")
    i_ps=input("enter ps")
    if us==i_us and ps==i_ps:
        print("wellcome")
        a=1
        break
    else:
        print("tri agin")
        '''
'''
s=20
while True:
    us=int(input("enter a number"))
    if s<us:
        print("your namuber is grater than my number")
    elif s>us:
        print("less then my number")
    elif s==us:
        print("yes")
        break
'''
'''
p1=['paper','rock','sic']
while True:
    if input("play agin y/n" )=='n':
        break
    p2=input("you r2 choice")
    if p2 =='paper':
        if p1[1]=='rock' and p2=='paper':
            print('p1 choice=',p1[1],' p1 win')
    elif p2=='rock':
        if p1[0]=='paper' and p2=='rock':
            print('p1 choice=',p1[0],'p1 win')
    elif p2=='sic':
        if p1[1]=='rock' and p2=='sic':
            print('p1 choice=',repr(p1[0]),'win p1')
'''
'''
import random
computer=['paper','rock','sic']
ch=random.choice(computer)
while True:
    if input("do you want to play again y/n")=='n':
        break  
    jithu=input("you jihu choice")
    print("computer choice",ch)
    if ch==jithu:
        print("draw")


    elif ch=='paper' and jithu=='rock':
        print("jithu lose")
    elif ch=='rock' and jithu=='sic':
        print("jithu lose")
    elif ch=='sic' and jithu=='paper':
        print("jithu lose")   
    else:
        print("jithu win")        
else:
    print("thank you for playing")        
'''
'''
for i in range(1,5):
    if i==3:
        continue
    print(i)
    '''
'''
l=[10,2.5,12]
for i in l:
    if type(i)!=int:
        continue
    print(i)
'''
#sll apl caher rom he given strng
'''
s=input("enter")
out=''
for i in s:
    if 'a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9':
        continue
    out+=i
print(out)
'''
#chick the given number is prime or not
'''
num=int(input("enter a number"))
for i in range(2,num):
    if num%i==0:
        print("the given number is no a prime")
        break
else:
    print("prime")
    '''

num=int(input("enter"))
count=0
i=2
while (num-1)>i:
    if num%i!=0:
        i+=1
        continue
    else:
        print('not prime')
        break
     
else:
    print('prime')
    
#chick the give string isloer case or not

'''
s=input("enter a string")
for i in s:
    if not('a'<=i<='z'):
        print("not all lower")
        break
else:
    print("all lower")
    '''
'''
s=input("enter a string")
i=0
while len(s)>i:
    if 'a'<=s[i]<='z':
        i+=1
        continue
    else:
        print("not lower")
        break
else:
    print("all lower")
    '''
    
#chick the give tuple is home or not
'''
t=eval(input("enter"))
for i in t:
    if type(t[i])!=type(t[0]):
        print("not homo")
        break
else:
    print("homo")
        '''
'''
t=eval(input("enter"))
i=0
while len(t)>i:
    if type(t[i])==type(t[0]):
        i+=1
        continue
    else:
        print("not homo")
        break
print(i)
#else:
#    print("homo")
    '''

        
