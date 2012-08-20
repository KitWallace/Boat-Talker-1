
def escape_XML(str) :
   str.replace('"',"\042")
   str.replace('&',"\046")
   str.replace('<',"\074")
   str.replace('>',"\076")
   return str  

def pause(msec):
   return '<break time="'+str(msec)+'"msec/>'

def digits(digits):
   return '<say-as interpret-as="tts:digits">'+str(digits)+"</say-as>"



