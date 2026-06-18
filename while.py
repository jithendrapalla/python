#1. write a program to print n times python """
'''
n=int(input("enter"))
i=1
while i<=5:
    print("python")
    i+=1
   ''' 
#2. print n natural number
'''
n= int(input("enter"))
i=1
while i<=n:
    print(i)
    i+=1
    '''
#3. print n odd numbers
'''
n=int(input("ener"))
i=1
while i<=n:
    if i%2==1:
        print(i)
    i+=1
    '''
#4.  print n even number
'''
n=int(input("ener"))
i=1
while i<=n:
    if i%2==0:
        print(i)
    i+=1
    '''
#5. print sum of n natural number
'''
n=int(input("ener"))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print(sum)
'''
#6. print product of n natural number
'''
n=int(input("ener"))
i=1
product=0
while i<=n:
    product+=i   
    i+=1
print(product)
'''
#print product n even number
'''
n=int(input("ener"))
i=1
product=1
while i<=n:
    if i%2==0:
        product*=i
    i+=1
print(product)

#7. extract all lower case from string
s=input("ener any sring")
i=0
out=''
while i<len(s):
    if 'a'<=s[i]<='z':
        out+=s[i]
    i+=1
print(out)

#8. extract all aupper case
s=input("enter")
i=0
out=''
while i<len(s):
    if 'A'<=s[i]<='Z':
        out+=s[i]
    i+=1
print(out)

#9. exract all digits
s=input("ener")
i=0
out=''
while i<len(s):
    if '0'<=s[i]<='9':
        out+=s[i]
    i+=1
print(out)

#10. extract all spl charter
s=input("enter")
i=0
out=''
while i<len(s):
    if not('a'<=s[i]<='z' or 'A'<=s[i]<='Z' or '0'<=s[i]<='9'):
        out+=s[i]
    i+=1
print(out)

#11. extract integer vales from lsit
l=eval(input("entedr"))
i=0
out=[]
while i<len(l):
    if type(l[i])==int:
        out+=[l[i]]
    i+=1
print(out)

#12. extract all sring value from tuple
t=eval(input("enter"))
i=0
out=[]
while i<len(t):
    if type(t[i])==str:
        out+=[t[i]]
    i+=1
print(tuple(out))

#13. sring value from given list
l=eval(input("enter"))
i=0
out=[]
while i<len(l):
    if type(l[i])==str:
        out+=[l[i]]
    i+=1
print(out)

#14. etract complex from list
l=eval(input("enter"))
i=0
out=[]
while i<len(l):
    if type(l[i])==complex:
        out+=[l[i]]
    i+=1
print(out)

#15. sring value from given list only if it have a midele vakue
l=eval(input("enter"))
i=0
out=[]
while i<len(l):
    if len(l[i])%2==1:
        if type(l[i])==str:
            out+=[l[i]]
    i+=1
print(out)

l=eval(input("enter"))
i=0
out=[]
while i<len(l):
    if type(l[i])==list:
        if len(l[i][0])%2==1:
            if type(l[i][0])==str:
                out+=[l[i][0]]
    else:
         if len(l[i])%2==1:
            if type(l[i])==str:
                out+=[l[i]]
    i+=1
print(out)   
'''
#16. revice a number without using slicing and type cast
'''
num=int(input("enter"))
i=0
rev=0
while num>0:
    ld=num%10
    rev=rev*10+ld
    num=num//10
    i+=1
print(rev)
'''
#17 sum of iduval number
'''
num=int(input("enter"))
i=0
sum=0
while num>0:
    ld=num%10
    sum=sum+ld
    num=num//10
    i+=1
print(sum)
'''
#18 product of digts
'''
num=int(input("enter"))
i=0
product=1
while num>0:
    ld=num%10
    product*=ld
    num//=10
    i+=1
print(product)
'''
#19. extact all lower case and uppercase and digit and spl charete in 4 varables:
'''
s=input("enter")
i=0
up=''
lower=''
digt=''
spl=''
while i<len(s):
    if 'A'<=s[i]<='Z':
        up+=s[i]
    elif 'a'<=s[i]<='z':
        lower+=s[i]
    elif '0'<=s[i]<='9':
        digt+=s[i]
    else:
        spl+=s[i]
    i+=1
print("upper: ",up," lower: ",lower," digit: ",digt," spl: ",spl)
    '''
