import tkinter as tk
import os
import random
import time
from PIL import Image, ImageTk

def agregar_caracter_posicion(cadena_modificar, caracter_a_agregar, posicion_cadena):
    # Agregar el caracter en la posición indicada
    cadena_modificar = cadena_modificar[:posicion_cadena] + "{" + caracter_a_agregar  + "}" + cadena_modificar[posicion_cadena:] + " + "
    return cadena_modificar

def siguiente_paso(estado_presente, cinta, posicion_cabeza):
    validacion_cadena = ''
    if (estado_presente, cinta[posicion_cabeza]) not in funciones_transicion:  # No hay una transicion para el estado presente y el simbolo leido en la cinta
        validacion_cadena = 'False'
    else:
        
        cinta_sin_espacios = cinta.strip()
        with open('salida.txt', 'a') as archivo:
            archivo.write(agregar_caracter_posicion(cinta_sin_espacios, estado_presente, posicion_cabeza))
        informacion_transicion = funciones_transicion[(estado_presente, cinta[posicion_cabeza])]
        estado_presente = informacion_transicion[0] # Actualiza el estado presente
        cinta_lista = list(cinta) # Convierto str a un objeto mutable list
        cinta_lista[posicion_cabeza] = informacion_transicion[1] # Escribe el carcater en la posicion de la cabeza 
        cinta = ''.join(cinta_lista) # convierto la lista a str nuevamente
        movimiento_cinta = informacion_transicion[2]
        
        if movimiento_cinta == 'r': # Se mueve la cabeza
            posicion_cabeza += 1
        else:
            posicion_cabeza -= 1
    return estado_presente, cinta, posicion_cabeza, validacion_cadena
    

