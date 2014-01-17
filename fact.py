#!/usr/bin/env python3
import sys
import math	

def function(x):
	return math.factorial(x) #calculating factorial using this function
print ("Factorial of ", int(sys.argv[1]), "is " ,function(int(sys.argv[1]))) 
#The int(sys.argv[1]) variable gives the second user typed argument in integer form