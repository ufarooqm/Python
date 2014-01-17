#!/usr/bin/env python3
import math
import sys

phi = float((1 + math.sqrt(5)) / 2) #calculating the value of phi

def function(n):
	return (phi ** n - (-1) ** n / phi ** n) / math.sqrt(5) #function to calculate fibonacci sequence for nth term

print ('Fibonnaci of ', int(sys.argv[1]),'is ',int(function(int(sys.argv[1]))))