#20 . extract all sting values from given list if its start with upper case and end with digit
'''
s=eval(input("enter"))
i=0
out=[]
while i<len(s):
    if type(s[i])==str:
        if 'A'<=s[i][0]<='Z' and '0'<=s[i][-1]<='9':
            out+=[s[i]]
    i+=1
print(out)
'''
#21. revice a sring with out using slicig
'''
s=input("enter a string")
i=0
rev=''
while i<len(s):
    rev=s[i]+rev
    i+=1
print(rev)
'''
# or
'''
s=input("ener")
i=1
rev=''
while i<=len(s):
    rev=rev+s[-i]
    i+=1
print(rev)
'''
#22. extract all the lower chater from the give onluny if it's ask value is even
'''
s=input("ener")
out=''
i=0
while i<len(s):
    if ord(s[i])%2==0:
        if 'a'<=s[i]<='z':
            out+=s[i]
    i+=1
print(out)    
'''
#23. input is "abcd" out put is {a:97,b:98,c:99,d:100}
'''
s=input("enter")
i=0
d={}
while i<len(s):
    d[s[i]]=ord(s[i])
    i+=1
print(d)
'''
#24. input 'pthon' output {0:p,1:t,2:t,3:h,4:o,5:n}
'''
s=input("enter")
i=0
out={}
while i<len(s):
    out[i]=s[i]
    i+=1
print(out)
'''
#25.Wap to print multiplication table for n. 
'''
n=int(input("enter"))
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1
 '''
#26.Wap to print all the characters of a string. 
'''
st=input("enter")
i=0
while i<len(st):
    print(st[i])
    i+=1
    '''
#27.Wap to print all the characters present at even index of a string. 
'''
st=input("ener")
i=0
while i<len(st):
    if i%2==0:
        print(st[i])
    i+=1
    '''
# 28. Wap to extract all the vowels present in a string. 
'''
st=input("enter")
i=0
while i<len(st):
    if st[i] in "aeiou":
        print(st[i])
    i+=1
    '''
#29. Wap to print factors of a integer number.
'''
num=int(input("enter"))
i=1
while i<=num:
    if num%i==0:
        print(i)
    i+=1    
'''
#30. Wap to check whether the number is perfect or not. 
'''
num=int(input("enter"))
sum=0
i=1
while i<num:
    if num%i==0:
        sum=sum+i
    i+=1
if sum==num:
    print("perfit")
else:
    print("not perfict")
    '''
#31. Wap to login to phonepe by entering correct otp.
'''
u_otp=int(input("enter otp"))
s_otp=829719
i=0
while i<3:
    if u_otp==s_otp:
        print("welcom")
    else:
        print("miss mach otp try agin")
        u_otp=int(input("enter"))
    if i==2:
        print("u loss tree chances")
    i+=1
'''
#32. Wap to run infinite loop until user enters the correct password. 
'''
u_password=input("enter your password")
s_password='Jithu@829719'
i=0
count=1
while i<count:
    if u_password==s_password:
        print("wellcome")
    else:
        print("incorret password")
        u_password=input("enter agin")
        count=count+1
    i+=1
    '''
