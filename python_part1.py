#Part-A Sring Functions
#Ans1.
text='PYTHON'
print(text.lower())
#Ans2.
name=' Hello World '
print(name.strip())
#Ans3.
fruit="banana"
print(fruit.count("a"))
#Ans4.
sentence='i have a dog'
print(sentence.replace("dog","cat"))
#Ans5.
msg='pyhton is fun'
print(msg.split())
#Ans6.
text="machine"
print(text.find("i"))
#Ans7.
greeting="Good Morning"
print(greeting.startswith("Good"))
#Ans8.
word="hello"
print(word.upper())
#Ans9.
number="12345"
print(number.isdigit())
#Ans10.
items=['data','science']
print(" ".join(items))

#Part-B List Function(12 Question)
#Ans11. 
l=[1,2,3]
l.append(10)
print(l)
#Ans12.
p=[5,6,7]
p.insert(1,99)
print(p)
#Ans13.
k=[9,1,3,8]
k.sort()
print(k)
#Ans14.
t=[10,20,30,40]
t.remove(20)
print(t)
#Ans15.
g=[1,2,3,4]
g.pop(3)
print(g)
#Ans16.
a=[1,2]
b=[3,4]
p=a.__add__(b)
print(p)
#Ans17.
nums=[2,4,2,2,6]
print(nums.count(2))
#Ans18.
s=[5,10,15]
print(sum(s))
#Ans19.
marks=[44,72,91,60]
print(max(marks))
#Ans20.
nums=[20,18,5,34]
print(min(nums))
#Ans21.
w=[8,9,10]
w.clear()
print(w)
#Ans22
j=[]
ok=[1,2,3]
j=ok.copy()
print(j)

#Part-C Control Statements(8 Questions)
#Ans23
num1=int(input('Enter a number to check odd and even='))
p=num1%2
if p==0:
    print("Your Number is Even")
else:
    print("Your Number is Odd")

#Ans24.
num2=int(input("Enter Number to check Positive,Negative or Zero="))
if num2>0:
    print("Your Number is Positive")
elif num2<0:
    print("Your Number is Negative")
else:
    print("Your Number is Zero")
#Ans25
i=0
for i in range(0,11):
    print(i)
#Ans26
i=0
for i in range(1,11):
    print(f"{5}X{i}={5*i}")

#Ans27
i=10
while i>0:
    print(i)
    i-=1
#Ans28
num=int(input("Enter Number to add its digit="))
sum1=0
while num>0:
    digit=num%10
    sum1+=digit
    num=num//10
print(sum1)

#Ans29
word=input("Enter a string to find Vowel in it=")
vowel_count=0
for i in word:
    if i.lower() in 'aeiou':
        vowel_count+=1
print(vowel_count)
#Ans30
string="madam"
p=string[::-1]
if p==string:
    print("Yes its a polindrome")
else:
    print("No its not a polindrome")