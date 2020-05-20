# -*- coding: utf-8 -*-\
"""
Created on Sun May 17 09:04:58 2020

@author: SHARI
"""
#Define a class, which have a class parameter and have a same instance parameter.
class Sample:
    count=0 #CLASS PARAMETER
    
    def count_increase(self):
        Sample.count += 1

print(Sample.count)
s1=Sample()
s1.count_increase()
print(s1.count) # INSTANCE PARAMETER
s2=Sample()
s2.count_increase()
print(s2.count) # INSTANCE PARAMETER
