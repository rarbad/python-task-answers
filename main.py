# extract username from email
# email=input("enter your email")
task:23
vegetables=("bringle","tomato","potato","chili")
(one,two,three,four)=vegetables
print(one)
print(two)
print(three)
print(four)

task:24
name=("pooja","punam","kirti","siddhi","pooja","gaytri","pooja")
x=name.count("pooja")
print(x)

task:25
vegetables=("bringle","tomato","potato","chili")
num=(2,34,56,8,96,)
c=vegetables+num
print(c)

task:26
colours=("red","yellow","pink","green","violet")
if "pink" in colours:
    print("yes,'pink' are present")
    
task:27
colours=("red","black","yellow","pink","green","violet")
print(colours [2:6])

task:28
colours=("red","black","yellow","pink","green","violet")
(One,two,*three)=colours
print(One)
print(two)
print(three)


task:29
My_tuple=(10,20,30,40,50)
element=30
print(My_tuple.index(element))

task:30
colours=("red","black","yellow","pink","green","violet")
New_tuple=colours*3
print(New_tuple)



task:31
students1 = dict(Name= "revati", Age= 22, Country="India")
print(students1)

task:32
stud1={
    "Name":"revati",
    "Age":21,
    "ciyt":"parbhani",
    "Grade":"A+"
}
print(stud1["Age"])
print(stud1.get("Name"))

task:33
stud1={
    "Name":"revati",
    "Age":21,
    "ciyt":"parbhani",
    "Grade":"A+"
}
print(stud1.keys())

task:34
stud1={
    "Name":"revati",
    "Age":21,
    "ciyt":"parbhani",
    "Grade":"A+"
}
print(stud1.values())

task:35
stud1={
    "Name":"revati",
    "Age":21,
    "ciyt":"parbhani",
    "Grade":"A+"
}
print(stud1.items())

task:36
stud1={
    "Name":"revati",
    "Age":21,
    "ciyt":"parbhani",
    "Grade":"A+"
}
if "name" in stud1:
    print("yes,'name' key exist. in dict")
else:
    print("yes 'name' key does not exist. in dict")
    
task:37    
stud1={
    "Name":"revati",
    "Age":21,
    "city":"parbhani",
    "Grade":"A+"
} 
print(stud1["city"])
stud1.update({"city":"pune"})
print(stud1["city"])


task:38
tud1={
    "name":"revati",
    "Age":22,
    "city":"parbhani",
    "Grade":"A+"
}
stud1["adhar no"]=917644697300
print(stud1)

task:39
students1={
    "name":"revati",
    "Age":22,
    "City":"parbhani",
    "Grade":"A+"
}
stud1.pop("city")
print(stud1)

task:41
stud1={
    "Name":"revati",
    "Age":22,
    "City":"parbhani",
    "Grade":"A+"
}
stud1. clear()
print(stud1)

task:43
number=int(input("enter a number:"))
if number>0:
    print("positive number")
else:
    print("negative or zero")

task:44
marks=int(input("enter a mark of students:"))
if marks>=90:
    print("you have got A grade")
elif marks >=80:
    print(" you have got B grade")
elif marks>=70:
    print("you have got C grade")
else:
    print("you have windows programming fail")
    
task:45
num=int(input("ente a number"))
if num>=1:
    print("positive number")
elif num>=1:
    num= int(input("number is even or number is odd"))
if num==0:
    print("positive number is even")
else:
    print("negative number is odd")

task:47
 i=1
    while i<10:
        print(i)
        i+=

task:49
cities=("pune","mumbai","delhi","kolkata","parbhani")
for x in cities:
     print(x)
    
task:50 
for x in range (2,21,2):
    print(x)

task:51    
def myfun(a,b):
    return a+b
    Result=myfun(4,8)
    print("sum:",Result)

task:52
square=lambda x:x**2
print(square)

task:53
def myfun(fun,num):
    return fun(num)
    square=lambda x:x**2
    cube=lambda x:x**3
    print(myfun(square,4))
    print(myfun(cube,3))
    
task:54
number=(45,23,98,65,43,96,12)
sum_element=sum(number)
max_element=max(number)
min_element=min(number)
print("sum of element:", sum_element)
print("maximum of element:",max_element)
print("minimum of element:",min_element)

task:55
import json
x={"name":"revati","age":22,"city":"parbhani"}
y=json.dumps(x)
print(y)

task:56
import json
x={"name":"omkar","age":21,"city":"parbhani"}
print(y) 

    
    
    
    
    




    
    
    
    
    
    




























































# username=input("enter your username")
# print(email)
# print(username)

#  replace every 'a'in a string with @
# a= "revatiarbad"
# print(a.replace("a","@"))



# reverse a string without using reverse()
# input_string= input ("enter your name")
# surname=input_string[::-1]
# print("reversed string:",surname)

# count the number of vowels in a the string
# name=input("enter your name")
# vowel_count= sum(name.count(vowel)for vowel in "aeiou")
# print("number of vowel in the name:",{vowel_count})

 

# upper case & lower case string
# name=input("enter a string")
# print(name.upper())
# print(name.lower())
  
  
# bill_amount=float(input ("enter a bill_ amount"))
# message=f"my bil_amount is {bill_amount}"
# print(message)

# a="revati,arbad ! "
# a_new=a.strip()
# print(a)

a="revati gaytri, revati, arbad"
x=a.count("revati")
print(x)

# extract a substring from a gifind the maximun and minimum number in a list
# num=[2,8,8,34,65,67,87,96,345,987,65]
# num.sort()
# print(num)

# remove duplicate from list
# a=["apple","banana","kiwi","mango","apple","cherry"]
# a=set(("apple","banana","kiwi","mango","apple","cherry"))
# a=list(a)
# print(a)

# merge to list and sort the result
# fruits=["apple","banana","kiwi","mango","apple","cherry"]
# name=["revati","punam","pooja","pratikshs","gaytri"]
# add=fruits+name
# print(add)
# add.sort()
# print(add)

# swap the first and last elements of a list
# a=[4,3,2,8,6,1,5]
# a[0]="5"
# print(a)
# a[6]="4"
# print(a)
task:16
letters=["a","b","c","d","e","f"]
print(letters[2:4])
print(letters[:3])

task:18
name=["revati","punam","pooja","gaytri","aditi","dipali"]
name.insert(2,"siddhi")
print(name)

task:19
name=["revati","punam","pooja","gaytri","aditi","dipali"]
add=("list_to_string:",name)
print(add)

task:20
num=[3,6,8,9,5,6,7]
name=["revati","punam","pooja","gaytri","aditi","dipali"]
num.append("4")
print (num)
name.remove("pooja")
print(name)
name.clear()
print(name)

task;21
tuple1 =(1,2,3,4,5)
tuple2 =(3,4,5,6,7)
common_elements=tuple(set(tuple 1) & set(tuple 2)
print("common_elements:",common_ellements)

task:22
name=["revati","punam","pooja","gaytri","aditi","dipali"]
x=list(name)
x[2] ="siddhi"
name=tuple(x)
print(name)























 
