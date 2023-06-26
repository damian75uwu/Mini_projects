"""
Proyectos para principiantes:
1. Par o impar
2. Juego Mad Libs
3. Contador de palabras
4. ¿Es palíndromo?
5. Información de la biografía
6. Calculador de propinas
7. ¿Cuál es el acrónimo?
8. Piedra, Papel y tijera
9. Adivina el número
10. Generador de letras
"""
# Project 1
def par_inpar():
   num = int(input("Escoge un número entre 1 y 1000: "))
   num2 = int(num) % 2
   print(num2)
   if num2 == 0:
       print(f"El número {num} es par!")
   elif num2 == 1:
       print(f"El número {num} es impar!")

# Project 2
def mad_lib():
   name = input("Escribe un nombre: ")
   pais = input("Escribe un pais: ")
   pet = input("Escribe una mascota: ")
   print(f"Erase una vez un señor/a llamado {name} que vivia en {pais} con su {pet}")

# Project 3
def contador_palabras():
   uwu = input("En que estas pensando: ")
   print("Tu frase tiene",len(uwu),"carracteres.")
   print("y tambien tiene", len(uwu.split()), "palabras.")

# Project 4
def es_palindromo():
   user = input("Escribe una palabra: ")
   palabra_invertida = user[::-1]
   print(palabra_invertida)
   if user == palabra_invertida:
       print(f"La palabra: {user}({palabra_invertida}), es un palíndromo.")
   elif user != palabra_invertida:
       print(f"La palabra: {user}({palabra_invertida}), no un palíndromo.")

# Project 5
def info_biogradia():
   while True:
       nom = input("Escribe tu nombre: ")
       edad = input("Escribe tu edad: ")
       fecha_n = input("Escribe tu fecha de nacimiento(dd/mm/aa): ")
       meta_per = input("Escribe tu meta personal: ")
       if not nom.isalpha():
           print("1 El arguento no es valido")
           continue
       if not meta_per.isalpha():
           print("2 El arguento no es valido")
           continue
       elif not edad.isdigit():
           print("3 El arguento no es valido")
           continue
       print(f"- Nombre: {nom}\n- Edad: {edad}\n- Fecha de nacimiento: {fecha_n}\n- Meta personal: {meta_per}")
       break

# Project 6
def calc_propinas():
  bill_amount = float(input("Escribe cuál es monto de la factura total de hoy: "))
  tip_percentage = float(input("Escribe cuál es el porcentaje de propinas de hoy: "))
  num_pople = int(input("¿Con cuantas personas compartes la factura?: "))
  tip_amount = bill_amount * tip_percentage /100
  bill_contribution = bill_amount / num_pople
  tip_contribution = tip_amount / num_pople
  total_contribution = bill_contribution + tip_contribution
  print(f"La factura por persona es de {bill_contribution} y la contribucion de propinas"
        f"es de {total_contribution} y por ultimo, el total de contribucion es {total_contribution}")

# Project 7
def tu_acronimo():
   while True:
       frase = input("Escribe una organizacion o concepto(max5/min2 palabras): ")
       uwu = frase.upper().split()
       uwu_list = list(uwu)
       uwu_list_num = len(uwu_list)
       if uwu_list_num >= 6:
           print("ERROR: Has escrito mas de 5 palabras")
           continue
       elif uwu_list_num <= 1:
           print("ERROR: Has escrito menos de 2 palabras")
           continue
       match uwu_list_num:
           case 2:
               uwu1 = uwu_list[0]
               uwu2 = uwu_list[1]
               print(f"Tu acrónimo (de la frase: {frase}) es: " + uwu1[0] + uwu2[0])
               break


           case 3:
               uwu1 = uwu_list[0]
               uwu2 = uwu_list[1]
               uwu3 = uwu_list[2]
               print(f"Tu acrónimo (de la frase: {frase}) es: "+uwu1[0]+uwu2[0]+uwu3[0])
               break
           case 4:
               uwu1 = uwu_list[0]
               uwu2 = uwu_list[1]
               uwu3 = uwu_list[2]
               uwu4 = uwu_list[3]
               print(f"Tu acrónimo (de la frase: {frase}) es: "+uwu1[0]+uwu2[0]+uwu3[0]+uwu4[0])
               break
           case 5:
               uwu1 = uwu_list[0]
               uwu2 = uwu_list[1]
               uwu3 = uwu_list[2]
               uwu4 = uwu_list[3]
               uwu5 = uwu_list[4]
               print(f"Tu acrónimo (de la frase: {frase}) es: "+uwu1[0]+uwu2[0]+uwu3[0]+uwu4[0]+uwu5[0])
               break

