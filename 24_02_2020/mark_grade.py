# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:23:26 2020

@author: SHARI
"""

#Take input as student marks (0,100) and return if the student is distinction or first class
# or second class or third class or fail (Marks>70 distinction, 70>marks>60 first class, 60>marks>50 second class,
# 50>marks>40 third class, marks<40 fail.

n=int(input("enter number of subjects "))
mark_list=list()
print("enter marks")
total=0
for i in range(0,n):
    mark= int(input(("enter mark ",i+1)))
    mark_list.append(mark)
    total=total+mark

average= total/n
if average>=70:
    grade="distinction"
elif average<70 and average>=60:
    grade="first class"
elif average<60 and average>=50:
    grade="second class"
elif average<50 and average>=40:
    grade="third class"
else:
    grade="fail"

print("grade of student=",grade)