# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


print("Auro Saswat Raj")
a = 5
b = 10
c = a + b
print(a, "=", b, "=", c)
fruits = ["Apple", "Mango", "Banana", "Bhelpuri"]
for x in fruits:
    print(x)
    if x == "Banana":
        print("Banana is executed..! with iteration=", fruits.index("Banana"))
    else:
        print("Just skipped with iteration")

for i in range(2000, 2500 + 1):
    if i % 17 == 0 and i % 5 != 0:
        print(i)

i = int(input("Enter a number:\n"))
m = int(i / 2)
count = 0
for x in range(2, m+1):
    if i % x == 0:
        count = count + 1
        break

if count == 1:
    print(i, "is not a prime number")
else:
    print(i, "is a prime number")

print("The numbers that are divisible by 17 but not by 5 are:")
for i in range(2000,2500+1):
    if i%17==0 and i%5!=0:
        print(i)
print("Before Swapping")
a=5
b=10
print("value of a:",a,"\nValue of b:",b)
temp=a
a=b
b=temp
print("After Swapping")
print("value of a:",a,"\nValue of b:",b)
print("\nUsing Question's Code Format Swapping procedure:")
print("Before Swapping")
a=5
b=10
print("value of a:",a,"\nValue of b:",b)
a,b=b,a
print("After Swapping")
print("value of a:",a,"\nValue of b:",b)

def fun():
    print("Here the program begins..!")


fun()


def large(*num):
    maxium = num[0]
    for i in num:
        if i > maxium:
            maxium = i
    print(maxium)


large(45, 23, 45, 78, 98, 112, 123, 156, 156)

# Approach-2 is :-
mylist = [0]


def addnumber(num):
    mylist.append(num)

def large1(mylist1):
    mylist1=mylist
    maximum=mylist1[0]
    for i in mylist1:
        if i > maximum:
            maximum=i

    print("Largest Number is ",maximum)


while True:
    num=int(input('Enter a number...Press 0 to compute'))
    if num != 0:
        addnumber(num)
    else:
        large1(mylist)
        break
