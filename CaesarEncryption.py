def encrypt(message, patterning):
    newS=''
    for car in message:
        newS=newS+chr(ord(car)+ patterning)
    return newS

def decrypt(message, patterning):
   newS=''
   for car in message:
       newS=newS+chr(ord(car) - patterning)
   return newS