def validar_cadena(cinta, ventana_anterior):
    cinta_sin_espacios = cinta
    ventana_anterior.withdraw() # Oculta la ventana anterior
    ventana_animacion = tk.Toplevel()  # Crea una nueva ventana
    ventana_animacion.title("Animación")

    estado_presente = 'q0' # Se establece el estado presente como el estado incial 'q0'
    posicion_cabeza = 0

    if len(cinta_sin_espacios) > 16:
        etiqueta_mensaje = tk.Label(ventana_animacion, text="No se puede animar, porque la cadena es mayor a 16 caracteres\n La salida del programa se encuentra en el archivo 'salida_programa'", font=("Arial", 16))
        etiqueta_mensaje.grid(row=0, column=0, columnspan=20)
    else:
        # Acompleta la cinta con espacios en blanco hasta que la cinta tenga 1006 caracteres en total
        cinta = cinta.ljust(1006)

        etiqueta_cinta = tk.Label(ventana_animacion, text="Cinta", font=("Arial", 16))
        etiqueta_cinta.grid(row=1, column=7, columnspan=2)

        # Crear canvas para la cinta
        cinta1 = tk.Canvas(ventana_animacion, width=30, height=30, borderwidth=2, relief="solid")
        cinta1.grid(row=2, column=0)
        cinta2 = tk.Canvas(ventana_animacion, width=30, height=30, borderwidth=2, relief="solid")
        cinta2.grid(row=2, column=1)
        cinta3 = tk.Canvas(ventana_animacion, width=30, height=30, borderwidth=2, relief="solid")
        cinta3.grid(row=2, column=2)
        cinta4 = tk.Canvas(ventana_animacion, width=30, height=30, borderwidth=2, relief="solid")
        cinta4.grid(row=2, column=3)
        cinta5 = tk.Canvas(ventana_animacion, width=30, height=30, borderwidth=2, relief="solid")
        cinta5.grid(row=2, column=4)
        cinta6 = tk.Canvas(ventana_animacion, width=30, height=30, borderwidth=2, relief="solid")
        cinta6.grid(row=2, column=5)
        cinta7 = tk.Canvas(ventana_animacion, width=30, height=30, borderwidth=2, relief="solid")
        cinta7.grid(row=2, column=6)
        cinta8 = tk.Canvas(ventana_animacion, width=30, height=30, borderwidth=2, relief="solid")
        cinta8.grid(row=2, column=7)
        cinta9 = tk.Canvas(ventana_animacion, width=30, height=30, borderwidth=2, relief="solid")
        cinta9.grid(row=2, column=8)
        cinta10 = tk.Canvas(ventana_animacion, width=30, height=30, borderwidth=2, relief="solid")
        cinta10.grid(row=2, column=9)
        cinta11 = tk.Canvas(ventana_animacion, width=30, height=30, borderwidth=2, relief="solid")
        cinta11.grid(row=2, column=10)
        cinta12 = tk.Canvas(ventana_animacion, width=30, height=30, borderwidth=2, relief="solid")
        cinta12.grid(row=2, column=11)
        cinta13 = tk.Canvas(ventana_animacion, width=30, height=30, borderwidth=2, relief="solid")
        cinta13.grid(row=2, column=12)
        cinta14 = tk.Canvas(ventana_animacion, width=30, height=30, borderwidth=2, relief="solid")
        cinta14.grid(row=2, column=13)
        cinta15 = tk.Canvas(ventana_animacion, width=30, height=30, borderwidth=2, relief="solid")
        cinta15.grid(row=2, column=14)
        cinta16 = tk.Canvas(ventana_animacion, width=30, height=30, borderwidth=2, relief="solid")
        cinta16.grid(row=2, column=15)

        # Agregar el texto de la cinta al canvas
        texto_cinta1 = cinta1.create_text(19, 19, text=cinta[0], font=("Arial", 12), fill="black")
        texto_cinta2 = cinta2.create_text(19, 19, text=cinta[1], font=("Arial", 12), fill="black")
        texto_cinta3 = cinta3.create_text(19, 19, text=cinta[2], font=("Arial", 12), fill="black")
        texto_cinta4 = cinta4.create_text(19, 19, text=cinta[3], font=("Arial", 12), fill="black")
        texto_cinta5 = cinta5.create_text(19, 19, text=cinta[4], font=("Arial", 12), fill="black")
        texto_cinta6 = cinta6.create_text(19, 19, text=cinta[5], font=("Arial", 12), fill="black")
        texto_cinta7 = cinta7.create_text(19, 19, text=cinta[6], font=("Arial", 12), fill="black")
        texto_cinta8 = cinta8.create_text(19, 19, text=cinta[7], font=("Arial", 12), fill="black")
        texto_cinta9 = cinta9.create_text(19, 19, text=cinta[8], font=("Arial", 12), fill="black")
        texto_cinta10 = cinta10.create_text(19, 19, text=cinta[9], font=("Arial", 12), fill="black")
        texto_cinta11 = cinta11.create_text(19, 19, text=cinta[10], font=("Arial", 12), fill="black")
        texto_cinta12 = cinta12.create_text(19, 19, text=cinta[11], font=("Arial", 12), fill="black")
        texto_cinta13 = cinta13.create_text(19, 19, text=cinta[12], font=("Arial", 12), fill="black")
        texto_cinta14 = cinta14.create_text(19, 19, text=cinta[13], font=("Arial", 12), fill="black")
        texto_cinta15 = cinta15.create_text(19, 19, text=cinta[14], font=("Arial", 12), fill="black")
        texto_cinta16 = cinta16.create_text(19, 19, text=cinta[15], font=("Arial", 12), fill="black")

        # Cargar la imagen de la flecha hacia arriba
        imagen_flecha = Image.open("flecha_arriba.png")  
        imagen_flecha = imagen_flecha.resize((30, 30))  
        imagen_flecha = ImageTk.PhotoImage(imagen_flecha) 

        eflecha = tk.Label(ventana_animacion, image=imagen_flecha)
        eflecha.image = imagen_flecha  # Evitar que la imagen sea eliminada por la recolección de basura
        eflecha.grid(row=3, column=0)

        etiqueta_estado_presente = tk.Label(ventana_animacion, text=f"Estado presente: {estado_presente}", font=("Arial", 16))
        etiqueta_estado_presente.grid(row=4, column=5, columnspan=6)

        etiqueta_estado_final = tk.Label(ventana_animacion, text="Estado final: q4", font=("Arial", 16))
        etiqueta_estado_final.grid(row=5, column=5, columnspan=6)

        string_funciones_transicion = str(funciones_transicion)
        aux_recortar = string_funciones_transicion[:31] + '\n'
        funciones_transicion_lineas = aux_recortar
        # Siguiente transicion 
        aux_recortar = string_funciones_transicion[31:]
        aux_recortar = aux_recortar[:31] + '\n'
        funciones_transicion_lineas = funciones_transicion_lineas + aux_recortar
        # Siguiente transicion 
        aux_recortar = string_funciones_transicion[62:]
        aux_recortar = aux_recortar[:31] + '\n'
        funciones_transicion_lineas = funciones_transicion_lineas + aux_recortar
        # Siguiente transicion 
        aux_recortar = string_funciones_transicion[93:]
        aux_recortar = aux_recortar[:31] + '\n'
        funciones_transicion_lineas = funciones_transicion_lineas + aux_recortar
        # Siguiente transicion 
        aux_recortar = string_funciones_transicion[124:]
        aux_recortar = aux_recortar[:31] + '\n'
        funciones_transicion_lineas = funciones_transicion_lineas + aux_recortar
        # Siguiente transicion 
        aux_recortar = string_funciones_transicion[155:]
        aux_recortar = aux_recortar[:31] + '\n'
        funciones_transicion_lineas = funciones_transicion_lineas + aux_recortar
        # Siguiente transicion 
        aux_recortar = string_funciones_transicion[186:]
        aux_recortar = aux_recortar[:31] + '\n'
        funciones_transicion_lineas = funciones_transicion_lineas + aux_recortar
        # Siguiente transicion 
        aux_recortar = string_funciones_transicion[217:]
        aux_recortar = aux_recortar[:31] + '\n'
        funciones_transicion_lineas = funciones_transicion_lineas + aux_recortar
        # Siguiente transicion 
        aux_recortar = string_funciones_transicion[248:]
        aux_recortar = aux_recortar[:31] + '\n'
        funciones_transicion_lineas = funciones_transicion_lineas + aux_recortar
        # Siguiente transicion 
        aux_recortar = string_funciones_transicion[279:]
        aux_recortar = aux_recortar[:31] + '\n'
        funciones_transicion_lineas = funciones_transicion_lineas + aux_recortar

        etiqueta_funciones_transicion = tk.Label(ventana_animacion, text=f"Funciones transicion: \n{funciones_transicion_lineas}", font=("Arial", 16))
        etiqueta_funciones_transicion.grid(row=6, column=5, columnspan=6)

    while estado_presente != 'q4' and cinta[posicion_cabeza] != ' ':
        estado_presente, cinta, posicion_cabeza, validacion_cadena = siguiente_paso(estado_presente, cinta, posicion_cabeza) # Ejecuto un paso en la maquina de Turing
        if validacion_cadena == 'False':
            break
        if len(cinta_sin_espacios) > 16:
            etiqueta_mensaje = tk.Label(ventana_animacion, text="No se puede animar, porque la cadena es mayor a 16 caracteres\n La salida del programa se encuentra en el archivo 'salida_programa'", font=("Arial", 16))
            etiqueta_mensaje.grid(row=0, column=0, columnspan=20)
        else:
            # Actualizar la animacion
            ventana_animacion.update()
            if len(cinta_sin_espacios) < 16:
                time.sleep(velocidad_animacion)
            cinta1.itemconfig(texto_cinta1, text=cinta[0])
            cinta2.itemconfig(texto_cinta1, text=cinta[1])
            cinta3.itemconfig(texto_cinta1, text=cinta[2])
            cinta4.itemconfig(texto_cinta1, text=cinta[3])
            cinta5.itemconfig(texto_cinta1, text=cinta[4])
            cinta6.itemconfig(texto_cinta1, text=cinta[5])
            cinta7.itemconfig(texto_cinta1, text=cinta[6])
            cinta8.itemconfig(texto_cinta1, text=cinta[7])
            cinta9.itemconfig(texto_cinta1, text=cinta[8])
            cinta10.itemconfig(texto_cinta1, text=cinta[9])
            cinta11.itemconfig(texto_cinta1, text=cinta[10])
            cinta12.itemconfig(texto_cinta1, text=cinta[11])
            cinta13.itemconfig(texto_cinta1, text=cinta[12])
            cinta14.itemconfig(texto_cinta1, text=cinta[13])
            cinta15.itemconfig(texto_cinta1, text=cinta[14])
            cinta16.itemconfig(texto_cinta1, text=cinta[15])
            etiqueta_estado_presente.config(text=f'Estado presente: {estado_presente}')
            eflecha.grid(row=3, column=posicion_cabeza)

    estado_presente, cinta, posicion_cabeza, validacion_cadena = siguiente_paso(estado_presente, cinta, posicion_cabeza) # Ejecuto un paso en la maquina de Turing
    cinta_aux_sin_espacios = cinta.strip()
    cinta_aux_sin_espacios = agregar_caracter_posicion(cinta_aux_sin_espacios, estado_presente, posicion_cabeza)
    cinta_aux_sin_espacios = cinta_aux_sin_espacios[:len(cinta_aux_sin_espacios) - 3]

    if estado_presente == 'q4' and cinta[posicion_cabeza] == ' ':
        validacion_cadena = 'True'
    if validacion_cadena == 'False':
        if len(cinta_sin_espacios) > 16:
            etiqueta_mensaje = tk.Label(ventana_animacion, text="No se puede animar, porque la cadena es mayor a 16 caracteres\n La salida del programa se encuentra en el archivo 'salida_programa'", font=("Arial", 16))
            etiqueta_mensaje.grid(row=0, column=0, columnspan=20)
        else:
            etiqueta_aceptacion = tk.Label(ventana_animacion, text="La cadena no pertenece al lenguaje {0^n1^n | n>= 1}", font=("Arial", 16), foreground="red")
            etiqueta_aceptacion.grid(row=7, column=1, columnspan=13)
    elif validacion_cadena == 'True':
        if len(cinta_sin_espacios) > 16:
            etiqueta_mensaje = tk.Label(ventana_animacion, text="No se puede animar, porque la cadena es mayor a 16 caracteres\n La salida del programa se encuentra en el archivo 'salida_programa'", font=("Arial", 16))
            etiqueta_mensaje.grid(row=0, column=0, columnspan=20)
        else:
            etiqueta_aceptacion = tk.Label(ventana_animacion, text="La cadena pertenece al lenguaje {0^n1^n | n>= 1}", font=("Arial", 16), foreground="green")
            etiqueta_aceptacion.grid(row=7, column=1, columnspan=13)

    with open('salida.txt', 'a') as archivo:
        archivo.write(cinta_aux_sin_espacios)
        if validacion_cadena == 'True':
            archivo.write(f'\n\nLa cadena es reconocida por la máquina de Turing')
        if validacion_cadena == 'False':
            archivo.write(f'\n\nLa cadena no es reconocida por la máquina de Turing')

    if len(cinta_sin_espacios) > 16:
        etiqueta_mensaje = tk.Label(ventana_animacion, text="No se puede animar, porque la cadena es mayor a 16 caracteres\n La salida del programa se encuentra en el archivo 'salida_programa'", font=("Arial", 16))
        etiqueta_mensaje.grid(row=0, column=0, columnspan=20)
    else:
        # Actualizar la animacion
        ventana_animacion.update()
        if len(cinta_sin_espacios) < 16:
            time.sleep(velocidad_animacion)
        cinta1.itemconfig(texto_cinta1, text=cinta[0])
        cinta2.itemconfig(texto_cinta1, text=cinta[1])
        cinta3.itemconfig(texto_cinta1, text=cinta[2])
        cinta4.itemconfig(texto_cinta1, text=cinta[3])
        cinta5.itemconfig(texto_cinta1, text=cinta[4])
        cinta6.itemconfig(texto_cinta1, text=cinta[5])
        cinta7.itemconfig(texto_cinta1, text=cinta[6])
        cinta8.itemconfig(texto_cinta1, text=cinta[7])
        cinta9.itemconfig(texto_cinta1, text=cinta[8])
        cinta10.itemconfig(texto_cinta1, text=cinta[9])
        cinta11.itemconfig(texto_cinta1, text=cinta[10])
        cinta12.itemconfig(texto_cinta1, text=cinta[11])
        cinta13.itemconfig(texto_cinta1, text=cinta[12])
        cinta14.itemconfig(texto_cinta1, text=cinta[13])
        cinta15.itemconfig(texto_cinta1, text=cinta[14])
        cinta16.itemconfig(texto_cinta1, text=cinta[15])
        etiqueta_estado_presente.config(text=f'Estado presente: {estado_presente}')
        eflecha.grid(row=3, column=posicion_cabeza)

    ventana_animacion.protocol("WM_DELETE_WINDOW", lambda: [ventana.destroy()])

