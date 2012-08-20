#!/usr/bin/python
""" yacht control  

"""

import sys
import speak
import time

from menu import *

def visit(item) :
   action = item.getAttribute('action')
   if action == "" :
      text = item.getAttribute('title')
   else : 
      text = eval(action)
   speak.say(text)
   print text

name = sys.argv[1]
menu = Menu(name)
menu.run(visit)

