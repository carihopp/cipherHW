#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:49:21 2020

@author: carettahopp
"""

import decryption

if __name__ == '__main__':
    
    cipher = decryption.open_cipher()
    letter_values, IC = decryption.vigenere_check(cipher)
    print(letter_values, IC)
    result = decryption.cipher_ic()
    print(result)