def mostrar_ventana_ingresar_cadena():
    ventana.withdraw()  # Oculta la ventana principal
    ventana_cadena = tk.Toplevel()  # Crea una nueva ventana
    ventana_cadena.title("Ingresar cadena")
    
    etiqueta_cadena = tk.Label(ventana_cadena, text="Ingrese la cadena", font=("Arial", 16))
    etiqueta_cadena.pack(padx=20, pady=20)

    cinta = tk.Entry(ventana_cadena, font=("Arial", 12))
    cinta.pack(pady=10)

    boton_validar = tk.Button(ventana_cadena, text="Validar", width=20, height=2,
                              bg="#CAFFBF", font=("Arial", 12),
                              command=lambda: validar_cadena(cinta.get(), ventana_cadena))
    boton_validar.pack(pady=10)

    ventana_cadena.protocol("WM_DELETE_WINDOW", lambda: [ventana.destroy()])

def generar_cadena_binaria_aleatoria():
    longitud = random.randint(1, 1000)
    cadena_binaria = ''.join(random.choice('01') for _ in range(longitud))
    return cadena_binaria

with open('salida.txt', 'w') as archivo:
            archivo.write('Instantaneas\n')

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Automata Pila")

# Contenedor principal
contenedor_principal = tk.Frame(ventana)
contenedor_principal.grid(column=0, row=0, padx=(50,50), pady=(10,10))

