def generar_alumnos(clase, num_alumnos):
    # Crear y abrir el archivo LDIF
    with open('alumnos_tuapellido.ldif', 'w') as archivo:
        # Usar un bucle for para crear el número de alumnos especificado
        for i in range(1, num_alumnos + 1):
            archivo.write(f"dn: uid=alumno{i},ou={clase},dc=tuapellido,dc=org\n")
            archivo.write("objectClass: inetOrgPerson\n")
            archivo.write(f"uid: alumno{i}\n")
            archivo.write(f"cn: Alumno {i}\n")
            archivo.write(f"sn: Apellido{i}\n")
            archivo.write(f"mail: alumno{i}@tuapellido.org\n\n")

# Llamada a la función con los parámetros indicados en el examen
generar_alumnos("1ESOC", 20)
