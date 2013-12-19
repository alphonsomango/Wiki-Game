#!/usr/bin/env python

import sys
import string
from bs4 import BeautifulSoup
import urllib
from collections import deque


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
def printList(path):
	#print "GOT TO PRINT LIST"
	print path #prints first succesfull(unless depth reached) path
	sys.exit(0) #exit



##
## ----------------------------------------------------------------

##
## ----------------------------------------------------------------
## follows links until it gets the end goal or recurses too far
##
def playGame(start, end, depth): #finds path, breadth first 
	#print "GOT TO PLAY GAME"
	q = deque([start])
	path = ([start])
	playGameRecurse(q,end,depth-1,path)
	
##
## ----------------------------------------------------------------

##
## ----------------------------------------------------------------
## follows links until it gets the end goal or recurses too far
##
def playGameRecurse(q, end, depth, path): #finds path, breadth first 

	#print "GOT TO PLAY GAME RECURSE"
	temp = q.popleft()

	if (temp == end):
		printList(path) #we found it
		#print "GOT TO TEMP == END"
	if (depth >0):
		#print "GOT TO ELIF (DEPTH >0)"
		html_doc = urllib.urlopen(temp)
		soup = BeautifulSoup(html_doc)
		for link in soup.find_all('a'):
			q.append(link.get('href'))
		#print "GOT PAST ELIF (DEPTH >0)"	
		
	if (depth ==0 or len(q) == 0):
		printList("not found") #not found
		#print "GOT TO DEPTH == 0 OR Q.EMPTY"
	else:
		#print "GOT TO ELSE"
		playGameRecurse(q, end, depth-1,path.append(temp))

	
	
##
## ----------------------------------------------------------------



##
## ----------------------------------------------------------------
## Beginning of mainline
##
def main(argv):
	i=1
	numArgument = 0
	depth = 2 #inflexible for now
	link = [] 

	for arg in argv[1:]:
		if arg[0] == '-':
			if len(arg) > 1 and (arg[1] == 'h' or arg[1] == 'H'):#if we see -h print help
				printHelp()
				sys.exit(0)
				
		else: #if not then grab the link and put it in array
			link.append(arg)
			numArgument = numArgument+1
		
		i=i+1

	if numArgument != 2: #if no links or more than two then print help
		printHelp()
		sys.exit(0)
		
	if(depth > 0 and depth < 5):
		playGame(link[0], link[1], depth) #do work
		#print "GOT PAST DEPTH CHECK AND PLAYGAME"
		
	else: #to avoid going too deep we dont allow more than x recursions 
		printHelp()
		sys.exit(0)


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
