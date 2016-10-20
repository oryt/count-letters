#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#A script that will take the sequence and print out what letters it consis of 
#and how many times they are present in the sequence

n = input('Please enter sequence \n')
sequence = n
list2 = []
in_memoriam='RIP_Stardust-RIP_Lemmy'

print(in_memoriam)

# A loop that will count how many times a letter is present in the sequence, format the 
# number with a right alignment and then push that together with the letter to a list 

for l in sequence:
	a = l
	p = sequence.count(l)
	c = str (p)
	y ='{:>5}'.format(c)
	d = a + y
	list2.append(d)

# push the list to a set to eliminate duplicate entries. Due to using a set the order of the 
#list is lost.

z=set(list2)

# a loop that prints each entry of the set

for x in z:
	print(x)
print(in_memoriam)
