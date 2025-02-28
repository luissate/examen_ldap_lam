ldif = ""
for i in range(1, 2001):
    ldif += f"""
dn: uid=alumno{i},ou=alumnos,dc=saurina,dc=org
objectClass: inetOrgPerson
uid: alumno{i}
sn: Apellido{i}
cn: Alumno{i}
userPassword: password{i}
"""

with open("alumnos.ldif", "w") as f:
    f.write(ldif)
