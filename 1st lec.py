print("hello world")
a = 7
b=5
print(a*b)
print(type (a))
print(8*9,8+5)
print(a)
print(9%3)


#####comments####
#in python we use # for single line comments
"""in python we use triple quotes for multi line comments
like this  

this is a multi line comment
"""
#arithmetic operators 
# + , - , * , / , % , // , **
#** is used for power
#relational operators
# > , < , >= , <= , == , !=
c=89
v=90

print(c==v)
print(c!=v)
num=3
num+=7

#num+=7 it means num=num+7

num=10

num **= 5
print("num is :",num)
'''logical operators'''
"""logical operators are like ( not it is used such
as not true = false, not false= true)

another logical operator is 'and' (used like if both the 
values are true then it will return true otherwise false)

anothe logical operator is 'or' (used like if any one of the 
value is true then it will return true othewise false
mean to get return false in 'or' operator,  both the values 
should be false)


"""
a=True
b=False
print("and operator is :", a and b)
print("or operator is :", a or b)
#type conversion
a=6
b=6.31
add = a+b
print("the addition wil be :",add)



"""here add will be work as folat like 6+6.31 because
it convert int into float"""

#a= "5"
#b=9
#x = a+b
#print(x)
#it will give error because we cant add string and int
#to solve this we use type casting


####type casting####
#a=5.36

a =float("5.36")
# this will convert string into float
b=75
b=int (b)
d=a+b
print(type (b))
print(type(a))
print("addition will be:",d)

print("d is =",d)
#through the type casting we can convert numbers into string 
m=str (88)
type (m)
print (type (m))
print(m)
 
                ######## input function ########


name =input ("enter your name :")


print("welcome :",name)

value= input("enter your value :   " )
print(type(value),value)
#if we write an integer value it will consider as string in input function
#to solve this we use type casting
val = int(input("enter your value :    "))

print(type(val),val)
#now it will consider as integer


