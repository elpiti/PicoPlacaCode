# -*- coding: utf-8 -*-
#!/usr/bin/python

from datetime import datetime
print "  Enter a License Plate Number, Date and Time\n"

arr = []

lista_dia = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
lista_num =['12','34','56','78','90']
texto = ["  License plate number Ex. LLL#### : ","  Date Ex. DD-MM-YYYY              : ",
         "  Time 24/hour format Ex. HH:MM    : "]


class run(object):
   global in_plate, dia_semana, hora, horaf, placa
   
   def in_plate(placa):
          
      if(placa[:3].isalpha() == False):
           print "Enter a valid license plate number"
      elif(placa[3:].isdigit() == False):
           print "Enter a valid license plate number"
      elif (len (placa) != 7):
           print "Enter a valid license plate number"

   def dia_semana(d_semana):
           
       if (d_semana in lista_dia[0:5]):
                
          if(placa[6:] in lista_num[0]):
             bandera = 'Monday'
             if(d_semana != bandera ):
                horaf(arr[2])
             else:
                 hora(arr[2])
                      
          elif(placa[6:] in lista_num[1]):
             bandera = 'Tuesday'
             if(d_semana != bandera ):
                horaf(arr[2])
             else:
                 hora(arr[2])
             
          elif(placa[6:] in lista_num[2]):
             bandera = 'Wednesday'
             if(d_semana != bandera ):
                horaf(arr[2])
             else:
                 hora(arr[2])
                
          elif(placa[6:] in lista_num[3]):
             bandera = 'Thursday'
             if(d_semana != bandera ):
                horaf(arr[2])
             else:
                 hora(arr[2])
                
          elif(placa[6:] in lista_num[4]):
             bandera = 'Friday'
             if(d_semana != bandera ):
                horaf(arr[2])
             else:
                 hora(arr[2])
                 
       elif(d_semana in lista_dia[5]):
          print("It is weekend there is no Pico y Placa")
             
       elif(d_semana in lista_dia[6]):
          print("It is weekend there is no Pico y Placa")   
       else:
          print "Enter a valid day of the week"       

   def hora(h_hora):
      puntos = h_hora.replace(':','',1)
      puntos2 = int(puntos)
      
      if(puntos2 in range(700,931) or puntos2 in range(1600,1931)):  
           print("This car can not be on the road")
      else:
         print("This car can be on the road") 

   def horaf(h_hora):
      
      puntos = h_hora.replace(':','',1)
      puntos2 = int(puntos)
      print("This car can be on the road") 


   for i in range(0, 3):
       arr.append(raw_input(texto[i]))

   placa = arr[0]
   date_format = datetime.strptime(arr[1],"%d-%m-%Y")
   d_semana = date_format.strftime('%A')
   h_hora = arr[2]
   in_plate(placa)
   dia_semana(d_semana)

