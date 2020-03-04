#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:38:08 2018

@author: joey


"""
option = input("enter 0 for binary, 1 for decimal, or 2 for hexadecimal:\t")

if option == '0':
    
    binary = input("enter binary number:\t")
    b2 = str(binary)
    l = len(b2)
    n = l - 1
    decimal = 0
    
    for i in range(0, l):
        if b2[i] == '1':
            decimal += (2**n)  
        n -= 1
    print("binary number =\t" + str(decimal)+"\n")
    
elif option == '1':
    decimal = input("Enter decimal number:\t")
    
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
    
else:
    
    hexadecimal = input("enter a hexadecimal number:\t")
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
        
    print("decimal number\t" + str(decimal))




