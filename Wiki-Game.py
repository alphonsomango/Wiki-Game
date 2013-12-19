#!/usr/bin/env python

import sys
import string
from bs4 import BeautifulSoup
import urllib

##
## ----------------------------------------------------------------
## prints help
##
def printHelp():

	sys.stderr.write("Wiki-Game.py [Start URL] [End URL]\n")
##
## ----------------------------------------------------------------


##
## ----------------------------------------------------------------
## prints lists formated with proper indentation
##
def printList():
	#prints succesfull path
##
## ----------------------------------------------------------------

##
## ----------------------------------------------------------------
## follows links until it gets the end goal or recurses too far
##
def playGame(start, end, depth):
	#finds path
##
## ----------------------------------------------------------------


##
## ----------------------------------------------------------------
## Beginning of mainline
##
def main(argv):
	i=1
	numArgument = 0
	depth = 0 #not used yet

	for arg in argv[1:]:
		if arg[0] == '-':
			if len(arg) > 1 and (arg[1] == 'h' or arg[1] == 'H'):#if we see -h print help
				printHelp()
				sys.exit(0)
				
		else: #if not then grab the link and put it in array
			link[i-1] = arg
			numArgument = numArgument+1
		
		i=i+1

	if numArgument == 0 or numArgument > 2: #if no links or more than two then print help
		printHelp()
		sys.exit(0)
		
	if(depth > 0 and depth < 5):
		playGame(link[0], link[1], depth) #do work
		
	else: #to avoid going too deep we dont allow more than x recursions 
		printHelp()
		sys.exit(0)
		
	printList() #ouput
	sys.exit(0) #exit
##
## ----------------------------------------------------------------


##
## ----------------------------------------------------------------
## This causes the main() function to be called if run from
## the command line; otherwise we can be loaded as an
## importable module
if __name__ == "__main__": main(sys.argv)
##
## ----------------------------------------------------------------








######################### ACTUAL CODE #################### NOT USED YET
html_doc = urllib.urlopen("http://en.wikipedia.org/wiki/2013_South_Sudanese_coup_d%27%C3%A9tat_attempt")


soup = BeautifulSoup(html_doc)

for link in soup.find_all('a'):
    print(link.get('href'))
