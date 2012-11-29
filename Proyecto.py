print "Bienvenido"
print "En este juego probaremos tus conocimientos basicos, asi que no temas :)"
score=0
estado=True


def metodo_salir(salir):
	if salir=="salir":
		exit()

while estado:
	
	pregunta = raw_input("Elige una pregunta del 1 al 10, (Cualquier otra tecla para terminar): ")
	if pregunta == '1':
		print "Que animal tiene en su nombre las cinco vocales?"
		respuesta1 = raw_input().lower()
		if respuesta1 == 'murcielago':
			print 'Correcto'
			score +=1			
			print "Puntaje: %i"%score + " puntos(s)"	 
		else:
			print 'Incorrecto, Murcielago, como que no tuviste infancia. JAJAJA!'
			print 'Puntuacion Final: '
			print score
			print 'Escriba "salir" para terminar'
			key = raw_input()
			metodo_salir(key)
			
	elif pregunta == '2':
		print "La operacion matematica: 8+9+3+5+6x0, es igual a:"
		respuesta2 = raw_input().lower()
		if respuesta2 == '25':
			print 'Correcto'
			score +=1			
			print "Puntaje: %i"%score + " puntos(s)"
		else:
			print 'Incorrecto, es 25, Ay! te toca regresar a primaria, JAJAJAJA'
			print 'Puntuacion Final: '
			print score
			print 'Escriba "salir" para terminar'
			key = raw_input()
			metodo_salir(key)
	elif pregunta == '3':
		print "El sol es un(a)?: "
		respuesta3 = raw_input().lower()
		if respuesta3 == 'estrella':
			print 'Correcto'
			score +=1			
			print "Puntaje: %i"%score + " puntos(s)"	
		else:
			print 'Incorrecto, es una estrella, y aunque no lo parezca es una de las mas pequenas conocidas'
			print 'Puntuacion Final: '
			print score
			print 'Escriba "salir" para terminar'
			key = raw_input()
			metodo_salir(key)
	elif pregunta == '4':
		print "Quien descubrio la fuerza de gravedad? (Solo apellido)"
		respuesta4 = raw_input().lower()
		if respuesta4 == 'newton':
			print 'Correcto'
			score +=1			
			print "Puntaje: %i"%score + " puntos(s)"
		else:
			print 'Incorrecto, fue Newton y su famosa manzana'
			print 'Puntuacion Final: '
			print score
			print 'Escriba "salir" para terminar'
			key = raw_input()
			metodo_salir(key)
	elif pregunta == '5':
		print "Cual es la ciencia que esta orientada al estudio de la vida?"
		respuesta5 = raw_input().lower()
		if respuesta5 == 'biologia':
			print 'Correcto'
			score +=1			
			print "Puntaje: %i"%score + " puntos(s)"		
		else:
			print 'Incorrecto, la Biologia es la ciencia orientada al estudia de la vida'
			print 'Puntuacion Final: '
			print score
			print 'Escriba "salir" para terminar'
			key = raw_input()
			metodo_salir(key)
	elif pregunta == '6':
		print "La cancion 'Hey Jude', es de? (nombre de banda en ingles)"
		respuesta6 = raw_input().lower()
		if respuesta6 == 'the beatles':
			print 'correcto'
			score +=1			
			print "Puntaje: %i"%score + " puntos(s)"		
		else:
			print 'Incorrecto, The Beatles '
			print 'Puntuacion Final: '
			print score
			print 'Escriba "salir" para terminar'
			key = raw_input()
			metodo_salir(key)
	elif pregunta == '7':
		print "La Segunda Guerra Mundial termino en el anyo?"
		respuesta7 = raw_input().lower()
		if respuesta7 == '1945':
			print 'correcto'
			score +=1			
			print "Puntaje: %i"%score + " puntos(s)"		
		else:
			print 'Incorrecto, termino en 1945. Como se nota que nunca jugaste Call of Duty, XD!'
			print 'Puntuacion Final: '
			print score
			print 'Escriba "salir" para terminar'
			key = raw_input()
			metodo_salir(key)
	elif pregunta == '8':
		print "Fueron los franceces los que marcaron la diferencia en la victoria de los aliados en la WWII? (V/F)"
		respuesta8 = raw_input().lower()
		if respuesta8 == 'f':
			print 'correcto'
			score +=1			
			print "Puntaje: %i"%score + " puntos(s)"		
		else:
			print 'Incorrecto, la diferencia fue marcada por EE.UU luego de unirse a los aliados'
			print 'Puntuacion Final: '
			print score
			print 'Escriba "salir" para terminar'
			key = raw_input()
			metodo_salir(key)
	elif pregunta == '9':
		print "se considera 'Mito' una narrativa que puede llegar a presentar hechos reales: (V/F)"
		respuesta9 = raw_input().lower()
		if respuesta9 == 'f':
			print 'correcto'
			score +=1			
			print "Puntaje: %i"%score + " puntos(s)"		
		else:
			print 'Incorrecto, son las leyendas las que pueden llegar a presentar hechos reales'
			print 'Puntuacion Final: '
			print score
			print 'Escriba "salir" para terminar'
			key = raw_input()
			metodo_salir(key)
	elif pregunta == '10':
		print "Saben tus padres que eres homosexual?"
		respuesta10 = raw_input().lower()
		if respuesta10 == 'si':
			print 'Me parece bien que tus padres respeten tus inclinaciones, pero cuidado con los homofobicos'
			score +=1			
			print "Puntaje: %i"%score + " puntos(s)"		
		else:
			print 'Creo que deberias de confiar en las personas mas cercanas a ti, tu familia y amigos entenderan, es hora de salir de ese closet. JAJAJA!'
			print 'Puntuacion Final: '
			print score
			print 'Escriba "salir" para terminar'
			key = raw_input()
			metodo_salir(key)		
	else:
		
			
		print 'Puntuacion Final: '
		print score
		print 'Escriba "salir" para terminar'
		key = raw_input()
		metodo_salir(key)
		

