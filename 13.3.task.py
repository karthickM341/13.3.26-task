# 1 Bitwise operator.

#1. & opertor
a=10
b=6
c=a&b
print(c)
#2,| opertor
x=12
y=5
z=x|y
print(z)
#3.~ operator
num=8
print(~num)
#4.^ operator
a=15
b=9
c=a^b
print(c)
#5.<< operator
num=7
print(num<<2)
#6.>> operator
num=20
print(num>>1)
#7.& operator user input method
'''
a=int(input("num1:"))
b=int(input("num2:"))
c=a&b
print(c)
#8.XOR operator user input method
a=int(input("num1:"))
b=int(input("num2:"))
c=a^b
print(c)
'''

#2 string task
#9.task
word="hi"
print(word*4)
#10.task
word="python"
print(word*3)
#11.task
word1="super"
word2="man"
word=word1+word2
print(word)
#12.task
word1="hello"
word2=" "
word3="world"
word=word1+word2+word3
print(word)
#13.task
#name=input("Enter the name:")
#print(name*5)
#14.task
#name1=input("Enter the name1:")
#name2=input("Enter the name2:")
#name=name1+name2
#print("full name:",name)

#3. Input and Type casting task.
#15 .task
#name=input("enter the name:")
#print(type(name))
#16.task
#age=int(input("enter your age:"))
#print(type(age))
#17.task
num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
number=num1=num2
print("total number:"number)
#18.task
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
average=(a+b)/2
print("average:"average)
#19.task
a=int(input("number1:"))
b=int(input("number2:"))
print(3*a*2+b-2)
#20.task
number=input("enter your num:")
print("casting type:",type(number))
number=int(input("enter your num:"))
print("casting type:",type(number))

# Unit digit task
#21.task
number=input("enter the number:")
print("last number:",number[-1])
#22.task
number=int(input("enter the number:"))
print("number:",number%10)
#23.task
number=int(input("enter the number:"))
print("number:",number//10)
#24.task
number=input("enter the number:")
print("2nd last number:",number[-2])
#25.task
number=76859
print("last number:",number%10)

#if statement task
#26.task
if(10>=5):
    print("condition is true")
#27.task
num=int(input("enter your number:"))
if(num>50):
    print("condition is true")
#28.task
age=int(input("enter your age:"))
if(age>=18):
    print("your eligible")
#29.task
num=int(input("enter the num:"))
if(num>100):
    print("condition is true")
#30.task
num=int(input("enter your num:"))
if(num>=0):
    print("yes its true")

# if-else task
#31.task
num=int(input("number:"))
if(num==2):
    print("num is even")
else:
    print("num is odd")
#32.task
mark=int(input("enter your mark:"))
if(mark>=35):
    print("congrats you are pass")
else:
    print("you are fail")
#33.task
num=int(input("enter the num:"))
if(num>0):
    print("number is positive")
else:
    print("number is negative")
#34.task
num=int(input("enter the number:"))
if(num>10):
    print("numter is greater")
else:
    print("number is smaller")

# Nested if task
#35.job eligibility task
age=int(input("enter your age:"))
height=int(input("enter your height:"))
weight=int(input("enter your weight:"))
if(age>=18):
    if(height>=160):
        if(weight>=60):
            print("you are selected")
        else:
            print("weight is not enough")
    else:
        print("height is not enough")
else:
    print("age is not enough")
#36.college admission program
mark=int(input("enter your mark:"))
age=int(input("enter your age:"))
if(mark>=60):
    if(age>=17):
        print("your admission is accepted")
    else:
        print("age is not enough")
else:
    print("your mark is not enough")
#37.sports selection
age=int(input("enter your age:"))
height=int(input("enter your height:"))
weight=int(input("enter your weight:"))
if(age>=16):
    if(height>=150):
        if(weight>=50):
            print("you are selected")
        else:
            print("weight is not enough")
    else:
        print("height is not enough")
else:
    print("age is not enough")

# Match statement
#38.task
number=int(input("take a number(1-7):"))
match number:
    case 1:
        print("sunday")
    case 2:
        print("monday")
    case 3:
        print("tuesday")
    case 4:
        print("wednesday")
    case 5:
        print("thursday")
    case 6:
        print("friday")
    case 7:
        print("saturday")
#39.task
number=int(input("take a number(1-3):"))
match number:
    case 1:
        print("red")
    case 2:
        print("blue")
    case 3:
        print("green")
#40.task
number=int(input("take a number(1-4):"))
match number:
    case 1:
        print("apple")
    case 2:
        print("mango")
    case 3:
        print("orange")
    case 4:
        print("banana")


