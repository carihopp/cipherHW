#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:46:38 2020

@author: carettahopp
"""

import matplotlib.pyplot as plt
import numpy as np
import string
import itertools
import string
import math
from collections import Counter

list_engL =[0.0834, 0.0154, 0.0273, 0.0414, 0.1260, 0.0203, 0.0192, 0.0611, 0.0671, 0.0023, 0.0087, 0.0424, 0.0253, 0.0680, 0.0770, 0.0166, 0.0009, 0.0568, 0.0611, 0.0937, 0.0285, 0.0106, 0.0234, 0.0020, 0.0204, 0.0006]  


def vigenere_check(cipher):
    letter_counting =[]
    letter_counting = doubles_rel_distribution_IC(cipher)
    #print(letter_counting)  
    result_helper = []
    result =0
    resultlist=[]
    list =[]
    a=0
    for x in range(0,len(list_engL)):
        list.append(list_engL[x])
    for x in range(0,len(list)):
            result_helper.append(list[x]*letter_counting[x][1])
            result += result_helper[x]
            resultlist.append([result, x])
    return resultlist, result

def open_cipher():
    text = ""
    list = []
    f = open('ciphertext.txt', 'r', encoding='utf-8')
    text = f.read()
    #print(text)
    for char in text:
        list.append(char)
    f.close()
    return list

def counting_duplicates_KL(cipher):
    shift_list=[]
    double_distrb_index = []
    double_distrb = []
    for x in range(0,len(cipher)-1):
        shift_list.append(cipher[x])
    shift_list.pop()
    cipher.pop()
    '''for x in range(0,len(cipher)-1):
        counter=0
        f = open('similiarletters.txt', 'a')
        last_letter = shift_list.pop()
        shift_list.insert(0,last_letter)
        print(shift_list, cipher)
        for i in range(0,len(shift_list)-1):
            if shift_list[i]==cipher[i]:
                counter += 1 
        print(x, counter)
        f.write(str(counter) + ' \n')
    #print(f.read) 
    f.close''' 
    t = open('similiarletters.txt', 'r')
    i = 0
    for line in t:
        a= int(line.rstrip())
        double_distrb_index.append([i, a])
        double_distrb.append(a)
        i +=1
    t.close()              
    return double_distrb_index, double_distrb

def distribution(final, cipher):
    #print(final)
    '''distribution = final
    plt.hist(distribution)
    plt.title("Histogram")
    plt.xlabel("Wert")
    plt.ylabel("Häufigkeit")
    plt.show()
    y = [str(x) for x in range(0, 200)]
    visitors = final
    index = np.arange(len(final))
    index1 = np.arange(300)
    bar_width = 0.1
    plt.bar(index, visitors, bar_width,  color="green")
    plt.xticks(y,index) # labels get centered
    plt.yticks(index1) # labels get centered
    plt.show()'''
    
def doubles_rel_distribution_IC(cipher):
    a = 0
    i = 0
    j =0
    list_alph=[]
    result = []
    list2=[string.ascii_uppercase]
    for x in range(0,26):
        list_alph.append([list2[0][x], 0])
    #print(list_alph)
    for i in range(0, len(cipher)):
        for j in range(0, len(list_alph)):
            if cipher[i]==list_alph[j][0]:
                a = 1
                a +=list_alph[j][1]
                list_alph[j][1]=a
    #print(list_alph)
    length = len(cipher)
    for i in range(0,len(list_alph)):
        result.append(list_alph[i])
        result[i][1]=result[i][1]/length
    #print(result)
    return result
    
def mapping_eng_distrb(cipher_rel):   
    list_engL =[0.0834, 0.0154, 0.0273, 0.0414, 0.1260, 0.0203, 0.0192, 0.0611, 0.0671, 0.0023, 0.0087, 0.0424, 0.0253, 0.0680, 0.0770, 0.0166, 0.0009, 0.0568, 0.0611, 0.0937, 0.0285, 0.0106, 0.0234, 0.0020, 0.0204, 0.0006]  
    #print(list_engL)   
    result_helper = []
    result =0
    resultlist=[]
    list6 =[]
    a=0
    for x in range(0,len(list_engL)):
        list6.append(list_engL[x])
    for x in range(0,len(list6)):
            result_helper.append(list6[x]*cipher_rel[x][1])
            result += result_helper[x]
            a=list6.pop()
            list6.insert(0,a)
            #print(list6)
            resultlist.append([result, x])
    print(result_helper)
    return resultlist
    
    
def ic_calculation(simis, cipher, start, distc):
    list_simis=[]
    list_cipher=[]
    list_rel =[]
    #print(simis)
    for letter in range(start,len(simis),distc):
        list_simis.append(simis[letter])
    #print(list_simis)
    for letter in range(start, len(cipher),distc):
        list_cipher.append(cipher[letter])
    print(list_cipher)
    list_rel = doubles_rel_distribution_IC(list_cipher)
    result = mapping_eng_distrb(list_rel)
    return result

def shift(text, shift_by):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    shifted = ""
    for x in text:
        index = alphabet.index(x)
        shift_index = index + shift_by
        if shift_index < 0:
            shift_index += len(alphabet)
        elif shift_index >= len(alphabet):
            shift_index -= len(alphabet)
        shifted += alphabet[shift_index]
    return shifted

       
def decrypt(text, key, from_index):
    decrypted = ""
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    #print(alphabet)
    shifted = [shift(alphabet, -k-from_index) for k in key]
    key_to_use = 0
    for i in range(len(text)):
        orig_index = alphabet.index(text[i])
        decrypted += shifted[key_to_use][orig_index]
        key_to_use = (key_to_use+1)%(len(key))

    return decrypted

    
    
    
def cipher_ic():  
    cipherlist = open_cipher()
    #print(cipherlist)
    
    # Searching the Key Length via Mapping the different Alphabets and 
    # counting the amount of similiarities to the cipher
    index_doubles_distribution, doubles_distribution = counting_duplicates_KL(cipherlist) 
    print(index_doubles_distribution)
    
    # Analysing the Distribution of the similiarities via histogram
    # Result: Key length is 4 digits
    frequency = distribution(doubles_distribution, cipherlist)
    print(frequency)
    
    # Separation of the cipher into the key digit parts and calculating the IC
    
    key0_ic = ic_calculation(doubles_distribution, cipherlist, 0, 4)
    key1_ic = ic_calculation(doubles_distribution, cipherlist, 1, 4)
    key2_ic = ic_calculation(doubles_distribution, cipherlist, 2, 4)
    key3_ic = ic_calculation(doubles_distribution, cipherlist, 3, 4)
    print('Resultlist')
    print(key0_ic, key1_ic, key2_ic, key3_ic)

        # Decision for the best IC for 0 shift: 19, 20, 21
    
        # Decision for the best IC for 1 shift: 14, 19, 20
    
        # Decision for the best IC for 2 shifts: 18, 19, 20
    
        # Decision for the best IC for 3 shifts: 19, 20, 21
    
    # Possible Decryptions: Starting with the three first possibilities
    plaintext0 = decrypt(cipherlist, [19,14,18,19], 0)
    print( 'This is the plaintext for the key = [19,14,18,19] ' + plaintext0)
    
    plaintext1 = decrypt(cipherlist, [20,19,19,20], 0)
    print( 'This is the plaintext for the key = [20,19,19,20] ' + plaintext1)

    plaintext2 = decrypt(cipherlist, [21,20,20,21], 0)
    print( 'This is the plaintext for the key = [21,20,20,21] ' + plaintext2)

    # The first Shift 0 text could become a plaintext but one of the key digits
    # is still wrong: Since we can see Situation (sitiation), the i is wrong
    # and that is the first digit of the key. Let's try 19 mod (26) = 7

    plaintext3 = decrypt(cipherlist, [7,14,18,19],0)
    print('This is the plaintext for the key = [7,14,18,19] ' + plaintext3)
    
    
    
    
    
    
    
    
    


