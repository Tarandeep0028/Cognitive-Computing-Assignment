# -*- coding: utf-8 -*-
"""Cognitive Computing-2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Zu1ksTjYZUjdbDFmPblzKcfMRcQo1lt9

1. Create a List L that is defined as= [10, 20, 30, 40, 50, 60, 70, 80].
  
  i.WAP to add 200 and 300 to L.
"""

List = [10,20,30,40,50,60,70,80]
print(List)
List.append(200)
List.append(300)
print(List)

"""ii. WAP to remove 10 and 30 from L."""

List = [10,20,30,40,50,60,70,80]
print(List)
List.remove(10)
List.remove(30)
print(List)

"""iii. WAP to sort L in ascending order."""

List = [10,20,40,30,50,70,60,80]
print(List)
List.sort()
print(List)

"""iv. WAP to sort L in descending order."""

List = [10,20,40,30,50,70,60,80]
print(List)
List.sort(reverse=True)
print(List)

#2.	Create a tuple of marks scored as scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45) and perform the following operations using tuple functions:

Tuple = (45, 89.5, 76, 45.4, 89, 92, 58, 45)

#i.	Identify the highest score and its index in the tuple.
max = Tuple[0]
maxIndex = 0

for i in range(len(Tuple)):
  if max < Tuple[i]:
    max = Tuple[i]
    maxIndex = i

print(f'max element {max} is present at index {maxIndex} ')

#ii.	Find the lowest score and count how many times it appears.

min = Tuple[0]
minIndex = 0

for i in range(len(Tuple)):
  if min > Tuple[i]:
    min = Tuple[0]

print(f'Minimum is = {min}')
print(Tuple.count(min));

#iii. 	Reverse the tuple and return it as a list.
ans =  Tuple[::-1]
ans_list = list(ans)
print(ans_list)

#iv. 	Check if a specific score ‘76’ (input by the user) is present in the tuple and print its first occurrence index, or a message saying it’s not present.

x = int(input("Please enter element to find: "))

found = ans.count(x)

if found==0:
  print("Element not present in list")
else:
  print(f'Element is = {x}')

#3.	WAP to create a list of 100 random numbers between 100 and 900. Count and print the:

from random import *
from math import *

randomizer = []
#i.	All odd numbers
for i in range(100):
  randomizer.append(randint(100,900))

countOdd=0
for i in range(100):
  if randomizer[i]%2!=0:
    print(randomizer[i])
    countOdd+=1

print(f'Odd numbers = {countOdd}')

#ii.	All even numbers
countEven=0
for i in range(100):
  if randomizer[i]%2==0:
    print(randomizer[i])
    countEven+=1

print(f'Even numbers = {countEven}')

#iii.	All prime numbers
countPrime=0
for i in range(100):
  prime = True
  for j in range(2,int(sqrt(randomizer[i]))+1):
    if randomizer[i]%j==0:
      prime = False
      break
  if prime==False:
    continue
  else:
     countPrime+=1
     print(randomizer[i])

print(f'Prime numbers = {countPrime}')

"""Consider the following sets representing scores of two teams:
A = {34, 56, 78, 90} and B = {78, 45, 90, 23} . Perform the following operations:
"""

A = {34,56,78,90}
B = {78,45,90,23}

#i.	Find the unique scores achieved by both teams (union).

unionAB = A | B
print(unionAB)

#ii.	Identify the scores that are common to both teams (intersection).

intersectionAB = A & B
print(intersectionAB)

#iii.	Find the scores that are exclusive to each team (symmetric difference).

symdiffAB = A ^ B
print(symdiffAB)

#iv.Check if the scores of team A are a subset of team B, and if team B's scores are a superset of team A.

checkFirst =  A.issubset(B)
checkSecond = B.issuperset(A)

print(f'A is a subset of B?? --> {checkFirst}')
print(f'B is a superset of A?? --> {checkSecond}')

#v.	Remove a specific score X (input by the user) from set A if it exists. If not, print a message saying it is not present.

x = int(input("Enter element to remove: "))

if x in A:
    A.remove(x)
    print(f"Element {x} has been removed ")
else:
    print(f"Element {x} is not present")

"""Write a program to rename a key city to location in the following dictionary:

data = {"city": "New York", "population": 8419600, "area": 468.9} .
"""

data = {
    "city" : "New York",
    "population" : 8419600,
    "area" : 468.9
}

data["location"] = data["city"]
data.pop("city")

print(data);