# Project 8
def piedra_papel_tijera():
   import random
   score_emp = 0
   score_gan = 0
   score_per = 0
   pc_op = ["piedra", "papel", "tijera"]
   while True:
       user = input("Escribe piedra, papel o tijera: ").lower()
       pc_rd = random.choice(pc_op)
       print("Jugador2 eligio: " + pc_rd)
       # EMPATE
       if user == "piedra" and pc_rd == "piedra":
           print("Empate!")
           score_emp += 1
           si_no = input("Quieres jugar de nuevo?(si/no): ").lower()
           if si_no == "si":
               continue
           else:
               print(f"Has empatado: {score_emp}, ganado: {score_gan} y perdido: {score_per} veces")
               break
       elif user == "papel" and pc_rd == "papel":
           print("Empate!")
           score_emp += 1
           si_no = input("Quieres jugar de nuevo?(si/no): ").lower()
           if si_no == "si":
               continue
           else:
               print(f"Has empatado: {score_emp}, ganado: {score_gan} y perdido: {score_per} veces")
               break
       elif user == "tijera" and pc_rd == "tijera":
           print("Empate!")
           score_emp += 1
           si_no = input("Quieres jugar de nuevo?(si/no): ").lower()
           if si_no == "si":
               continue
           else:
               print(f"Has empatado: {score_emp}, ganado: {score_gan} y perdido: {score_per} veces")
               break
       # GANAR
       if user == "piedra" and pc_rd == "tijera":
           print("Ganaste!!")
           score_gan += 1
           si_no = input("Quieres jugar de nuevo?(si/no): ").lower()
           if si_no == "si":
               continue
           else:
               print(f"Has empatado: {score_emp}, ganado: {score_gan} y perdido: {score_per} veces")
               break
       elif user == "papel" and pc_rd == "piedra":
           print("Ganaste!!")
           score_gan += 1
           si_no = input("Quieres jugar de nuevo?(si/no): ").lower()
           if si_no == "si":
               continue
           else:
               print(f"Has empatado: {score_emp}, ganado: {score_gan} y perdido: {score_per} veces")
               break
       elif user == "tijera" and pc_rd == "papel":
           print("Ganaste!!")
           score_gan += 1
           si_no = input("Quieres jugar de nuevo?(si/no): ").lower()
           if si_no == "si":
               continue
           else:
               print(f"Has empatado: {score_emp}, ganado: {score_gan} y perdido: {score_per} veces")
               break
       # PERDER
       if user == "piedra" and pc_rd == "papel":
           print("Perdiste...")
           score_per += 1
           si_no = input("Quieres jugar de nuevo?(si/no): ").lower()
           if si_no == "si":
               continue
           else:
               print(f"Has empatado: {score_emp}, ganado: {score_gan} y perdido: {score_per} veces")
               break
       elif user == "papel" and pc_rd == "tijera":
           print("Perdiste...")
           score_per += 1
           si_no = input("Quieres jugar de nuevo?(si/no): ").lower()
           if si_no == "si":
               continue
           else:
               print(f"Has empatado: {score_emp}, ganado: {score_gan} y perdido: {score_per} veces")
               break
       elif user == "tijera" and pc_rd == "piedra":
           print("Perdiste...")
           score_per += 1
           si_no = input("Quieres jugar de nuevo?(si/no): ").lower()
           if si_no == "si":
               continue
           else:
               print(f"Has empatado: {score_emp}, ganado: {score_gan} y perdido: {score_per} veces")
               break
       print(f"Has empatado: {score_emp}, ganado: {score_gan} y perdido: {score_per} veces")

# Project 9
def adivina_num():
   import random
   num = [0,1,2,3,4,5,6,7,8,9,10]
   num_rd = random.choice(num)
   score = 0
   while True:
       user = int(input("Elige un numero del 0 al 10: "))
       if user >= 11:
           print("Error: Es mayor a 10, intentalo de nuevo.")
           continue
       print(num_rd)
       if user == num_rd:
           print("Ganaste!!")
           score += 1
           si_no = input("Quieres jugar de nuevo?(si/no): ").lower()
           if si_no == "si":
               continue
           else:
               print(f"Has ganado {score} veces.")
               break
       elif user != num_rd:
           print("Perdiste...")
           si_no = input("Quieres jugar de nuevo?(si/no): ").lower()
           if si_no == "si":
               continue
           else:
               print(f"Has ganado {score} veces.")
               break
   print(f"Has ganado {score} veces.")

# Project 10
def generador_lyrics():
   while True:
       user = int(input("Elige una cancion entre estas y escribe su numero:\n"
                        "1. Middle of the night.\n"
                        "2. Don't wanna sleep.\n"
                        "3. Unholy.\n - "))
       if user == 1:
           mftn_letra = open("mftn.txt", "r")
           letra = mftn_letra.read()
           print(letra)
           mftn_letra.close()
           si_no = input("¿Quieres elegir otra cancion?(S/N)").lower()
           if si_no == "s":
               continue
           else:
               quit()
       elif user == 2:
           dws_letra = open("dws.txt", "r")
           letra = dws_letra.read()
           print(letra)
           dws_letra.close()
           si_no = input("¿Quieres elegir otra cancion?(S/N)").lower()
           if si_no == "s":
               continue
           else:
               quit()
       elif user == 3:
           unholy_letra = open("Unholy.txt", "r")
           letra = unholy_letra.read()
           print(letra)
           unholy_letra.close()
           si_no = input("¿Quieres elegir otra cancion?(S/N)").lower()
           if si_no == "s":
               continue
           else:
               quit()
