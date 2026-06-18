'''
Elif:              
21. Wap to check whether the char is uppercase, lowercase, digit or special char. 
22. Wap to check whether the given integer is single digit or two digits or three  digits or more than three digits.
23.Wap to check the given points are lying in which quadrant. 
24. Wap to find the greatest of 3 numbers. 
25. Wap to find the smallest of 3 numbers. 
26.Wap to check the relation between two integer numbers. 
27. Consider a character input if it is uppercase convert it into lowercase, if it is lowercase convert it into uppercase,
    if it is digit print the reminder when it is divided by 3 else if it is special character print it’s ASCII value. 
28.Wap to print ‘Fizz’ if the given number is multiple of three print ‘buzz’ if the  given number is multiple of 5 and print
    ‘Fizzbuzz’ if the number is multiple of  both 3 and 5.
'''
'''
#21. Wap to check whether the char is uppercase, lowercase, digit or special char
ch=input("enter any charter:")
if 'A'<=ch<='Z':
    print("upper")
elif 'a'<=ch<='z':
    print("lower")
elif '0'<=ch<='9':
    print("digit")
else:
    print("spl")


#22. Wap to check whether the given integer is single digit or two digits or three  digits or more than three digits.
num=int(input("enter any number"))
if 0<=num<=9:
    print("single")
elif 10<=num<=99:
    print("two diit")
elif 100<=num<=999:
    print("three digit")
else:
    print("more thaan three")

#23.Wap to check the given points are lying in which quadrant.
x=int(input("enter x value:"))
y=int(input("enter y value:"))
if x>0 and y>0:
    print("Q1")
elif x<0 and y>0:
    print("Q2")
elif x<0 and y<0:
    print("Q3")
else:
    print("Q4")

#24. Wap to find the greatest of 3 numbers.
a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
if a>b and a>c:
    print("a is bigger")
elif b>c:
    print("b is bigger")
elif c>b:
    print("c is bigger")
else:
    print("theree number are equal")


#25. Wap to find the smallest of 3 numbers.
a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
if a<b and a<c:
    print("a is samll")
elif b<c:
    print("b is samller")
elif c<d:
    print("c is smaller")
else:
    print("theree number are equal")

#26.Wap to check the relation between two integer numbers.
a=int(input("enter a value"))
b=int(input("enter b value"))
if a>b:
    print("a is bigger")
else:
    print("b is bigger")

#27. Consider a character input if it is uppercase convert it into lowercase, if it is lowercase convert it into uppercase,
#    if it is digit print the reminder when it is divided by 3 else if it is special character print it’s ASCII value.
ch=input("enter any charete or numebr")
if 'A'<=ch<='Z':
    print(chr(ord(ch)+32))
elif 'a'<=ch<='z':
    print(chr(ord(ch)-32))
elif '0'<=ch<='9':
    print(int(ch)%3)
else:
    print(ord(ch))

#28.Wap to print ‘Fizz’ if the given number is multiple of three print ‘buzz’ if the  given number is multiple of 5 and print
#    ‘Fizzbuzz’ if the number is multiple of  both 3 and 5.
num=int(input("enter any number"))
if num%3==0 and num%5==0:
    print("Fizzbuzz")
elif num%5==0:
    print("Buzz")
elif num%3==0:
    print("Fizz")
else:
    print("the given number wii not divided ith 3 and 5")
'''
    

