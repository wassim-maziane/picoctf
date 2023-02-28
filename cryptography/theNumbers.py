#!/bin/bash
#this python script will decipher the image, every number represents an alphabetic character and refers to it's order of the alphabet
L=[16,9,3,15,3,20,6,'{', 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, '}']
for x in L:
	if type(x) == int:
		print(chr(x + ord('A') - 1), end = '')
	else:
		print(x, end = '')
