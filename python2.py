  GNU nano 7.2                     create_ou_saurina.py                               
ldif = f"""

dn: ou=alumnos,dc=saurina,dc=org
objectClass: organizationalUnit
ou: alumnos
"""

with open("ou_alumnos.ldif", "w") as f:
     f.write(ldif)
