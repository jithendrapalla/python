'''Simple If: 
1. Wap to print the square of a number only if it is even. 
2. Wap to check whether the character is vowel or not. 
3. Wap to print Ascii value of a character only if it is upper case. 
4. Wap to print the cube of a number only if it is divisible by 9 or 6. 
5. Wap to check whether the given integer is 3 Digit number. 
6. Wap to check whether the last digit of a given number is 5. 
7. Wap to check whether the given data is float.  
8. Wap to check whether the data is single value data. 
9. Wap to check whether the given character is digit or not. 
10.Wap to check whether the given integer is multiple of 3. 
If else: 
11.Wap to check whether the data is mutable or not. 
12.Wap to check whether the given character is digit or not. 
13.Wap to check whether the given character is special or not. 
14.Wap to check whether a list consists of middle value or not. 
15.Wap to check whether the number is even or odd. 
16.Wap to check whether the given data is mutable or immutable. 
17.Wap to check whether 2 values are pointing to the same memory or not. 
18.Consider a tuple of length 2 and check whether the tuple is homogenous or not. 
19.Wap to check whether the string is palindrome or not. 
20.Wap to check whether the number is positive or negative.  '''

'''
#1. Wap to print the square of a number only if it is even. 
num=int(input('enter any number:'))
if num%2==0:
    print(num**2)

#2. Wap to check whether the character is vowel or not. 
ch=input('enter anu one char:')
if ch.lower() in ['a','e','i','o','u']:
    print('vowel')
    
#3. Wap to print Ascii value of a character only if it is upper case. 
ch=input('enter anu one char:')
if ch.isupper():
    print(ord(ch))
    
ch=input('enter anu one char:')
if 'A'<=ch<='Z':
    print(ord(ch))

#4. Wap to print the cube of a number only if it is divisible by 9 or 6. 
num=int(input("enter any number:"))
if num%9==0 or num%6==0:
    print(num**3)

#5. Wap to check whether the given integer is 3 Digit number. 
num=int(input("enter any number:"))
if 0<num>99:
    print("the given number is 3 digt")

#6. Wap to check whether the last digit of a given number is 5. 
num=int(input("enter any number:"))
#last_diit=num-(num//10)*10
#if last_dlit==5
if num%10==5:
    print("last diggit is 5")

#7. Wap to check whether the given data is float. 
num=eval(input("enter any value"))
if type(num)==float:
    print("float")  

#8. Wap to check whether the data is single value data. 
data=eval(input("enter data"))
if type(data) not in [list,tuple,set,dict,str]:
    print("single value")

#9. Wap to check whether the given character is digit or not.   
data=eval(input("enter data"))
if type(data)==int:
    print("digit")
   
#10.Wap to check whether the given integer is multiple of 3. 
num=int(input("enter any integer:"))
if num%3==0:
    print("is multipule of 3") 
    
#11.Wap to check whether the data is mutable or not. 
data=eval(input("enter data"))
if type(data) in [list,set,dict]:
    print(data,"given data is mutable")
else:
    print(data,"the given data is not a muable")

#12.Wap to check whether the given character is digit or not. 
ch=input("enter any ch")
if '0'<=ch<='9':
    print("digit")
else:
    print("not a digit")
    
#13.Wap to check whether the given character is special or not. 
ch=input("enter any ch")
if not('A'<=ch<='Z' or 'a'<=ch<='z' or '0'<=ch<='9'):
    print('spl')
else:
    print("not a spl")

#14.Wap to check whether a list consists of middle value or not. 
ele=eval(input("enter list"))
if len(ele)%2==1:
    print("middle")
else:
    print("no middele")

#15.Wap to check whether the number is even or odd. 
num=int(input("eneter any vale"))
if num%2==0:
    print("evn")
else:
    print("odd")

#16.Wap to check whether the given data is mutable or immutable.
data=eval(input("enter data"))
if type(data) in [list,set,dict]:
    print('mutabule')
else:
    print('immuablue')

#17.Wap to check whether 2 values are pointing to the same memory or not. 
a=eval(input('enter any value for a:'))
b=eval(input('enter any value for b:'))
if id(a)==id(b):
    print('saring same memory')
else:
    print('not same memory')
   
#18.Consider a tuple of length 2 and check whether the tuple is homogenous or not. 
t=eval(input("enter any tapule"))
if type(t[0])==type(t[1]):
    print("homogines")
else:
    print("not an homogines")

#19.Wap to check whether the string is palindrome or not. 
str1=input("enetr string")
if str1==str1[::-1]:
    print("polindrome")
else:
    print('not')
  
#20.Wap to check whether the number is positive or negative.  
num=int(input("enter any number"))
if 0<num:
    print("possive")
else:
    print("nagative")'''