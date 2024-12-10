#!/usr/bin/env python3
# -*- coding: utf-8 -*-
A = ["ali","veli","isik"]
B = [1,2,3]
AB = [A,B]


for i in AB:
    if type(i[0]) == int:
        print(list(map(lambda x: x-3, i)))

a = [1,2,3]
list(map(lambda x: x*2, a))

liste = [1,2,3,4]
A = []

for i in liste:
    A.append(i**2)

print(A)
list(map(lambda x: x**2, liste))

fun = lambda x: x**2
fun(3)

list(map(lambda x: x.upper(), ["Ali","Veli","isik"]))

from functools import reduce
reduce(lambda a,b: a/b, [8,4,2])

A = ["ali","veli","isik"]
B = [1,2,3]
AB = [A, B]

for i in AB:
    if type(i[0]) == str:
        print(list(map(lambda x: x + " hi", i)))  

list(map(lambda x: x/10, filter(lambda x: x > 20, [10,20,30,40,50])))

def yap(x,y,z):
    try:
        print(x/y*z)
    except ZeroDivisionError:
        print("gecersiz islem")

yap(1,2,0)


from functools import reduce
a = [1,2,3,4]
reduce(lambda a,b: a*b, a)

list(map(lambda x: x*1, [2,7,4]))


A = [[1,2],[3,4],[5,6]]
list(map(lambda x: x[0]*3, A))

from functools import reduce
A = ["Veri","Bilimi","Okulu"]
reduce(lambda a,b: a+b, list(map(lambda x: x[0], A)))

list(filter(lambda x: x < 2, [1,2,3,4,5]))
