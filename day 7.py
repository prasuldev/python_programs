#learn varibale + print    
'''name=("prasuldev")
age=23
print(name)
print(age)'''

#learn input()
'''name=input("enter your name")
age=input("enter your age")
print(name)
print(age)'''

#learn numbers+simple math
a=10
b=100
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)

#learn if/else making decision
age=int(input("enter your age"))
if age>=28:
    print("youre eligible for marriage")
else:
    print("youre not eligible for marriage")

#learn loops
for i in range(10):
    print(i)

#learn a list
fruits=["apple,banana,orange"]
print(fruits)
print(fruits[0])
print(fruits[1])

#learn append to a list
fruits=["apple,banana,orange"]
fruits.append("grape")
print(fruits)

#creta a function that use list
def add_fruits(fruits):
    fruits.append(banana)
my_fruits=["apple,grape,orange"]
add_fruits(my_list)
print(my_list)

#learn while loop
count=0
while count<5:
    print(count)
    count+=1

#lets break loop early
count=0
while True:
    print("count",count)
    if count==100:
        break
    count+=1   

#learn try/except
try:
    number=int(input("enter a number"))
    print("you entered",number)
except ValueError:
    print("thats not a valid number")

#learn file 

with open("myfile.txt","w") as f:
    f.write("hello world")

with open("myfile.text",r) as f:
    text=f.read()
    print(text)

# learn import

import random
number=random.randint(1,100)
print("random number between 1 and 100",number)

#learn random and guessing game 

import random 
secret = random.randint(1,6)
guess = int(input("guess a number between 1 and 6"))

if guess==scercet:
    print("congratulations you guessed the number")
else:
    print("sorry, that's not the right number. The number was", secret)   


#import guessing game
import random

secret=random.randint(1,5)
tries=0

while tries<3:
    guess = int(input("guess the number between 1 and 5"))
    if guess ==secret:
        print(" you guess it")
    else:
        print("try again")
    tries+=1
print("the number was",secret)    

#learn functions
def greet (name):
    print("hello",name)

greet("prasuldev")    

#learn function take input 

def greet(name):
    print("hello",name)
greet("sir")    
greet("madam")

#learn return value from function
def ad (a,b):
    return a+b
result=ad(3,4)
print("result")

#make a function value returns back
def add(a,b):
    return a+b
result=add(3,4)
print("result",result)

#a dictionary store key value pair
person={
    "name":"prasuldev",
    "age":23,
    "city":"kerala"
}
print(person)
print(person["name"])
print(person["age"])
print(person["city"])

#OOP just means: make your own type
class person:
    def __init__(self,name):
        self.name = name
    def say_hi(self):
        print("hi,i am", self.name)
        
p1 = person("alex")
p1.say_hi()


