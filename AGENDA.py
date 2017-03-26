# encoding: utf-8
import os
import time


class archivo(object):
    def __init__(self):
        self.lista = []
        self.mensajes = []
        self.historial = 0
        self.llamadas = []
        self.historialDellamadas = 0

    def limpiar(self):
        os.system("clear")

    # METODOS ARCHIVOS CONTACTOS

    def crearArchivo(self):
        archivo = open("contactos", "a")
        archivo.close()

    def crearArchivoNuevo(self):
        archivo = open("contactos", "w")
        archivo.close()

    def escribirArchivo(self):
        archivo = open("contactos", "w")
        self.lista.sort()
        for elemento in self.lista:
            archivo.write(elemento + "\n")
        archivo.close()

    def cargarArchivo(self):
        archivo = open("contactos", "r")
        self.lista.sort()
        linea = archivo.readline()
        if linea:
            while linea:
                if linea[-1] == "\n":
                    linea = linea[0:-1]
                self.lista.append(linea)
                linea = archivo.readline()
        archivo.close()

    # METODOS MENSAJES

    def crearArchivoMensajes(self):
        archivo = open("mensajes", "a")
        archivo.close()

    def escribirArchivoMensajes(self):
    	archivo = open("mensajes", "w")
    	for elemento in self.mensajes:
    		archivo.write(elemento + "\n")
    	archivo.close()

    def cargarArchivoMensajes(self):
    	archivo = open("mensajes", "r")
        linea = archivo.readline()
        if linea:
            while linea:
                if linea[-1] == "\n":
                    linea = linea[0:-1]
                self.mensajes.append(linea)
                self.historial = len(self.mensajes)
                linea = archivo.readline()
        archivo.close()

    # METODOS LLAMADAS

    def crearArchivoLlamadas(self):
        archivo = open("llamadas.txt", "a")
        archivo.close()

    def escribirArchivoLlamadas(self):
    	archivo = open("llamadas.txt", "w")
    	for elemento in self.llamadas:
    		archivo.write(elemento + "\n")
    	archivo.close()

    def cargarArchivoLlamadas(self):
    	archivo = open("llamadas.txt", "r")
        linea = archivo.readline()
        if linea:
            while linea:
                if linea[-1] == "\n":
                    linea = linea[0:-1]
                self.llamadas.append(linea)
                self.historialDellamadas = len(self.llamadas)
                linea = archivo.readline()
        archivo.close()

    def eliminarMensajes(self):
    	print " -------------------------------------------------------------------------------"
    	print " ====================|     ELIMINAR HISTORIAL DE MENSAJES   |==================="
    	print " -------------------------------------------------------------------------------"
    	eliminado = False

    	if ((self.mensajes != 0) and (self.historial != 0)):
	    	print " Seguro que desea eliminar el historial de mensajes enviados?"
	    	SN = raw_input("\n (s/n): ")

	    	if SN.lower() == 's':
				archivo = open("mensajes", "w")
				archivo.close()

				self.mensajes = []
				self.historial = 0

				print "\n 'Se ha eliminado todo el historial'"

        else:
        	print "\n 'Su historial de mensajes esta vacio'"

    # METODOS HISTORIAL DE MENSAJES

    def agregarAlHistorial(self):
    	self.historial += 1

    def historialMensajes(self):
    	print " -------------------------------------------------------------------------------"
    	print " =============================|   HISTORIAL SMS   |============================="
    	print " -------------------------------------------------------------------------------"
    	print "\n Mensajes enviados:", self.historial
    	print " -------------------------------------------------------------------------------"

    	for elemento in self.mensajes:
	        arreglo = elemento.split('\t')

	        print " Para:", arreglo[0]
	        print " Mensaje:", arreglo[1]
	        print "\t\t\t\t\t\t\tHora de envio:", arreglo[2]
	        print "\t\t\t\t\t\t\tFecha de envio:", arreglo[3]
	        print " -------------------------------------------------------------------------------"

	# METODOS HISTORIAL DE LLAMADAS

    def agregarAlHistorialDellamadas(self):
        self.historialDellamadas += 1

    def historialDellamadas(self):
		print " -------------------------------------------------------------------------------"
		print " =========================|   HISTORIAL DE LLAMADAS   |========================="
		print " -------------------------------------------------------------------------------"
		print "\n Llamadas realizadas:", self.historialDellamadas
		print " -------------------------------------------------------------------------------"

		for elemento in self.llamadas:
			arreglo = elemento.split('\t')

	        print " Para:", arreglo[0]
	        print "\t\t\t\t\t\t\tHora de llamada:", arreglo[1]
	        print "\t\t\t\t\t\t\tFin de llamada:", arreglo[2]
	        print "\t\t\t\t\t\t\tFecha de llamada:", arreglo[3]
	        print " -------------------------------------------------------------------------------"

	# METODOS CONTACTOS

    def crearContacto(self):
        print
        creado = False
        validarNombre = False

        while validarNombre == False:

            archivo.limpiar()
            print " -------------------------------------------------------------------------------"
            print " ============================|   NUEVO CONTACTO   |============================="
            print " -------------------------------------------------------------------------------"
            print

            nombre = raw_input(" Nombre: ")

            if len(nombre) == 0:
                print "\n\t\t\t\t     error!".upper()
                print "\n\t\t    'El campo (Nombre) no puede estar vacio'"
                print "                          Presione ENTER para continuar"
                raw_input()
                validarNombre = False

            else:
                encontrado = False

                for elemento in self.lista:
                    mostrar = elemento.split('\t')

                    if nombre.lower() == mostrar[0].lower():
                        encontrado = True
                        break

                    else:
                        encontrado = False


                if encontrado == True:
                    print "\n\t\t\t\t     error!".upper()
                    print "\n\t\t      'Ya tiene un contacto con ese nombre'"
                    print "                          Presione ENTER para continuar"
                    raw_input()
                    validarNombre = False

                else:
                    validarNombre = True
                    apellido = raw_input(" Apellido: ")

                    validarNumero = False
                    while validarNumero == False:
                        telefono = raw_input(" Numero de telefono: ")

                        if len(telefono) == 0:
                            print "\n\t\t\t\t     error!".upper()
                            print "\n\t\t    'El campo (Numero) no puede estar vacio'"
                            print "                          Presione ENTER para continuar"
                            raw_input()
                            validarNumero = False

                        elif not telefono.isdigit():
                        	print "\n\t\t\t\t     error!".upper()
                        	print "\n\t\t    'En este campo solo puede agregar numeros'"
                        	print "                          Presione ENTER para continuar"
                    		raw_input()
                    		validarNumero = False

                        else:
                            validarNumero = True
                            correo = raw_input(" Correo electronico: ")

                            print "\n Desea guardar este contacto?"
                            SN = raw_input(" (s/n): ")

                            if SN.lower() == 's':
                                self.lista.append(nombre + "\t" + apellido + "\t" + telefono + "\t" + correo + "\t")
                                creado = True

                            else:
                                creado = False
                                print "\n 'El contacto no se ha guardado'"

                            if creado == True:
                                print "\n                     'Nuevo contacto añadido a su agenda'"
                                archivo.escribirArchivo()
                                
    def mostrarContacto(self):
        listaVacia = True
        self.lista.sort()
        for i, elemento in enumerate(self.lista):
            i += 1
            mostrar = elemento.split('\t')
            print " " + str(i) + ") " + mostrar[0] + "\t     " + mostrar[1] + "\t         " + mostrar[2] + "\t " + mostrar[3]
            print " -------------------------------------------------------------------------------"
            listaVacia = False

        if listaVacia == True:
            print "\n 'Su lista de contactos esta vacia'"

    def eliminarCONTACTOS(self):

        if len(self.lista) == 0:
            print "\n 'Su lista de contactos esta vacia'"

        else:
            print " Seguro que desea eliminar todos los contactos?"
            SN = raw_input("\n (s/n): ")

            if SN.lower() == 's':

                self.lista = []

                if self.lista == []:
                    print "\n 'Se han eliminado todos los contactos'"
                    archivo.escribirArchivo()

    def buscarContactoNombre(self):
        campovacio = True

        while campovacio == True:
            archivo.limpiar()
            print " -------------------------------------------------------------------------------"
            print " ===========================|   BUSCAR POR NOMBRE   |==========================="
            print " -------------------------------------------------------------------------------"
            nombre = raw_input("\n Ingrese el nombre que desea buscar: ")
            print

            if len(nombre) == 0:
                print "\t\t\t'El campo de busqueda esta vacio'"
                print "\n Desea buscar con otro nombre?"
                SN = raw_input(" (s/n): ")

                if SN.lower() == 's':
                    campovacio = True

                else:
                    campovacio = False

            else:
                menuBus = True
                while menuBus == True:
                    noEncontrado = True
                    
                    for elemento in self.lista:
                        mostrar = elemento.split('\t')
                        if nombre.lower() == mostrar[0].lower():
                            archivo.limpiar()
                            print " Contacto encontrado: "
                            print "\n |      Nombre      |     Apellido      |    Telefono    |        Correo       |"
                            print " -------------------------------------------------------------------------------"
                            print "  " + mostrar[0] + "\t     " + mostrar[1] + "\t         " + mostrar[2] + "\t " + mostrar[3]
                            print " -------------------------------------------------------------------------------"
                            noEncontrado = False

                    if noEncontrado == False:
                        print
                        print "                                    Opciones     \n"
                        print "       (A) Eliminar  -  (B) Actualizar  -  (C) Enviar SMS  -  (D) llamar "
                        print
                        print "\n              'Presione ENTER si no desea realizar ninguna accion' "
                        print
                        opcion = raw_input(" Opcion > ")

                        if opcion.lower() == 'a':
                            archivo.limpiar()
                            print " -------------------------------------------------------------------------------"
                            print " =============================|     ELIMINAR     |=============================="
                            print " -------------------------------------------------------------------------------"
                            print " Seguro que desea eliminar este contacto?"
                            SN = raw_input("\n (s/n): ")

                            if SN.lower() == 's':
                                eliminado = False

                                for elemento in self.lista:
                                    mostrar = elemento.split("\t")

                                    if nombre.lower() == mostrar[0].lower():
                                        self.lista.remove(elemento)
                                        eliminado = True
                                        
                                if eliminado == True:
                                    archivo.escribirArchivo()
                                    print " \n 'El contacto ha sido eliminado'"
                                    menuBus = False
                                    campovacio = False

                        elif opcion.lower() == 'b':
                            menuAct = True
                            while menuAct == True:
                                archivo.limpiar()
                                print " -------------------------------------------------------------------------------"
                                print " ============================|     ACTUALIZAR     |============================="
                                print " -------------------------------------------------------------------------------"
                                print " |       (1) ACTUALIZAR NOMBRE          |        (2) ACTUALIZAR APELLIDO       |"
                                print " -------------------------------------------------------------------------------"
                                print " |       (3) ACTUALIZAR TELEFONO        |        (4) ACTUALIZAR CORREO         |"
                                print " -------------------------------------------------------------------------------"
                                print "\n                 'Presione ENTER para volver al menu anterior'\n"
                                opcion = raw_input(" Opcion > ")

                                if opcion == "1":
                                    nombreActualizado = False
                                    validarNombre = False

                                    while validarNombre == False:
                                        archivo.limpiar()
                                        print " -------------------------------------------------------------------------------"
                                        print " =========================|     ACTUALIZAR NOMBRE     |========================="
                                        print " -------------------------------------------------------------------------------"

                                        for elemento in self.lista:
                                            mostrar = elemento.split("\t")

                                        mostrar[0] = raw_input("\n Nuevo nombre: ")

                                        if len(mostrar[0]) == 0:
                                            print "\n\t\t\t\t     error!".upper()
                                            print "\n\t\t    'El campo (Nombre) no puede estar vacio'"
                                            print "                          Presione ENTER para continuar"
                                            raw_input()
                                            validarNombre = False

                                        else:
                                            for elemento in self.lista:
                                                arreglo = elemento.split('\t')

                                                if mostrar[0].lower() == arreglo[0].lower():
                                                    encontrado = True
                                                    break

                                                else:
                                                    encontrado = False

                                            if encontrado == True:
                                                print "\n\t\t\t\t     error!".upper()
                                                print "\n\t\t      'Ya tiene un contacto con ese nombre'"
                                                print "                          Presione ENTER para continuar"
                                                raw_input()
                                                validarNombre = False

                                            else:	                                            		
                                        		validarNombre = True
                                        		print "\n Desea guardar los cambios?"
                                        		SN = raw_input("\n (s/n): ")

                                        		if SN.lower() == 's':
                                        			self.lista.remove(elemento)
                                        			menuAct = False
                                        			self.lista.append(mostrar[0] + "\t" + mostrar[1] + "\t" + mostrar[2] + "\t" + mostrar[3] + "\t")
                                        			nombre = mostrar[0]
                                        			nombreActualizado = True

                                        		else:
                                        			nombreActualizado = False

                                    if nombreActualizado == True:
                                    	archivo.escribirArchivo()
                                    	print "\n 'Nombre actualizado'"
                                    	raw_input("\n                         'Presione ENTER para continuar'\n")
                                    	menuAct = True
                                    	continue

                                    if nombreActualizado == False:
                                    	print "\n 'No se han guardado los cambios'"
                                    	raw_input("\n                         'Presione ENTER para continuar'\n")
                                    	menuAct = True
                                    	continue


                                if opcion == "2":
                                    apellidoActualizado = False
                                    for elemento in self.lista:
                                        mostrar = elemento.split("\t")

                                        if nombre.lower() == mostrar[0].lower():
                                            archivo.limpiar()
                                            print " -------------------------------------------------------------------------------"
                                            print " ========================|     ACTUALIZAR APELLIDO     |========================"
                                            print " -------------------------------------------------------------------------------"
                                            mostrar[1] = raw_input("\n Nuevo apellido: ")
                                            menuAct = False

                                            print "\n Desea guardar los cambios?"
                                            SN = raw_input("\n (s/n): ")

                                            if SN.lower() == 's':
                                            	self.lista.remove(elemento)
                                            	self.lista.append(mostrar[0] + "\t" + mostrar[1] + "\t" + mostrar[2] + "\t" + mostrar[3] + "\t")
                                            	apellidoActualizado = True

                                            else:
                                            	apellidoActualizado = False

                                    if apellidoActualizado == True:
                                    	archivo.escribirArchivo()
                                        print "\n 'Apellido actualizado'"
                                        raw_input("\n                         'Presione ENTER para continuar'\n")  
                                        menuAct = True
                                        continue

                                    if apellidoActualizado == False:
		                            	print "\n 'No se han guardado los cambios'"
		                            	raw_input("\n                         'Presione ENTER para continuar'\n")
		                            	menuAct = True
		                            	continue

                                if opcion == "3":
                                    telefonoActualizado = False
                                    for elemento in self.lista:
                                        mostrar = elemento.split("\t")

                                        if nombre.lower() == mostrar[0].lower():

                                            validarNumero = False
                                            while validarNumero == False:
	                                            archivo.limpiar()
	                                            print " -------------------------------------------------------------------------------"
	                                            print " =======================|     ACTUALIZAR TELEFONO     |========================="
	                                            print " -------------------------------------------------------------------------------"
	                                            mostrar[2] = raw_input("\n Nuevo telefono: ")

	                                            if len(mostrar[2]) == 0:
	                                            	print "\n\t\t\t\t     error!".upper()
	                                            	print "\n\t\t       'Este campo no debe estar vacio'"
	                                            	print "                         Presione ENTER para continuar"
	                                            	raw_input()
	                                            	validarNumero = False

	                                            elif not mostrar[2].isdigit():
	                                            	print "\n\t\t\t\t     error!".upper()
                                            		print "\n\t\t   'En este campo solo puede agregar numeros'"
                                            		print "                          Presione ENTER para continuar"
	                                            	raw_input()
	                                            	validarNumero = False

	                                            else:
	                                            	validarNumero = True
	                                            	print "\n Desea guardar los cambios?"
	                                            	SN = raw_input("\n (s/n): ")

	                                            	if SN.lower() == 's':
	                                            		self.lista.remove(elemento)
	                                            		self.lista.append(mostrar[0] + "\t" + mostrar[1] + "\t" + mostrar[2] + "\t" + mostrar[3] + "\t")
	                                            		telefonoActualizado = True

	                                            	else:
		                                            	telefonoActualizado = False

                                    if telefonoActualizado == True:
                                    	archivo.escribirArchivo()
                                        print "\n 'Telefono actualizado'"
                                        raw_input("\n                         'Presione ENTER para continuar'\n")  
                                        menuAct = True
                                        continue

                                    if telefonoActualizado == False:
		                            	print "\n 'No se han guardado los cambios'"
		                            	raw_input("\n                         'Presione ENTER para continuar'\n")
		                            	menuAct = True
		                            	continue

                                if opcion == "4":
                                    correoActualizado = False
                                    for elemento in self.lista:
                                        mostrar = elemento.split("\t")

                                        if nombre.lower() == mostrar[0].lower():
                                        	archivo.limpiar()
                                        	print " -------------------------------------------------------------------------------"
                                        	print " ========================|     ACTUALIZAR CORREO     |=========================="
                                        	print " -------------------------------------------------------------------------------"
                                        	mostrar[3] = raw_input("\n Nuevo correo: ")
                                        	menuAct = False

                                        	print "\n Desea guardar los cambios?"
                                        	SN = raw_input("\n (s/n): ")

                                        	if SN.lower() == 's':
                                        		self.lista.remove(elemento)
                                        		self.lista.append(mostrar[0] + "\t" + mostrar[1] + "\t" + mostrar[2] + "\t" + mostrar[3] + "\t")
                                        		correoActualizado = True

                                        	else:
                                        		correoActualizado = False

                                    if correoActualizado == True:
                                    	archivo.escribirArchivo()
                                    	print "\n 'Correo actualizado'"
                                    	raw_input("\n                         'Presione ENTER para continuar'\n")
                                    	menuAct = True
                                    	continue

                                    if correoActualizado == False:
                                    	print "\n 'No se han guardado los cambios'"
                                    	raw_input("\n                         'Presione ENTER para continuar'\n")
                                    	menuAct = True
                                    	continue

                                else:
                                    menuAct = False
                                    menuBus = True
                                    archivo.escribirArchivo()

                        elif opcion.lower() == 'c':
                            archivo.limpiar()
                            mensajeEnviado = False

                            while mensajeEnviado == False:
                                print " -------------------------------------------------------------------------------"
                                print " ===========================|     ENVIAR MENSAJE    |==========================="
                                print " -------------------------------------------------------------------------------"
                                print
                                print " Para:", nombre
                                print " Mensaje: \n"

                                horaDeEnvio = time.strftime("%I:%M:%S")
                                fechaDeEnvio = time.strftime("%d/%m/%y")
                       
                                mensaje = raw_input(" ")

                                archivo.limpiar()
                                print " -------------------------------------------------------------------------------"
                                print " ===========================|     ENVIAR MENSAJE    |==========================="
                                print " -------------------------------------------------------------------------------"
                                print
                                print " Enviar mensaje?"
                                SN = raw_input("\n (s/n): ")

                                if SN.lower() == 's':
                                	mensajeEnviado = True

                                else:
                                	print "\n 'Mensaje no enviado'"
                                	raw_input()
                                	break

                            if mensajeEnviado == True:
                                self.mensajes.append(nombre + '\t' + mensaje + "\t" + horaDeEnvio + '\t' + fechaDeEnvio)
                                archivo.agregarAlHistorial()
                                archivo.escribirArchivoMensajes()
                                print "\n 'Mensaje enviado'"
                                raw_input()

                        else:
                            menuBus = False
                            campovacio = False
                            archivo.escribirArchivo()

                    if noEncontrado == True:
                        print " 'El nombre '%s' no se ha encontrado'" % (nombre)
                        print "\n Desea buscar con otro nombre?"
                        SN = raw_input(" (s/n): ")
                        if SN.lower() == 's':
                            break

                        else:
                            campovacio = False
                            break

    def buscarContactoNumero(self):
        campovacio = True

        while campovacio == True:
            archivo.limpiar()
            print " -------------------------------------------------------------------------------"
            print " ===========================|   BUSCAR POR NUMERO   |==========================="
            print " -------------------------------------------------------------------------------"
            numero = raw_input("\n Ingrese el numero que desea buscar: ")
            print

            if len(numero) == 0:
                print "\t\t\t'El campo de busqueda esta vacio'"
                print "\n Desea buscar con otro numero?"
                SN = raw_input(" (s/n): ")

                if SN.lower() == 's':
                    campovacio = True

                else:
                    campovacio = False

            else:
                menuBus = True
                while menuBus == True:
                    noEncontrado = True

                    for elemento in self.lista:
                        mostrar = elemento.split('\t')
                        if numero == mostrar[2]:
                            archivo.limpiar()
                            print " Contacto encontrado: "
                            print "\n |      Nombre      |     Apellido      |    Telefono    |        Correo       |"
                            print " -------------------------------------------------------------------------------"
                            print "  " + mostrar[0] + "\t     " + mostrar[1] + "\t         " + mostrar[2] + "\t " + mostrar[3]
                            print " -------------------------------------------------------------------------------"
                            noEncontrado = False

                    if noEncontrado == False:
                        print
                        print "                                     Opciones     \n"
                        print "       (A) Eliminar  -  (B) Actualizar  -  (C) Enviar SMS  -  (D) llamar "
                        print
                        print "\n              'Presione ENTER si no desea realizar ninguna accion' "
                        print
                        opcion = raw_input(" Opcion > ")

                        if opcion.lower() == 'a':
                            archivo.limpiar()
                            print " -------------------------------------------------------------------------------"
                            print " =============================|     ELIMINAR     |=============================="
                            print " -------------------------------------------------------------------------------"
                            print
                            print " Seguro que desea eliminar este contacto?"
                            SN = raw_input("\n (s/n): ")

                            if SN.lower() == 's':
                                eliminado = False

                                for elemento in self.lista:
                                    mostrar = elemento.split("\t")

                                    if numero == mostrar[2]:
                                        self.lista.remove(elemento)
                                        eliminado = True

                                if eliminado == True:
                                    archivo.escribirArchivo()
                                    print "\n 'El contacto ha sido eliminado'"
                                    menuBus = False
                                    campovacio = False

                        elif opcion.lower() == 'b':
                            menuAct = True
                            while menuAct == True:
                                archivo.limpiar()
                                print " -------------------------------------------------------------------------------"
                                print " ============================|     ACTUALIZAR     |============================="
                                print " -------------------------------------------------------------------------------"
                                print " |       (1) ACTUALIZAR NOMBRE          |        (2) ACTUALIZAR APELLIDO       |"
                                print " -------------------------------------------------------------------------------"
                                print " |       (3) ACTUALIZAR TELEFONO        |        (4) ACTUALIZAR CORREO         |"
                                print " -------------------------------------------------------------------------------"
                                print "\n                 'Presione ENTER para volver al menu anterior'\n"
                                opcion = raw_input(" Opcion > ")

                                if opcion == "1":
                                    nombreActualizado = False
                                    validarNombre = False

                                    while validarNombre == False:
                                        archivo.limpiar()
                                        print " -------------------------------------------------------------------------------"
                                        print " =========================|     ACTUALIZAR NOMBRE     |========================="
                                        print " -------------------------------------------------------------------------------"

                                        for elemento in self.lista:
                                            mostrar = elemento.split("\t")

                                        mostrar[0] = raw_input("\n Nuevo nombre: ")

                                        if len(mostrar[0]) == 0:
                                        	print "\n\t\t\t\t     error!".upper()
                                        	print "\n\t\t    'El campo (Nombre) no puede estar vacio'"
                                        	print "                          Presione ENTER para continuar"
                                        	raw_input()
                                        	validarNombre = False

                                        else:
                                        	for elemento in self.lista:
                                        		arreglo = elemento.split('\t')

                                        		if mostrar[0].lower() == arreglo[0].lower():
                                        			encontrado = True
                                        			break

                                        		else:
                                        			encontrado = False

                                        	if encontrado == True:
                                        		print "\n\t\t\t\t     error!".upper()
                                        		print "\n\t\t      'Ya tiene un contacto con ese nombre'"
                                        		print "                          Presione ENTER para continuar"
                                        		raw_input()
                                        		validarNombre = False

                                        	else:
                                        		validarNombre = True
                                        		print "\n Desea guardar los cambios?"
                                        		SN = raw_input("\n (s/n): ")

                                        		if SN.lower() == 's':
                                        			self.lista.remove(elemento)
                                        			menuAct = False
                                        			self.lista.append(mostrar[0] + "\t" + mostrar[1] + "\t" + mostrar[2] + "\t" + mostrar[3] + "\t")
                                        			nombre = mostrar[0]
                                        			nombreActualizado = True

                                        		else:
                                        			nombreActualizado = False

                                    if nombreActualizado == True:
                                    	archivo.escribirArchivo()
                                    	print "\n 'Nombre actualizado'"
                                    	raw_input("\n                         'Presione ENTER para continuar'\n")
                                    	menuAct = True
                                    	continue

                                    if nombreActualizado == False:
                                    	print "\n 'No se han guardado los cambios'"
                                    	raw_input("\n                         'Presione ENTER para continuar'\n")
                                    	menuAct = True
                                    	continue


                                if opcion == "2":
                                    apellidoActualizado = False
                                    for elemento in self.lista:
                                        mostrar = elemento.split("\t")

                                        if numero in mostrar[2]:
                                            archivo.limpiar()
                                            print " -------------------------------------------------------------------------------"
                                            print " ========================|     ACTUALIZAR APELLIDO     |========================"
                                            print " -------------------------------------------------------------------------------"
                                            mostrar[1] = raw_input("\n Nuevo apellido: ")
                                            menuAct = False

                                            print "\n Desea guardar los cambios?"
                                            SN = raw_input("\n (s/n): ")

                                            if SN.lower() == 's':
                                            	self.lista.remove(elemento)
                                            	self.lista.append(mostrar[0] + "\t" + mostrar[1] + "\t" + mostrar[2] + "\t" + mostrar[3] + "\t")
                                            	apellidoActualizado = True

                                            else:
                                            	apellidoActualizado = False

                                    if apellidoActualizado == True:
                                    	archivo.escribirArchivo()
                                    	print "\n 'Apellido actualizado'"
                                    	raw_input("\n                         'Presione ENTER para continuar'\n")
                                    	menuAct = True
                                    	continue

                                    if apellidoActualizado == False:
                                    	print "\n 'No se han guardado los cambios'"
                                    	raw_input("\n                         'Presione ENTER para continuar'\n")
                                    	menuAct = True
                                    	continue

                                if opcion == "3":
                                    telefonoActualizado = False
                                    for elemento in self.lista:
                                        mostrar = elemento.split("\t")

                                        if numero.lower() == mostrar[2].lower():
                                            validarNumero = False
                                            while validarNumero == False:
                                                archivo.limpiar()
                                                print " -------------------------------------------------------------------------------"
                                                print " =======================|     ACTUALIZAR TELEFONO     |========================="
                                                print " -------------------------------------------------------------------------------"
                                                mostrar[2] = raw_input("\n Nuevo telefono: ")

                                                if len(mostrar[2]) == 0:
                                                    print "\n\t\t\t\t     error!".upper()
                                                    print "\n\t\t       'Este campo no debe estar vacio'"
                                                    print "                         Presione ENTER para continuar"
                                                    raw_input()
                                                    validarNumero = False

                                                elif not mostrar[2].isdigit():
                                                    print "\n\t\t\t\t     error!".upper()
                                                    print "\n\t\t   'En este campo solo puede agregar numeros'"
                                                    print "                          Presione ENTER para continuar"
                                                    raw_input()
                                                    validarNumero = False

                                                else:
                                                    validarNumero = True
                                                    print "\n Desea guardar los cambios?"
                                                    SN = raw_input("\n (s/n): ")

                                                    if SN.lower() == 's':
                                                        self.lista.remove(elemento)
                                                        self.lista.append(mostrar[0] + "\t" + mostrar[1] + "\t" + mostrar[2] + "\t" + mostrar[3] + "\t")
                                                        numero = mostrar[2]
                                                        telefonoActualizado = True

                                                    else:
                                                        telefonoActualizado = False

                                    if telefonoActualizado == True:
                                        archivo.escribirArchivo()
                                        print "\n 'Telefono actualizado'"
                                        raw_input("\n                         'Presione ENTER para continuar'\n")
                                        menuAct = True
                                        continue

                                    if telefonoActualizado == False:
                                        print "\n 'No se han guardado los cambios'"
                                        raw_input("\n                         'Presione ENTER para continuar'\n")
                                        menuAct = True
                                        continue


                                if opcion == "4":
                                    correoActualizado = False
                                    for elemento in self.lista:
                                        mostrar = elemento.split("\t")

                                        if numero in mostrar[2]:
                                            archivo.limpiar()
                                            print " -------------------------------------------------------------------------------"
                                            print " ========================|     ACTUALIZAR CORREO     |=========================="
                                            print " -------------------------------------------------------------------------------"
                                            mostrar[3] = raw_input("\n Nuevo correo: ")
                                            menuAct = False

                                            print "\n Desea guardar los cambios?"
                                            SN = raw_input("\n (s/n): ")

                                            if SN.lower() == 's':
                                                self.lista.remove(elemento)
                                                self.lista.append(mostrar[0] + "\t" + mostrar[1] + "\t" + mostrar[2] + "\t" + mostrar[3] + "\t")
                                                correoActualizado = True

                                            else:
                                                correoActualizado = False

                                    if correoActualizado == True:
                                        archivo.escribirArchivo()
                                        print "\n 'Correo actualizado'"
                                        raw_input("\n                         'Presione ENTER para continuar'\n")
                                    	menuAct = True
                                    	continue

                                    if correoActualizado == False:
                                    	print "\n 'No se han guardado los cambios'"
                                    	raw_input("\n                         'Presione ENTER para continuar'\n")
                                    	menuAct = True
                                    	continue

                                else:
                                    menuAct = False
                                    menuBus = True
                                    archivo.escribirArchivo()

                        elif opcion.lower() == 'c':
                            archivo.limpiar()
                            mensajeEnviado = False

                            while mensajeEnviado == False:
                                print " -------------------------------------------------------------------------------"
                                print " ===========================|     ENVIAR MENSAJE    |==========================="
                                print " -------------------------------------------------------------------------------"
                                print
                                print " Para:", mostrar[0]
                                print " Mensaje: \n"

                                horaDeEnvio = time.strftime("%I:%M:%S")
                                fechaDeEnvio = time.strftime("%d/%m/%y")
                       
                                mensaje = raw_input(" ")

                                archivo.limpiar()
                                print " -------------------------------------------------------------------------------"
                                print " ===========================|     ENVIAR MENSAJE    |==========================="
                                print " -------------------------------------------------------------------------------"
                                print
                                print " Enviar mensaje?"
                                SN = raw_input("\n (s/n): ")

                                if SN.lower() == 's':
                                	mensajeEnviado = True

                                else:
                                	print "\n 'Mensaje no enviado'"
                                	raw_input()
                                	break

                            if mensajeEnviado == True:
                            	archivo.agregarAlHistorial()
                            	self.mensajes.append(mostrar[0] + '\t' + mensaje + "\t" + horaDeEnvio + '\t' + fechaDeEnvio)
                            	archivo.escribirArchivoMensajes()
                            	print "\n 'Mensaje enviado'"
                            	raw_input()

                        else:
                            menuBus = False
                            campovacio = False

                    if noEncontrado == True:
                        print " 'El numero '%s' no se ha encontrado'" % (numero)
                        print "\n Desea buscar con otro numero?"
                        SN = raw_input(" (s/n): ")
                        if SN.lower() == 's':
                            break

                        else:
                            campovacio = False
                            break

    def enviarSMS(self):
        print " -------------------------------------------------------------------------------"
        print " ===========================|     ENVIAR MENSAJE    |==========================="
        print " -------------------------------------------------------------------------------"
        print " |       [A] SMS a un contacto          |         [B] SMS a un numero          |"
        print " -------------------------------------------------------------------------------"

        opcion = raw_input("\n Opcion > ")

        if opcion.lower() == 'b':
            archivo.limpiar()

            while True:
                print " -------------------------------------------------------------------------------"
                print " ===========================|     ENVIAR MENSAJE    |==========================="
                print " -------------------------------------------------------------------------------"

                numero = raw_input("\n Numero del contacto: ")

                if not numero.isdigit():
                    print "\n 'Ingrese un numero de telefono valido'"
                    raw_input()
                    archivo.limpiar()

                else:
                    archivo.limpiar()
                    print " -------------------------------------------------------------------------------"
                    print " ===========================|     ENVIAR MENSAJE    |==========================="
                    print " -------------------------------------------------------------------------------"

                    print "\n Para:", numero
                    print " Mensaje: \n"

                    horaDeEnvio = time.strftime("%I:%M:%S")
                    fechaDeEnvio = time.strftime("%d/%m/%y")

                    mensaje = raw_input(" ")
                    archivo.limpiar()
                    print " -------------------------------------------------------------------------------"
                    print " ===========================|     ENVIAR MENSAJE    |==========================="
                    print " -------------------------------------------------------------------------------"
                    print
                    print " Enviar mensaje?"
                    SN = raw_input("\n (s/n): ")

                    if SN.lower() == 's':
                        archivo.agregarAlHistorial()
                        self.mensajes.append(str(numero) + '\t' + mensaje + "\t" + horaDeEnvio + '\t' + fechaDeEnvio)
                        archivo.escribirArchivoMensajes()
                        print "\n 'Mensaje enviado'"
                        break
                        archivo.limpiar()

                    else:
                        print "\n 'Mensaje no enviado'"
                        break
                        archivo.limpiar()


        if opcion.lower() == 'a':
            archivo.limpiar()
            print " -------------------------------------------------------------------------------"
            print " ===========================|     ENVIAR MENSAJE    |==========================="
            print " -------------------------------------------------------------------------------"
            nombre = raw_input("\n Nombre del contacto: ")

            noEncontrado = True
            for elemento in self.lista:
                mostrar = elemento.split('\t')
                if nombre.lower() == mostrar[0].lower():
                    noEncontrado = False

                    archivo.limpiar()
                    print " -------------------------------------------------------------------------------"
                    print " ===========================|     ENVIAR MENSAJE    |==========================="
                    print " -------------------------------------------------------------------------------"
                    print
                    print " Para:", mostrar[0]
                    print " Mensaje: \n"

                    horaDeEnvio = time.strftime("%I:%M:%S")
                    fechaDeEnvio = time.strftime("%d/%m/%y")

                    mensaje = raw_input(" ")

                    archivo.limpiar()
                    print " -------------------------------------------------------------------------------"
                    print " ===========================|     ENVIAR MENSAJE    |==========================="
                    print " -------------------------------------------------------------------------------"
                    print
                    print " Enviar mensaje?"
                    SN = raw_input("\n (s/n): ")

                    if SN.lower() == 's':
                        self.mensajes.append(mostrar[0] + '\t' + mensaje + "\t" + horaDeEnvio + '\t' + fechaDeEnvio)
                        archivo.agregarAlHistorial()
                        archivo.escribirArchivoMensajes()
                        print "\n 'Mensaje enviado'"

                    else:
                        print "\n 'Mensaje no enviado'"

            if (noEncontrado == True):
                print "\n 'El contacto '%s' no se ha encontrado en su agenda'" % (nombre)

                print "\n Desea agregar este contacto a su agenda?"
                SN = raw_input("\n (s/n): ")

                if (SN.lower() == 's'):
                    archivo.crearContacto()
                    print"\t\t\t'Presione ENTER para continuar'"
                    raw_input()
                    archivo.limpiar()
                    archivo.enviarSMS()

    def llamarAUnContacto(self):
    	print " -------------------------------------------------------------------------------"
        print " =========================|   LLAMAR A UN CONTACTO   |=========================="
        print " -------------------------------------------------------------------------------"
        print " |      [A] Contacto de la agenda       |      [B] Contacto Desconocido        |"
    	print " -------------------------------------------------------------------------------"

    	opcion = raw_input("\n Opcion > ")

    	if opcion.lower() == 'a':
            archivo.limpiar()
            print " -------------------------------------------------------------------------------"
            print " =========================|   LLAMAR A UN CONTACTO   |=========================="
            print " -------------------------------------------------------------------------------"

            nombre = raw_input("\n Nombre del contacto: ")

            archivo.limpiar()
            print " -------------------------------------------------------------------------------"
            print " =========================|   LLAMAR A UN CONTACTO   |=========================="
            print " -------------------------------------------------------------------------------"
            print "\n Llamada para: " + nombre
            print "\n                       'Presione ENTER para iniciar la llamada' "
            print
            opcion = raw_input(" Opcion > ")
            print "\n Realizando llamada..."

            volverALlamar = True
            while volverALlamar == True:

            	i = 0
            	duracion = 0

            	fechaDeLlamada = time.strftime("%d/%m/%y")
            	horaDeLlamada = time.strftime("%I:%M:%S")

            	while i <= 10:	
            		time.sleep(1)
            		archivo.limpiar()
            		print " -------------------------------------------------------------------------------"
            		print " =========================|   LLAMAR A UN CONTACTO   |=========================="
            		print " -------------------------------------------------------------------------------"
	            	print
            		print " LLAMANDO..."
            		print "\n                  'Presione ENTER para finalizar la llamada' "
            		duracion += 1
            		i += 1
            		print " Duracion: " + str(duracion) + "s"

            		time.sleep(1)
            		archivo.limpiar()
            		print " -------------------------------------------------------------------------------"
            		print " =========================|   LLAMAR A UN CONTACTO   |=========================="
            		print " -------------------------------------------------------------------------------"
	            	print
	            	print
	            	print "\n                  'Presione ENTER para finalizar la llamada' "
	            	duracion += 1
	            	i += 1
	            	print " Duracion: " + str(duracion) + "s"

                finDeLallamada = time.strftime("%I:%M:%S")
                archivo.limpiar()
                print " -------------------------------------------------------------------------------"
                print " =========================|   LLAMAR A UN CONTACTO   |=========================="
                print " -------------------------------------------------------------------------------"
                print "\n Duracion de la llamada: " + str(duracion) + "s"
                print "\n 'Llamada finalizada'"

                self.llamadas.append(nombre + "\t" + horaDeLlamada + '\t'+ finDeLallamada + '\t' + fechaDeLlamada)
                archivo.agregarAlHistorialDellamadas()
                archivo.escribirArchivoLlamadas()

                print "\n Desea volver a llamar?"
                SN = raw_input(" (s/n): ")

                if SN.lower() == 's':
                	volverALlamar = True

                else:
                	volverALlamar = False

        if opcion.lower() == 'b':
            archivo.limpiar()
            validarNumero = True

            while validarNumero == True:
	            print " -------------------------------------------------------------------------------"
	            print " =========================|   LLAMAR A UN CONTACTO   |=========================="
	            print " -------------------------------------------------------------------------------"

	            numero = raw_input("\n Numero del contacto: ")

	            if not numero.isdigit():
	                print "\n 'Ingrese un numero de telefono valido'"
	                raw_input()
	                validarNumero = True
	                archivo.limpiar()

	            else:
	            	validarNumero = False
	            	archivo.limpiar()
	            	print " -------------------------------------------------------------------------------"
	                print " =========================|   LLAMAR A UN CONTACTO   |=========================="
	                print " -------------------------------------------------------------------------------"
	            	print "\n Llamada para: " + numero
	            	print "\n                    'Presione ENTER para iniciar la llamada' "
	            	print
	            	opcion = raw_input(" Opcion > ")
	            	print "\n Realizando llamada..."

	            	volverALlamar = True
	            	while volverALlamar == True:

	                    i = 0
	                    duracion = 0

	                    fechaDeLlamada = time.strftime("%d/%m/%y")
	                    horaDeLlamada = time.strftime("%I:%M:%S")

	                    while i <= 10:
	                        time.sleep(1)
	                        archivo.limpiar()
	                        print " -------------------------------------------------------------------------------"
	                        print " =========================|   LLAMAR A UN CONTACTO   |=========================="
	                        print " -------------------------------------------------------------------------------"
	                        print
	                        print " LLAMANDO..."
	                        print "\n                  'Presione ENTER para finalizar la llamada' "
	                        duracion += 1
	                        i += 1
	                        print " Duracion: " + str(duracion) + "s"

	                        time.sleep(1)
	                        archivo.limpiar()
	                        print " -------------------------------------------------------------------------------"
	                        print " =========================|   LLAMAR A UN CONTACTO   |=========================="
	                        print " -------------------------------------------------------------------------------"
	                        print
	                        print
	                        print "\n                  'Presione ENTER para finalizar la llamada' "
	                        duracion += 1
	                        i += 1
	                        print " Duracion: " + str(duracion) + "s"

	                    finDeLallamada = time.strftime("%I:%M:%S")
	                    archivo.limpiar()
	                    print " -------------------------------------------------------------------------------"
	                    print " =========================|   LLAMAR A UN CONTACTO   |=========================="
	                    print " -------------------------------------------------------------------------------"
	                    print "\n Duracion de la llamada: " + str(duracion) + "s"
	                    print "\n 'Llamada finalizada'"

	                    self.llamadas.append(numero + "\t" + horaDeLlamada + '\t'+ finDeLallamada + '\t' + fechaDeLlamada)
	                    archivo.agregarAlHistorialDellamadas()
	                    archivo.escribirArchivoLlamadas()

	                    print "\n Desea volver a llamar?"
	                    SN = raw_input(" (s/n): ")

	                    if SN.lower() == 's':
		                	volverALlamar = True

	                    else:
		                	volverALlamar = False


