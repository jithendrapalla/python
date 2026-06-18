#write a program to loing to intagram
'''
username='jithu'
pasword='jithu@123'
us=input("enter user name")
if us==username:
    pas=input("enter password")
    if pas==pasword:
        print("login suciffully")
    else:
        print("worng password1")
else:
    print("worng user name")
    '''
#wap to chick the given data having a midele or no onlf if is list or tuple
'''
data=eval(input("enter a data"))
if type(data)== list or type(data)==tuple:
    if len(data)%2!=0:
        print("have a midel value")
    else:
        print("no midele value")
else:
    print("the given value is not a list or tuple")
    
'''
#ploindeom have the length 5
'''
data=eval(input("enter a data"))
rev=data[::-1]
if len(data)==5:
    if data==rev:
        print("polydrom")
    else:
        print("not a poly drom")
else:
    print("lenth is less  then 5")
    '''
#string is sring and its upper uppercase
'''
data=input("enter any string")
if data==data[::-1]:
    if 'A'<=data[0]<='Z':
        print("sart wih upper")
    else:
        print("not srart with upper")
else:
    print("not a poly drome")
    '''
#wap the give ch is vowel or consant.
'''
ch=input("enter any charter")
if len(ch)==1 and type(ch)==str:
    if ch in ['a','e','i','o','u','A','E','I','O','U']:
        print("the given cher is vowel")
    else:
        print("the given ch is not a vole")
else:
    print("its not a single charter or not a chrter ")
    '''
# gind biggerst among  4 number
'''
a=int(input("enter A value"))
b=int(input("enter B value"))
c=int(input("enter C value"))
d=int(input("enter D value"))
if a>=b:
    if a>=c:
        if a>=d:
            print("A is biggerst")
        else:
            print("D is biggerst")
    else:
        if c>=d:
            print("C is bigger")
        else:
            print("D is biggest")
else:
    if b>=c:
        if b>=d:
            print("B is biger")
        else:
        print("D is bigger")
    else:
       if c>=d:
            print("c is bigger")
        else:
            print("d is bigeer")
'''
#33. Wap to print the value as it is only if the length of the value is even. 
# print the values only the lenth is evan
'''
num=eval(input("enter any number"))
if len(num)%2==0:
    print(num)
else:
    print("not a even lenth")
'''
#34.Wap to print the last value of a list
#only if it is palindrome string starting with  vowel.
'''
l=eval(input("enter list vales only in string"))
if type(l)==list:
    if l[0]==l[0][::-1]:
        if l[0][0] in 'aeiouAEIOU':
            print("star with vowel")
        else:
            print("not start with vowel")
    else:
        print("not a poly")
else:
    print("not a list")
'''
#35.Wap to print the reversed string only if it is starting with vowel ,
#ending with  consonant and having a middle value.
'''
s=input("enter any string")
if s[0] in 'aeiouAEIOU':
    if s[-1] not in 'aeiouAEIOU':
        if len(s)%2==1:
            print(s[::-1])
        else:
            print("no middele value")
    else:
        print("ending with vowel")
else:
    print("not start with vowel")
'''
#36.Wap to find the second greatest of 4 values.
'''
a=int(input("enter A value"))
b=int(input("enter B value"))
c=int(input("enter C value"))
d=int(input("enter D value"))
if a>=b and a>=c and a>=c:
    if b>=c and b>=d:
        print(b)
    elif c>=d and c>=b:
        print(c)
    else:
        print(d)
elif b>=a and b>=c and b>=d:
    if a>=c and a>=d:
        print(a)
    elif c>=a and c>=d:
        print(c)
    else:
        print(d)
elif c>=a and c>=b and c>=d:
    if a>=b and a>=d:
        print(a)
    elif b>=d and b>=a:
        print(b)
    else:
        print(d)
else:
    if a>=c and a>=b:
        print(a)
    elif b>=a and  b>=c:
        print(b)
    else:
        print(c)
'''
#37.Wap to find the smallest of 4 numbers.
'''
a=int(input("enter A value"))
b=int(input("enter B value"))
c=int(input("enter C value"))
d=int(input("enter D value"))
if a<=b and a<=c and a<=c:
    if b<=c and b<=d:
        print(b)
    elif c<=d and c<=b:
        print(c)
    else:
        print(d)
elif b<=a and b<=c and b<=d:
    if a<=c and a<=d:
        print(a)
    elif c<=a and c<=d:
        print(c)
    else:
        print(d)
elif c<=a and c<=b and c<=d:
    if a<=b and a<=d:
        print(a)
    elif b<=d and b<=a:
        print(b)
    else:
        print(d)
else:
    if a<=c and a<=b:
        print(a)
    elif b<=a and  b<=c:
        print(b)
    else:
        print(c)
    '''
#Write a program to print middle Character of the given string only if it
#is upper  Case Character.
'''
st=input("enter any string")
if 'A'<=st<='Z':
    if len(st)%2==1:
        mid=(len(st)//2)
        print(st[mid])
    else:
        print("nodidele value")
else:
    print("srat with not upper")
    '''
#wi



st=input("enter any sring")
midele=len(st)//2
if len(st)%2!=0 and 'A'<=st[midele]<='Z':
    if st==st[::-1]:
        print('the guiven string is poly')
    else:
        print("the given str is not a poly")
else:
    if len(st)==5:
        if 'A'<=st<='Z':
            print("upper")
        else:
            print("not a upper")
    else:
        print("not a length")
