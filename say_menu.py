#!/usr/bin/python
import sys
import speak

from menu import *

def visit(item) :
   text = item.getAttribute('title')
   speak.say(text)
   print text

name = sys.argv[1]
menu = Menu(name)
menu.run(visit)
