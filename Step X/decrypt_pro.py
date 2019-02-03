#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

# Input
a_string = raw_input("Please enter the string: ")

# Decoding
a_string2 = a_string[::-1]

# my_string = a_string2.decode("base64")

# My encoding
# None

# separates the decoded string into chunks
# n = 2
#
# my_string = ([a_string2[i:i+n] for i in range(0, len(a_string2), n)])

# Slipt string into chunks
chunks, chunk_size = len(a_string2), len(a_string2)// 6
my_string = ([ a_string2[i:i+chunk_size] for i in range(0, chunks, chunk_size) ])
print (my_string)
