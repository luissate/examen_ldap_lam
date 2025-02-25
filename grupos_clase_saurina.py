def generar_ldif(grupos):
    with open('oueso1tuapellido.ldif', 'w') as archivo:
        for grupo in grupos:
            archivo.write(f"dn: ou={grupo},dc=tuapellido,dc=org\n")
            archivo.write("objectClass: organizationalUnit\n")
            archivo.write(f"ou: {grupo}\n\n")

# Lista de unidades organizativas
grupos = ["1ESOA", "1ESOB", "1ESOC", "1ESOD"]

# Llamar a la función
generar_ldif(grupos)