#33. Wap to extaract all the even integers present in a tuple at odd index.   
'''
t=eval(input("enter"))
i=0
out=()
while i<len(t):
    if i%2==1:
        if t[i]%2==0 and t[i]>0:
            out+=(t[i],) 
    i+=1
print(out)
'''
#34. Wap to remove duplicates from a list without converting into set. 
'''
l=eval(input("enter"))
nd=[]
i=0
while i<len(l):
    if l[i] not in nd:
        nd=nd+[l[i]]
    i+=1
print(nd)
'''
#35. Wap to find the greatest number in a given list of integers.
'''
l=eval(input("enter"))
i=0
big=0
while i<len(l):
    if l[i]>big:
        big=l[i]
    i+=1
print(big)
'''
#36. Wap to find the sum of cube of a number in a string
'''
s=input("enter")
num=''
i,sum,n=0,0,0
while i<len(s):
    if '0'<=s[i]<='9':
        sum=sum+((int(s[i]))**3) 
    i+=1
print(sum)
'''
#37. Wap to check whether the number is Armstrong or not.   
'''
num=int(input("enter"))
l=len(str(num))
i,sum,temp=0,0,num
while i<l:
    ld=num%10
    sum=sum+(ld**l)
    num=num//10
    i+=1
if sum==temp:
    print("amstring")
else:
    print("not")
    '''
#38. Wap to get the following output. A=’10011100’ B=’00110101’ out=4(count of positions having same values)
'''
A=input("enter A")
B=input("enter B")
i,count=0,0
while i<len(A):
    if A[i]==B[i]:
        count+=1
    i+=1
print(count)
    '''
#39. Wap to check the given number is prime or not. 
'''
num=int(input("enter"))
i,count=1,0
while i<=num:
    if num%i==0:
        count+=1
    i+=1
if count==2:
    print("prime")
else:
    print("not")
'''
#40. Wap to check whether the number is palindrome or not. 
'''
num=int(input("enter"))
i,rev=0,0
while num>0:
    ld=num%10
    rev=rev*10+ld
    num//=10
    i+=1
if num==rev:
    print("poly")
else:
    print("not")
'''
#41. Wap to find the HCF of two numbers. 
'''
A=int(input("enter A"))
B=int(input("enter B"))
i=1
a=[]
b=[]
while i<=A:
    if A%i==0:
        a=a+[i]
    i+=1
j=1
while j<=B:
    if B%j==0:
        b=b+[j]
    j+=1
max_f=max(a,b)
min_f=min(a,b)
hcf=[]
k=0
while k<len(max_f):
    if min_f[k] in max_f:
        hcf=hcf+[min_f[k]]
    k+=1
print(max(hcf))
'''
#or
'''
a=int(input("enter A"))
b=int(input("enter B"))
while b!=0: 
    a,b=b,a%b
print(a)
'''
#42. Wap to convert binary to decinaml. 
'''
s=input("enter")
i=1
count=0
decimal=0
while i<=len(s):
    if s[-i]=='1':
        decimal=decimal+(2**count)
    count+=1
    i+=1
print(decimal)
'''
#43. Wap to convert decimal to binary.
'''
num=int(input("enter"))
i=0
bi=''
while num!=0:
    bi=str(num%2)+bi
    num//=2
print(bi)
'''
#44.Wap to count the number of words in a string. 
'''
s=input("enter")
i,count=0,1
while i<len(s):
    if s[i]==' ':
        count+=1
    i+=1
print(count)
    '''
#45.Wap to find the product of all the digits present in a number
'''
num=int(input("ener"))
i,product=0,1
while num>0:
    ld=num%10
    product=product*ld
    num//=10
    i+=1
print(product)
        '''
#46. Wap to find the common elements in two sets 
'''
set1=eval(input("enter set1"))
set2=eval(input("enter set2"))
i=0
comm=[]
l=list(set1)
while i<len(set1):
    if l[i] in set2:
        comm+=[l[i]]
    i+=1
print(set(comm))
'''
#47. Wap to toggle a string. 
'''
s=input("enter")
i=0
out=''
while i<len(s):
    if 'a'<=s[i]<='z':
        out+=chr(ord(s[i])-32)
    elif 'A'<=s[i]<='Z':
        out+=chr(ord(s[i])+32)
    else:
        out+=s[i]
    i+=1
print(out)
    '''
#48. Wap to guess the number.
import random
num=int(input("enter"))
s_num=random.randint(1,10)
while True:
    if num==s_num:
        print("congratulations ")
        break
    elif num>s_num:
        print("guess a smaller number")
    else:
        print("guess a bigger number")
    num=int(input("enter agin"))   
    
    
