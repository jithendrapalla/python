#1.Wap to print all the integers present in a list
'''
n=eval(input("enter"))
out=[]
for i in n:
    if type(i)==int:
        out+=[i]
print(out)
'''
'''
n=eval(input("enter"))
out=[]
i=0
while i<len(n):
    if type(n[i])==int:
        out+=[n[i]]
    i+=1
print(out)
'''
#2.Wap to find the length of homogenous tuple without len().
'''
n=eval(input("enter"))
lenth=0
for i in n:
    lenth+=1
print(lenth)
'''
'''
n=eval(input("enter"))
lenth=0
while n:
    lenth+=1
    n=n[lenth:]
print(lenth)

'''


#3.Wap to extract all the even numbers present in a list.
'''
n=eval(input("enter"))
l=[]
for i in n:
    if type(i)==int:
        if i%2==0:
            l+=[i]
print(l)
'''
#4. Wap to remove duplicates from list
'''
n=eval(input("enter"))
n1=[]
for i in n:
    if i not in n1:
        n1+=[i]
print(n1)
'''
'''
n=eval(input("enter"))
for i in range(len(n)-1):
    for j in range(i+1,len(n)):
        if n[i]==n[j]:
            n.pop(i)
print(n)
'''
#5. Wap to reverse a string without using slicing.
'''
s=input("enter")
rev=''
for i in s:
    rev=i+rev
print(rev)
'''
#6. wap to extract all the lowercase characters in a string only if the ascii value is  even.
'''
n=input("enter")
out=''
for i in n:
    if ord(i)%2==0:
        if 'a'<=i<='z':
            out+=i
print(out)
'''
#7. Wap to check whether the last digit of an integer is even or not.
'''
n=eval(input("enter"))
for i in n:
    if type(i)==int:
        ld=i%10
        if ld%2==0:
            print(i ,"last is evan")
        else:
            print(i,"not")
'''
#8. Wap to extract all the key value pairs from the dictionary only if the keys are of string datatype and values are integers.
'''
n=eval(input("enter"))
out={}
for i in n:
    if type(i)==str:
        if type(n[i])==int:
            out[i]=n[i]
print(out)
'''
#9. Wap to extract key value pairs from the dictionary only if both keys and values are exactly same.
'''
n=eval(input("enter"))
out={}
for i in n:
    if i==n[i]:
        out[i]=n[i]
print(out)
'''
#10. Wap to get the following output using len function. S=’power star’ Out={‘power’:5,’star’:4}
'''
s=input("entter")
out={}
key=''
length=0
for i in s:
    if i!=' ':
        length+=1
        key+=i
    else:
        out[key]=length
        key=''
        length=0
if key!='':
    out[key]=length
print(out)
'''
#11. Wap to get the following output. S=’power star’ Out={‘power’:’rewop’,’star’:’rats’}
'''
n=input("enter")
out={}
for i in n.split(' '):
    out[i]=i[::-1]
print(out)
    '''
#12. wap to extract all the non default values from a list.
'''
n=eval(input("enter"))
non=[]
for i in n:
    t=type(i)
    if i!=t():
        non+=[i]
print(non)
'''
#or
'''
n=eval(input("enter"))
non=[]
for i in n:
    if bool(i)==True:
        non+=[i]
print(non)
'''
#13. Wap to check whether the list is homogenous or not.
'''
n=eval(input("enter"))
f=0
d=type(n[0])
for i in n:
    if type(i)!=d:
        f=1
        break
if(f==1):
    print("non")
else:
    print("homo")
    '''
#14. Wap to replace the space by * present in a string
'''
s=input("enter")
out=''
for i in s:
    if i!=' ':
        out+=i
    else:
        out+='*'
print(out)
        '''
