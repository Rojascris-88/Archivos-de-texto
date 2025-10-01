# Crear un archivo y escribir líneas de notas personales
with open('my_notes.txt', 'w') as file:
    # En esta parte se escribe las 3 lineas de notas personales
    file.write('Nota 1: Mi nombre es Cristian Rojas.\n')
    file.write('Nota 2: Estudio en la Universidad Estatal Amazonica.\n')
    file.write('Nota 3: Carrera Tecnologias de la Información.\n')

# En esta parte se abre el archivo para leer línea por línea
with open('my_notes.txt', 'r') as file:
    # Leer cada línea y mostrarla en consola
    line = file.readline()  # Permite leer la primera línea
    while line:
        print(line.strip())  # Muestra la línea sin salto de línea extra
        line = file.readline()  # Permite leer siguiente línea