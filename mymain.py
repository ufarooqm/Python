#!/usr/bin/env python3
import fib #importing fib file and fact file 
import sys
import fact
def main(arg):
	fib.function(arg)
	fact.function(arg)
if __name__ == '__main__':
	while len(sys.argv) >1:
		main (int(sys.argv[1]))
		sys.exit(0)