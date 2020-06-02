# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:12:03 2020

@author: SHARI
"""

#Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

string="hello world! hello world! hello world! hello world!"
string_list=string.split(" ") # split given string with space and find unique words from string ie,hello , world! here
unique_word=[]
for i in string_list:
    if i not in unique_word:
        unique_word.append(i)      
 
#compress string by making a string with unique words ie, hello world! 
data_compress=""
for i in unique_word:
    data_compress=data_compress+i+" "
    
data_compress=data_compress.strip(" ")  #remove blank space from both end  
print("compressed data:",data_compress) 

#decompress given compressed string by counting its occurrences in the original string and replicating for calculated count
# times  ie, hello world! for 4 times
count=string.count(data_compress)   
print("\ndecompressed data:")
data_decompress=data_compress*count
print(data_decompress)
    
    
