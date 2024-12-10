#!/usr/bin/env python3
# -*- coding: utf-8 -*-
for i in range(5):
    if i == 3:
        continue 
    print(i)

def kup_al(x):
     print(x**3)
     kup_al(2)

def mesaj():
    print("Merhaba!")    
    
mesaj() 

def islem(x):
    if (x<0):
        return "NO"
    else:
        x*5
 
islem(2)

A = 12    
if type(A) == str:
    A = A.strip("*")
    print(A)    
else:
    A  = "*" + str(A) + "*"
    print(A.strip())

def harf_say(x):
    len(x)
 
harf_say("Merhaba!")

def islem(x):
    if (x>10):
        return "YES"
    else:
        return x*5
 
islem(4)

def harf_say(x):
    return len(x)
 
harf_say("Merhaba!")

urun_fiyatlari = [19,29,39]
 
for i in urun_fiyatlari:
    if i >= 30:
        print(i/2)
    else:
        print(i*0)
        
liste = ["a","b","c"]
liste.reverse()
print(liste)      

sayilar = [10,20,30,40]
 
for i in sayilar:
    if i == 30:
        continue
    print(i)
    
def yazdir(metin):
    print(metin, "yazanlar")
yazdir("gelecegi")

def islem(x,y):
    A = [x,y]
    return A[0] + A[1]

islem(1,3)

A = []

for i in [1,2,3,4]:
    A.append(i)

A[0]

if [1,2,3,4][1] == 2:
    print("YES".lower())
else:
    print("NO")  