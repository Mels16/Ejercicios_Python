from Funciones23 import *
from Diccionario import *
import time
personas = {'Mary': [
 
    {'libro': 'la más callada de la clase',
     'fecha': '08-02-2023'}   
    
]}


while True:
   try:
      programa(personas)
   except:
       print("ocurrio un error intenta de nuevo")
       time.sleep(1.2)