"""
Proyectos para "juniors":
1. Tiempo vivido.
2. Generador de contraseñas.
3. Encriptar mensaje.
4. Desencriptar mensaje.
5. Conversor de monedas
6. Validador tarjeta de credito + colores
7. Calculadora.
"""

# Project 1
def calc_imc():
   import datetime
   print("Escribe la fecha de tu nacimiento: ")
   dia_naci = int(input("Escribe el numero del dia: "))
   mes_naci = int(input("Escribe el numero del mes: "))
   anio_naci = int(input("Escribe el numero del año: "))


   fecha_nacimieto = datetime.datetime(anio_naci,mes_naci,dia_naci)
   fecha_actual = datetime.datetime.now()
   diferencia = fecha_actual - fecha_nacimieto
   dias_vibidos = diferencia.days
   segundos_vividos = diferencia.seconds


   horas_vividas, segundos_vividos = divmod(segundos_vividos, 3600)
   minutos_vividos, segundos_vividos = divmod(segundos_vividos, 60)
   print(f"Has vivido:\n- Segundos: {segundos_vividos}.\n- Minutos: {minutos_vividos}.\n- Horas: {horas_vividas}.\n")

# Project 2
def generador_contras():
   import secrets
   import string

   letras = string.ascii_letters
   num = string.digits
   special_c = string.punctuation
   alfabeto = letras + num + special_c

   contra_longi = int(input("Escribe cuanto de larga quieres tu contraseña en numeros: "))

   contra = ''
   for i in range(contra_longi):
       contra += ''.join(secrets.choice(alfabeto))

   print("Contra 1:",contra)

   while True:
       for i in range(contra_longi):
           contra += ''.join(secrets.choice(alfabeto))
       if (any(char in special_c for char in contra) and
           sum(char in num for char in contra) >=2):
           break
    
       print("Contra 2:",contra)

# Project 3
def encriptar_mensaje():
   alfabeto = "abcdefghijlmnñopqrstuvwxyz"
   clave = 3
   nuevo_mensaje = ""
   mensaje = input("Introduce un mensaje para encriptar: \n- ")
   for caracter in mensaje:
      if caracter in alfabeto:
          position = alfabeto.find(caracter)
          nueva_positioin = (position + clave) % 27
          nuevo_caracter = alfabeto[nueva_positioin]
          nuevo_mensaje += nuevo_caracter
      else:
          nuevo_mensaje += caracter
   print("Mensaje encriptado: \n- "+ nuevo_mensaje)

# Project 4
def desencriptar_mensaje():
  alfabeto = "abcdefghijlmnñopqrstuvwxyz"
  clave = 3
  nuevo_mensaje = ""
  mensaje = input("Introduce el mensaje para desencriptar: \n- ")
  for caracter in mensaje:
      if caracter in alfabeto:
          position = alfabeto.find(caracter)
          nueva_positioin = ((position + clave)-6) % 27
          nuevo_caracter = alfabeto[nueva_positioin]
          nuevo_mensaje += nuevo_caracter
      else:
          nuevo_mensaje += caracter
  print("Mensaje desencriptado: \n- " + nuevo_mensaje)

# Project 5
def conversor_moneda():
   opcion = int(input("Escribe el numero que corresponde a lo que deeces convertir:\n1. Euro a dolar  2. Dolar a euro\n- "))

   if opcion == 1:
       num_euro = float(input("Escribe la cantidad que quieras convertir a dolar: "))
       num_dolar = num_euro * 1.11
       print(f"{num_euro} = {num_dolar}")
   if opcion == 2:
       num_euro = float(input("Escribe la cantidad que quieras convertir a euro: "))
       num_dolar = num_euro / 1.11
       print(f"{num_euro} = {num_dolar}")

# Project 6
def validador_tar_credito():
import datetime
from colorama import Fore
########COLORES###########
color_verde = Fore.GREEN
color_rojo = Fore.RED
color_negro = Fore.BLACK
color_azul = Fore.BLUE
##########################
while True:
   num_val = input(color_azul + "Escribe el numero de tu tarjeta de credito: ")
   print(color_azul + "Escribe la fecha de caducidad:")
   dia = int(input(color_negro + "Escribe el dia: "))
   mes = int(input("Escribe el mes: "))
   anio = int(input("Escribe el año: "))
   ######################################
   num_val_list = list(num_val)
   n_v_list_long = len(num_val_list)
   fecha_caducidad = datetime.datetime(anio, mes, dia)
   fecha_actual = datetime.datetime.now()


   if n_v_list_long > 16:
       print(color_rojo + "Error, el numero es incorrecto, intente de nuevo")
       continue
   elif n_v_list_long < 16:
       print(color_rojo + "Error, el numero es incorrecto, intente de nuevo")
       continue
   else:
       print(color_verde + "- El Numero de tu targeta es valido.")


   if fecha_actual == fecha_caducidad:
       si_no = input(color_rojo + "Tu tarjeta a caducado.\n" + color_negro + "¿Quieres intentar con otra?(S/N): ").lower()
       if si_no == "s":
           continue
       else:
           break
   elif fecha_actual >= fecha_caducidad:
       si_no = input(color_rojo + "- Tu tarjeta a caducado.\n" + color_negro + "¿Quieres intentar con otra?(S/N): ").lower()
       if si_no == "s":
           continue
       else:
           break
   else: print(color_verde + "- Tu targeta no está caducada.")
   print("!Tu targeta es Valida!")
   break



# Project 7
def calculadora():
   while True:
       num1 = int(input("Escribe el primer numero: "))
       simbolo = input("Escribe +, -, * o /: ")
       num2 = int(input("Escribe el segundo numero: "))
       if simbolo == "+":
           print(num1 + num2)
       elif simbolo == "-":
           print(num1 - num2)
       elif simbolo == "*":
           print(num1 * num2)
       elif simbolo == "/":
           print(num1 / num2)
       else:
           print("Error, intentelo de nuevo.")
           continue
       si_no = str(input("Quieres hacer otro calculo? (S/N): ")).lower()
       if si_no == "s":
           continue
       else:
           break