archivo = archivo()
archivo.crearArchivo()
archivo.cargarArchivo()

archivo.crearArchivoMensajes()
archivo.cargarArchivoMensajes()

archivo.crearArchivoLlamadas()
archivo.cargarArchivoLlamadas()


menu = True

while menu == True:

    archivo.escribirArchivo()
    
    archivo.limpiar()

    print " -------------------------------------------------------------------------------"
    print " ==============================|     AGENDA     |==============================="
    print " -------------------------------------------------------------------------------"
    print " |       (1) AGREGAR CONTACTO           |        (2) MOSTRAR CONTACTOS         |"
    print " -------------------------------------------------------------------------------"
    print " |       (3) BUSCAR CONTACTO            |        (4) ELIMINAR CONTACTOS        |"
    print " -------------------------------------------------------------------------------"
    print " |       (5) ENVIAR SMS                 |        (6) LLAMAR UN CONTACTO        |"
    print " -------------------------------------------------------------------------------"
    print " |       (7) HISTORIAL DE SMS           |        (8) HISTORIAL DE LLAMADAS     |"
    print " -------------------------------------------------------------------------------"
    print " |                             |   (0) SALIR    |                              |"
    print " -------------------------------------------------------------------------------"

    try:
        opcion = input("\n Opcion > ")
        
    except:
        print
        print "                               'Opcion invalida'"
        print "                         Presione ENTER para continuar"
        print
        raw_input()

    else:
	    if opcion == 0:
	        print "\n 'Ha salido de la agenda' \n"
	        break

	    elif opcion == 1:
	        archivo.limpiar()
	        print " -------------------------------------------------------------------------------"
	        print " ============================|   NUEVO CONTACTO   |============================="
	        print " -------------------------------------------------------------------------------"

	        agregarOtro = True
	        while agregarOtro == True:
	            archivo.crearContacto()

	            print
	            print " (a) Agregar otro contacto"
	            print " (v) Volver al menu principal"
	            print " (s) Salir de la agenda"

	            elegir = raw_input("\n Opcion > ")

	            if elegir == 'v':
	                agregarOtro = False
	                menu = True
	                archivo.limpiar()

	            elif elegir == 's':
	                print "\n 'Ha salido de la agenda' \n"
	                agregarOtro = False
	                menu = False

	            elif elegir == 'a':
	                agregarOtro = True
	                menu = True
	                archivo.limpiar()

	            else:
	            	break

	    elif opcion == 2:
	        archivo.limpiar()
	        print "\n |      Nombre      |     Apellido      |    Telefono    |        Correo       |"
	        print " -------------------------------------------------------------------------------"

	        archivo.mostrarContacto()

	        print
	        print " (v) Volver al menu principal"
	        print " (s) Salir de la agenda"

	        elegir = raw_input("\n Opcion > ")

	        if elegir == 'v':
	            menu = True
	            archivo.limpiar()

	        if elegir == 's':
	            print "\n 'Ha salido de la agenda' \n"
	            menu = False

	    elif opcion == 3:

	        elegir = True
	        while elegir == True:
	            archivo.limpiar()
	            print " -------------------------------------------------------------------------------"
	            print " ==============================|     BUSCAR     |==============================="
	            print " -------------------------------------------------------------------------------"
	            print " |       [A] Buscar por nombre          |        [B] Buscar por numero         |"
	            print " -------------------------------------------------------------------------------"
	            print
	            print " (v) Volver al menu principal"
	            print " (s) Salir de la agenda"

	            elegir = raw_input("\n Opcion > ")

	            if elegir == 'a' or elegir == 'A':
	                
	                archivo.buscarContactoNombre()
	                archivo.escribirArchivo()

	                print
	                print " (b) Volver al menu buscar"
	                print " (v) Volver al menu principal"
	                print " (s) Salir de la agenda"
	                elegir = raw_input("\n Opcion > ")

	                if elegir == 'v':
	                    elegir = False
	                    menu = True
	                    archivo.limpiar()

	                elif elegir == 's':
	                    print "\n 'Ha salido de la agenda' \n"
	                    elegir = False
	                    menu = False

	                elif elegir == 'b':
	                	elegir = True
	                	archivo.limpiar()

	                else:
	                	break

	            if elegir == 'b' or elegir == 'B':
	                
	                archivo.buscarContactoNumero()
	                archivo.escribirArchivo()

	                print
	                print " (b) Volver al menu buscar"
	                print " (v) Volver al menu principal"
	                print " (s) Salir de la agenda"
	                elegir = raw_input("\n Opcion > ")

	                if elegir == 'v':
	                    elegir = False
	                    menu = True
	                    archivo.limpiar()

	                elif elegir == 's':
	                    print "\n 'Ha salido de la agenda' \n"
	                    elegir = False
	                    menu = False

	                elif elegir == 'b':
	                	elegir = True
	                	archivo.limpiar()

	                else:
	                	break

	            if elegir == 'v':
	                elegir = False
	                menu = True
	                archivo.limpiar()

	            if elegir == 's':
	                print "\n 'Ha salido de la agenda' \n"
	                elegir = False
	                menu = False

	    elif opcion == 4:
	        archivo.limpiar()
	        print " -------------------------------------------------------------------------------"
	        print " ====================|     ELIMINAR TODOS LOS CONTACTOS     |==================="
	        print " -------------------------------------------------------------------------------"

	        archivo.eliminarCONTACTOS()

	        print
	        print " (v) Volver al menu principal"
	        print " (s) Salir de la agenda"

	        elegir = raw_input("\n Opcion > ")

	        if elegir == 'v':
	            menu = True
	            archivo.limpiar()

	        if elegir == 's':
	            print "\n 'Ha salido de la agenda' \n"
	            menu = False

	    elif opcion == 5:
	        elegir = True

	        while elegir == True:
	        	archivo.limpiar()
	        	archivo.enviarSMS()

	        	print
	        	print " (e) Enviar otro mensaje"
	        	print " (v) Volver al menu principal"
	        	print " (s) Salir de la agenda"

	        	elegir = raw_input("\n Opcion > ")

	        	if elegir == 'v':
	        		elegir = False
	        		menu = True
	        		archivo.limpiar()

	        	if elegir == 's':
	        		print "\n 'Ha salido de la agenda' \n"
	        		elegir = False
	        		menu = False

	        	if elegir == 'e':
	        		elegir = True
	        		archivo.limpiar()

	    elif opcion == 6:
	        elegir = True

	        while elegir == True:
	        	archivo.limpiar()
	        	archivo.llamarAUnContacto()

	        	print
	        	print " (l) Llamar a otro contacto"
	        	print " (v) Volver al menu principal"
	        	print " (s) Salir de la agenda"

	        	elegir = raw_input("\n Opcion > ")

	        	if elegir == 'v':
	        		elegir = False
	        		menu = True
	        		archivo.limpiar()

	        	if elegir == 's':
	        		print "\n 'Ha salido de la agenda' \n"
	        		elegir = False
	        		menu = False

	        	if elegir == 'l':
	        		elegir = True
	        		archivo.limpiar()

	    elif opcion == 7:
	    	archivo.limpiar()

	    	elegir = True

	    	archivo.historialMensajes()

	        while elegir == True:
	            print
	            print " (e) Eliminar historial de mensajes"
	            print " (v) Volver al menu principal"
	            print " (s) Salir de la agenda"

	            elegir = raw_input("\n Opcion > ")

	            if elegir == 'e':
	            	archivo.limpiar()
	            	archivo.eliminarMensajes()
	            	elegir = True

	            if elegir == 'v':
	                elegir = False
	                menu = True
	                archivo.limpiar()

	            if elegir == 's':
	                print "\n 'Ha salido de la agenda' \n"
	                elegir = False
	                menu = False

	    elif opcion == 8:
	        archivo.limpiar()
	        elegir = True

	        while elegir == True:
	            print
	            print " (v) Volver al menu principal"
	            print " (s) Salir de la agenda"

	            elegir = raw_input("\n Opcion > ")

	            if elegir == 'v':
	                elegir = False
	                menu = True
	                archivo.limpiar()

	            if elegir == 's':
	                print "\n 'Ha salido de la agenda' \n"
	                elegir = False
	                menu = False

	    else:
	    	print
	        print "                               'Opcion invalida'"
	        print "                         Presione ENTER para continuar"
	        print
	        raw_input()
