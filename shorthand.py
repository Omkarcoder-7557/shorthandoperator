#program for the short hand operator
a=int(input("enter first number:"))
b=int(input("enter second number:"))
#logic
a+=b #a=a+b
print(a)
a=b-a # we can not crete short hand operator a-b!=b-a
a-=b #a=a-b
#print(a)