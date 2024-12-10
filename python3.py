#!/usr/bin/env python3
# -*- coding: utf-8 -*-
liste = ["a","b","c"]
liste.reverse()
print(liste)


sozluk = {"REG" : {"RMSE": 10,
"MSE": 11,
"SSE": 12},
 
"LOJ" : {"RMSE": 111,
"MSE": 2222,
"SSE": 333},
 
"CART" : {"RMSE": 99,
"MSE": 00,
"SSE": 66}}

sozluk["CART"]["SSE"]

set1 = set([5,7,9])
set2 = set([5,6,7])
set1.union(set2)

liste = [10,20,30,40]
liste.pop(1)
liste

liste = [1,1,2,3,4,5,1,2,1]
liste.count(1)

set1 = set([5,7,9])
set2 = set([5,6,7])
set1.symmetric_difference(set2)

liste = [50,10,30,40]
liste.sort()
liste

liste = ["a","b","c"]
liste.index("b")

set1 = set([5,7,9])
set2 = set([5,6,7])
set2.difference(set1)

set1 = set([5,7,9])
set2 = set([5,6,7])
set1.union(set2)

liste = ["a","b","c"]
liste.extend(liste)
liste