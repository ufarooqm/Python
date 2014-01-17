#!/usr/bin/env python3

import hello

def main(arg):
	hello.say_hello(arg)
if __name__ == '__main__':
	import sys
	if len(sys.argv) >1:
		main(sys.argv[1])
	else:
		main('world')
	sys.exit(0)


