#license test
'''age=int(input("what is your age"))
if age>=18:
    print("youre eligible for license")
else:
    print("not eligible for license")'''

#bigger number
'''num1=int(input("enter frist number"))
num2=int(input("enter second number"))    
if num1>num2:
    print(" frist number bigger")
elif num1<num2:
    print(" second number bigger")    
else:
    print("both number are equal")  '''
# number even or odd
'''num=int(input("enter a number"))
if num % 2==0:
    print("even number")
else:
    print("odd number")'''    

#grade checker
'''marks=int(input("enter the marks"))
if marks >= 90:
    print("grade A")
elif marks >= 75:
    print("grade B")
elif marks >=50:
    print("grade C")
else:
    print("fail")'''     

#login check
'''username=input("enter user name")
password=input("enter password") 

if username=="admin" and password=="1234":
    print("login succus ")
else:
    print("login failed")'''
#calculator
'''num1=int(input("enter a number"))
num2=int(input("enter a number"))
op= input("choose operation(+,-,*,/):")

if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)  
else:
    print("invaild")   '''           

#night , morning , evening , afternoon ,
T = int(input('enter the time (0-24):'))
if T < 0:
    print('invalid')
elif 0 <= T <=5:
    print('midnight')
elif 6 <= T <=11:
    print('morning')
elif 12 <= T <=17:
    print('afternoon')
elif 18<= T <=23:
    print('evening')
elif T == 24:
    print('night')
else:
    print('invalid')
