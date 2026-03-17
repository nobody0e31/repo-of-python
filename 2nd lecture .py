str = 'this is string'
print(str)
str = "this is string"
str = """it is string"""
#here is \t is escape sequence u can see in the next line.

str = "it is string.\t hello world"
print(str)
str = "it is string.\n hello world"
print(str) 
#here are now some basic operations 
'''now first operation is concatenation
'''
str1= 'addition'   
str2= 'divide'
finalstring = str1+str2
print(finalstring)
'''#now second operation is to see or print the length of string and for 
this we use a function that is "len(str)"       '''

a = "python 0999"
len1= len(a)
print (len1)
b = '7899'
string = 'here len function will also count space in length of string'
len12 = len(string)
print(len12)

#####now the concept of indexing in string#####
strindex = 'hello world'
ch=strindex[0]
print(ch)

#this is 2nd way to print or about indexing print(strindex[0]) #h
#now we are going to learn slicing concept in python string
stringslice = 'apna college'
a=stringslice[1:4]  #here 1 is starting index and 4 is ending index but ending index is not included
print(a)
#print (str[5:7]) it is second way to print slicing'
abcdf= 'hello i am going to learn slicing concept'
print(abcdf[4:len(abcdf)])# if we want 0:4 then we can use print(abcdf[:4]) than thisprint(abcdf[0:4])
 # mean of it is that to go till the last of string
  #we can also use space to go last in the string while using slicing concept
  #like this print(abcdf[4:])
     # now we are going to learn about negative indexing in python string
negindex = 'python programming'
print(negindex[-1]) #g
print(negindex[-5]) #a
print(negindex[-7:-2]) #rammi

 
 
#*********************string functions in python****************************




#endswith() function
strfunc = 'hello world'
print(strfunc.endswith('world')) #True
#capatilize() function
strfunc1 = 'hello world'
print(strfunc1.capitalize()) #Hello world


str000 =strfunc1.capitalize()
print(str000)
# replace() function
strreplace = 'hello world'
print(strreplace.replace('world','everyone')) #hello everyone


#find() function

strfind = 'hello world'
print(strfind.find('world')) #6#returns first index of 1st occurrer 
 
#count function
strcount = 'hello world hello universe'
print(strcount.count('hello')) #2

####### if elif and else if statements    #############

#age = print(input("enter your age"))
age=66
if ( age > 17 ):             ####indentation
   print("you can vote")
else:
   print("can not vote")
   
   ###nesting
   ageui = 66
   if(ageui>=18):
      if(ageui>80):
         print("cannot drive")
      else:
         print("can drive ")
   else:
         print("cannot drive")
         
   
   