#15. Wap to count the number of occurrence of a specified character.
'''
s=input("enter")
u=input("enter your char")
count=0
for i in s:
    if i==u:
        count+=1
print(u,'no og times:',count)
'''
#16. Wap to get the following output. S=’always keep smiling’ Out-‘syawla peek gnilims’
'''
s=eval(input("enter"))
out=''
for i in s.split():
    out=out+i[::-1]+' '
print(out)
'''
'''s=input("enter:")
out=''
for i in s:
    if n[i]==' ':

print(out)'''
#17. Wap to get the following output.   In=’push maadi kushi padi’ Out={‘push’:’ph’,’maadi’:’a’,’kushi’:’s’,’padi’:’pi’}
'''
n=eval(input("enter"))
d={}
for i in n.split():
    if len(i)%2!=0:
        d[i]=i[len(i)//2]
    else:
        d[i]=i[0]+i[-1]
print(d)
'''
#18.Wap to toggle a string
'''
s=input("enter")
out=''
for i in s:
    if 'a'<=i<='z':
        out+=chr(ord(i)-32)
    elif 'A'<=i<='Z':
        out+=chr(ord(i)+32)
    else:
        out+=i
print(out)
'''
#19. Wap extract upper, lower, digit and special characters present in a string to different.  output variable
'''
s=input("enter")
upper,lower,digit,spl='','','',''
for i in s:
    if 'A'<=i<='Z':
        upper+=i
    elif 'a'<=i<='z':
        lower+=i
    elif '0'<=i<='9':
        digit+=i
    else:
        spl+=i
print(upper,lower,digit,spl)
'''
#20. Wap to get the following output.   S=’hai hello ‘ Out={‘hai’:’ai’,’hello:’eo’}
'''
s=input("enter")
val=''
key=''
out={}
for i in s:
    if i!=' ':
        key+=i
        if i in 'aeiou':
            val+=i
    else:
        out[key]=val
        val=''
        key=''
if key!='':
    out[key]=val
print(out)
'''
#21. Wap to get the following output.   S=['http://jiocinema.com','http://file.py','web.html','http://amazom.com','http://www.org']
# Out=[‘com’,’py’,’html’,’org’]
'''
n=eval(input("enter"))
out=[]
for i in n:
    out+=[i.split('.')[-1]]
print(out)
'''
#22. Wap to get the following output.
# S=[‘http://jiocinema.com’,’http://file.py’,’web.html’,’http://amazom.com’,’http://www.org ’http://python.py’]
# Out={‘com’:[‘jiocinema’,’amazon’],’py’:[‘file’,’python’],’html’:[‘web’], ’org’:[‘www’]}
'''
n=eval(input("enter"))
out={}
for i in n:
    temp=i.split('http://')[-1]
    name=temp.split('.')[0]
    ex=temp.split('.')[-1]
    if ex not in out:
        out[ex]=[name]
    else:
        out[ex].append(name)
print(out)
'''
#23. Wap to get the following output.   L=['hai',34,3.4,'hello',90,'byebye'] Out={‘hai’:’hi’,’hello’:’ho’,’byebye’:’be’}
'''
n=eval(input("enter"))
out={}
for i in n:
    if type(i)==str:
        out[i]=i[0]+i[-1]
print(out)
'''
#24. wap to get the following output.   In=’hello’ Out={0:’h’,1:’e’,2:’l’,3:’l’,4:’o’}
'''
s=input("enter")
out={}
ind=0
for i in s:
    out[ind]=i
    ind+=1
print(out)
'''
#25. Wap to extract all the string values present in list only if the string is palindrome.
'''
n=eval(input("enter"))
out=[]
for i in n:
    if type(i)==str:
        if i==i[::-1]:
            out+=[i]
print(out)
'''
#26. Wap to return the positions of vowels present in the given string.
'''
s=input("enter")
pos=''
count=0
for i in s:
    if i in 'aeiouAEIOU':
        pos+=str(count)+' '
    count+=1
print(pos)
'''
#27. Wap to check whether the given collection is having nested collection or not.
'''
n=eval(input("enter"))
res=0
for i in n:
    if type(i) in (list,tuple,set,dict):
        res=1
if res==1:
    print("nested coll")
else:
    print("not")
'''
#28.Wap to count the number of words in a string.
'''
s=input("enter")
res=0
for i in s.split(' '):
    res+=1
print(res)
'''
#29. Wap to check whether the number is neon number or not.  N=9→9**2=81→8+1=9
'''
num=int(input("enter"))
temp=num
product=num**2
'''
#30. Wap to find the longest word in a string.
'''
s=input("enter")
longest=''
sam=0
big=1
for i in s.split():
    big=len(i)
    if big>sam:
        big=big
        longest=i
    else:
        sam=big
        longest=i
print(longest)
'''
#31. Wap to replace the special character present in a string by space.
'''
s=input("enter")
count=0
out=''
for i in s:
    if not('A'<=i<='Z' or 'a'<=i<='z' or '0'<=i<='9'):
        out+=' '
    else:
        out=out+i
print(out)
        '''
