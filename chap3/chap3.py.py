# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 10:16:11 2022

@author: Surface
"""
#3.1
len("monty")
def right_justify(s):
    s=(" "*65,"monty")
    print(s)
right_justify("s")
    

#3.2.1
def do_twice(f):
    f()
    f()
def print_spam():
    print("spam")
do_twice(print_spam)
#3.2.2
def do_twice(f,x):
    f(x)
    f(x)
#3.2.3

#3.2.4
def print_twice(a):
    print(a)
    print(a)
print_twice("spam")
    
#3.2.5
def do_four(f,x):
    print_twice
    print_twice
       

print("+ - - - -  + - - - - +")
print("|          |         |")
print("|          |         |")
print("|          |         |")
print("|          |         |")
print("+ - - - -  + - - - - +")
print("|          |         |")
print("|          |         |")
print("|          |         |")
print("|          |         |")
print("+ - - - -  + - - - - +")

def print_line():
    print("- - - - - - - - - - - ")
def print_line1():
    print("|         |         |")
def do_twice():
    print_line1()
    print_line1()
print_line()
print_line1()
do_twice()
print_line()
print_line1()
do_twice()
print_line()








































