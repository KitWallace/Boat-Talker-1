#!/usr/bin/python
import speak
import presenter

for key in presenter.read_key() :
   print key
   speak.say(key)
   