#32. wap to print the square of all the integers present in a list.
'''
n=eval(input("enter"))
squ=[]
for i in n:
    if type(i)==int:
        squ+=[i**2]
print(squ)
'''
#33. Wap to extract all the odd number present at even index from a list.
'''
n=eval(input("enter"))
odd=[]
index=0
for i in n:
    if type(i)==int:
        if i%2==1:
            if index%2==0:
                odd+=[i]
    index+=1
print(odd)
'''
#34.  Wap to extract all the mutable values present in a tuple.
'''
n=eval(input("enter"))
out=()
for i in n:
    if type(i) in (list,set,dict):
        out+=(i,)
print(out)
'''
#35. Wap to get the following output.   In=’10100011231’ Out=’010111000’ ( 0→1 and 1→0 if it is other than 0 &1 ignore)
'''
s=input("enter")
out=''
for i in s:
    if i=='0':
        a='1'
        out+=a
    elif i=='1':
        b='0'
        out+=b
print(out)
        '''
#36. Wap to get the following output.   In=’abacbaacc’ Out={‘a’:4,’b’:2,’c’:3}
'''
s=input("enter")
out={}
for i in s:
    if i not in out:
        out[i]=1
    else:
        out[i]+=1 #out[i]=out[i]+1
print(out)
'''
#37. wap to extract keyvalue pair from the dictionary only if the key is Boolean datatype.
'''
n=eval(input("enter"))
out={}
for i in n:
    if type(i)==bool:
        out[i]=n[i]
print(out)
'''
#38. Wap to get the following output.   In=’127342’ Out=’242173’ (extract even and odd digits separately and concatenate both)
'''
n=input("enter")
even=''
odd=''
for i in n:
    if i in '02468':
        even+=i
    elif i in '13579':
        odd+=i
print(even+odd)
'''
#39. Wap to checek whether the string is having only lowercase or not using continue.
'''
n=input("enter")
a=''
for i in n:
    if 'a'<=i<='z':
        continue
        a+=i
    else:
        a+=i
        break
if a=='':
    print("only lower")
else:
    print("not only lower")
    '''
#40. Wap to find the sum square of individual digits of a string
'''
s=input("enter")
sum=0
for i in s:
    if i in '0123456789':
        sum+=int(i)**2
print(sum)
'''
#41.ip='AbcdeFghij' op=[lower_case only]
'''
s=input("enter")
out=[]
for i in s:
    if 'a'<=i<='z':
        out+=i
print(out)
'''

'''
n=eval(input('entrer tuple'))
c=0
while n:
        c+=1
        n=n[1:]
print(c)
   '''
'''
s=input("enter")
lower=s.lower()
out=set()
for i in lower:
        if 'a'<=i<='z':
                out.add(i)
print(out)
if len(out)==26:
       print('panagram')
else:
        print('not panagram')
        '''

    