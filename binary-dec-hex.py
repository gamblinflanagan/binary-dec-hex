#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:38:08 2018

@author: joey


"""

def HexIn(hexadecimal):
    uphex = hexadecimal.upper()
    hexlist = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    decimal = 0
    
    for i in range(0, len(uphex)):   
        if i > 0:
            if uphex[i] in hexlist:
                decimal *= 16
                decimal += hexlist.index(uphex[i])
        else:
            decimal += hexlist.index(uphex[i])
        
    print("\ndecimal number =\t" + str(decimal))
    DecIn(decimal)
    
    
    
    
def DecIn(decimal):
    dec = int(decimal)
    n = 0
    power = 2**n
    
    while dec > power:
        n += 1
        power = 2**n
        if dec <= power:
            break
        
    if dec == 2**n:    
        dec -= 2**n
        m = n-1
    else:
        dec -= 2**(n-1)
        m = n-2
        
    binary = '1'
    n2 = m
    
    for i in range(0, n2+1):
        if 2**m > dec:
            binary += '0'
        else:
            binary += '1'
            dec -= 2**m
        m -= 1
    
    print("binary number =\t" + binary)
    


def DecHex(decimal):
    dec = int(decimal)
    hexx = ''
    hexLst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if dec < 16:
        hexx = hexLst[dec]
    else:
        while dec >= 1:
            div = dec/16
            idiv = int(dec/16)
            rem = int((div-idiv)*16)
            
            hexx += hexLst[rem]
            dec = div
        
        hexx = hexx[::-1]

    #print((479/16-int(479/16))*16)
    print("\nhex number =\t" + str(hexx))
     
    
    
def BinIn(binary):
    b2 = str(binary)
    l = len(b2)
    n = l - 1
    decimal = 0
    
    for i in range(0, l):
        if b2[i] == '1':
            decimal += (2**n)  
        n -= 1
    print("binary number =\t" + str(decimal)+"\n")
    DecHex(decimal)






option = ''

while option != '3':
    option = input("enter 0 for binary, 1 for decimal, 2 for hexadecimal, or 3 to quit:\t")
    
    if option == '0':
        user = input("enter binary number:\t")
        BinIn(user)
        
    elif option == '1':
        user = input("enter decimal number:\t")
        DecIn(user)
        DecHex(user)
        
    
    elif option == '2':   
        user = input("enter hexadecimal number:\t")
        HexIn(user)