# Etiqueta de inicio
etiqueta = tk.Label(contenedor_principal, text="Validar con la máquina de Turing si el input pertenece al lenguaje {0^n 1^n | n >= 1}", font=("Arial", 16))
etiqueta.grid(row=1, column=0, columnspan=2)

boton_ingresar_cadena = tk.Button(contenedor_principal, text="Ingresar cadena", width=20, height=5,\
    bg="#CAFFBF", font=("Arial", 12), command=mostrar_ventana_ingresar_cadena)
boton_ingresar_cadena.grid(row=3, column=0)



boton_cadena_aleatoria = tk.Button(contenedor_principal, text="Cadena aleatoria", width=20, height=5,\
    bg="#CAFFBF", font=("Arial", 12), command=lambda: validar_cadena(generar_cadena_binaria_aleatoria(), ventana))
boton_cadena_aleatoria.grid(row=3, column=1)

velocidad_animacion = 1

# Estructura de funciones_transicion
# ('estado_presente', 'simbolo_leido'): ('estado_siguiente', 'simbolo_a_escribir', 'direcicion_mover_cabeza')
#                                                                                       r=rigth, l=left 
funciones_transicion = {
    ('q0', '0'): ('q1', 'x', 'r'),
    ('q0', 'y'): ('q3', 'y', 'r'),
    ('q1', '0'): ('q1', '0', 'r'),
    ('q1', 'y'): ('q1', 'y', 'r'),
    ('q1', '1'): ('q2', 'y', 'l'),
    ('q2', '0'): ('q2', '0', 'l'),
    ('q2', 'y'): ('q2', 'y', 'l'),
    ('q2', 'x'): ('q0', 'x', 'r'),
    ('q3', 'y'): ('q3', 'y', 'r'),
    ('q3', ' '): ('q4', ' ', 'r')
}

# Iniciar el bucle de eventos
ventana.mainloop()