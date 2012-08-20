#!/usr/bin/python
import time
import speak

while True :
   message = "The Raspberry Pi time is " + speak.escape_XML(speak.ssml_break(500)) + time.strftime('%I %M %p') 
   speak.say(message)
   time.sleep(60)
