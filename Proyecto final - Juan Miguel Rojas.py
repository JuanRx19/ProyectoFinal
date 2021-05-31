import json

#Se hace la lectura del archivo donde se encuentran los usuarios con vehiculo registrado.
Load = open("usuarios.json", "r", encoding="utf-8")
usuarios = json.load(Load)

#Se hace la lectura del archivo donde se encuentra la información acerca del parqueadero
Load2 = open("tiposParqueaderos.json", "r", encoding="utf-8")
tiposParqueaderos = json.load(Load2)

#Se hace la lectura y luego se modificara la ocupación del parqueadero
Load3 = open("ocupacionParqueaderos.json", "r", encoding="utf-8")
ocupacionParqueaderos = json.load(Load3)

#user es la variable en la cual guardo todo los usuarios con su informacion(nombre, identificación, tipo de usuario, etc...)
user = usuarios["usuarios"]

#parqueadero1 es la variable en la cual guardo mi segundo archivo de parqueadero el cual se modificara.
parqueadero1 = ocupacionParqueaderos

#parqueadero2 es la variable en la cual tendremos nuestro parqueadero original, donde al retirar los vehiculos se reemplazara el puesto dado.
parqueadero2 = tiposParqueaderos

n = 0
par = list(parqueadero1.keys())
dude = 0

#Función que me permite registrar nuevos usuarios
def regV(usuarios, user, nom, id):
    n = 0
    for i in range(len(user)):
        if (user[i][1] == id):
            n+=1
    if(n == 1):
        print("El usuario ya ha registrado un vehiculo.")
    else:
        tu = input("1. Estudiante\n2. Profesor\n3. Personal Administrativo\nPor favor ingrese que tipo de usuario es: ")
        if(tu == "1"):
            tu = "Estudiante"
        elif(tu == "2"):
            tu = "Profesor"
        elif(tu == "3"):
            tu = "Personal Administrativo"
        placa = input("Por favor ingrese la placa del vehiculo: ")
        tv = input("1. Automóvil\n2. Automóvil eléctrico\n3. Motocicleta\n4. Discapacitado\nPor favor ingrese que tipo de vehiculo es: ")
        if(tv == "1"):
            tv = "Automóvil"
        elif(tv == "2"):
            tv = "Automóvil Eléctrico"
        elif(tv == "3"):
            tv = "Motocicleta"
        elif(tv == "4"):
            tv = "Discapacitado"
        pp = input("1. Mensualidad\n2. Diario\nPor favor ingrese que plan de pago tendrá: ")
        if(pp == "1"):
            pp = "Mensualidad"
        elif(pp == "2"):
            pp = "Diario"
        user.append([nom, id, tu, placa, tv, pp])
        usuarios["usuarios"] = user
    return usuarios

#Funcion la cual me permite hacer el parqueadero.
def parQ(parqueadero1, parqueadero, n1, n2):
    c = 1
    pro = ""
    for p in range(len(parqueadero[0])):
        pro+= " " + str(c) + " "
        c+=1
    print(pro)
    c = 1
    for x in range(len(parqueadero)):
        print(str(c), end="")
        c+=1
        for y in range(len(parqueadero[0])):
            if(parqueadero[x][y] == n1 or parqueadero[x][y] == n2):
                print(" 0 ", end="")
            else:
                print(" X ", end="")
        print("\n")
    col = int(input("Por favor ingrese el numero de la columna a parquear: "))
    fil = int(input("Por favor ingrese el numero de la fila a parquear: "))
    col = col - 1
    fil = fil - 1
    if(parqueadero[fil][col] == n1 or parqueadero[fil][col] == n2):
        parqueadero[fil][col] = placa
        parqueadero1[piso] = parqueadero
        with open("ocupacionParqueaderos.json", "w", encoding= "utf-8") as file:
            json.dump(parqueadero1, file, indent=1, ensure_ascii = False)
        print("¡El vehiculo se parqueado correctamente!")
    else:
        print("Este lugar se encuentra ocupado o no disponible, por favor vuelva a intentarlo.")
    return parqueadero1

#Menú de opciones para el parqueardero.
opc = int(input("1. Ingreso de vehiculo\n2. Registro de vehiculo\n3. Retirar vehiculo\n4. Salir\nPor favor digite la opción que desea utilizar: "))
while(opc != 4):
    #Opción para el ingreso de vehiculos
    if(opc == 1):
        n = 0
        placa = input("Por favor ingrese la placa del vehiculo: ")
        for i in range(len(user)):
            if(user[i][3] == placa):
                ingreso = user[i][0]
                tp = user[i][4]
                n+=1
        for p in par:
            for i in range(len(parqueadero1[p])):
                for y in range(len(parqueadero1[p][0])):
                    if(parqueadero1[p][i][y] == placa):
                        dude+=1
        if(dude == 1):
            print("El vehiculo con la placa " + str(placa) + " ya ha sido ingresada en el parqueadero.")
        else:
            if(n == 1):
                print("Bienvenido señor(a) " + str(ingreso) + ", por favor ingrese en que lugar desea parquear.")
            else:
                print("Tu placa no se encuentra registrada, por lo tanto seras tomado como visitante.")
                tp = input("1. Automóvil\n2. Automóvil eléctrico\n3. Motocicleta\n4. Discapacitado\nPor favor ingrese que tipo de vehiculo es: ")
                if(tp == "1"):
                    tp = "Automóvil"
                elif(tp == "2"):
                    tp = "Automóvil Eléctrico"
                elif(tp == "3"):
                    tp = "Motocicleta"
                elif(tp == "4"):
                    tp = "Discapacitado"
            piso = input("1. Piso 1\n2. Piso 2\n3. Piso 3\n4. Piso 4\n5. Piso 5\n6. Piso 6\nPor favor seleccione el piso que desea parquear: ")
            if(piso == "1"):
                piso = "Piso1"
            elif(piso == "2"):
                piso = "Piso2"
            elif(piso == "3"):
                piso = "Piso3"
            elif(piso == "4"):
                piso = "Piso4"
            elif(piso == "5"):
                piso = "Piso5"
            elif(piso == "6"):
                piso = "Piso6"
            parqueadero = parqueadero1[piso]
            n1 = 0
            n2 = 0
            if(tp == "Automóvil"):
                n1 = 1
                n2 = 0
                parqueadero1 = parQ(parqueadero1, parqueadero, n1, n2)
            elif(tp == "Automóvil Eléctrico"):
                n1 = 1
                n2 = 2
                parqueadero1 = parQ(parqueadero1, parqueadero, n1, n2)
            elif(tp == "Motocicleta"):
                n1 = 3
                parqueadero1 = parQ(parqueadero1, parqueadero, n1, n2)
            elif(tp == "Discapacitado"):
                n1 = 1
                n2 = 4
                parqueadero1 = parQ(parqueadero1, parqueadero, n1, n2)
        
    #Opción para el registro de vehiculos  
    if(opc == 2):
        n = 0
        nom = input("Por favor ingrese su nombre: ")
        id = int(input("Por favor ingrese su identificación: "))
        #Llamado a la función para crear usuarios
        usuarios = regV(usuarios, user, nom, id)
        with open("usuarios.json", "w", encoding = "utf-8") as file:
            json.dump(usuarios, file, indent=4, ensure_ascii = False)

    #Opción para retirar vehiculos
    if(opc == 3):
        tdp = ""
        l = 0
        n = 0
        nac = 0
        placa = input("Por favor ingrese la placa del vehiculo a retirar: ")
        canh = int(input("Por favor digite la cantidad de horas que permanecio el vehiculo en el parqueadero: "))
        for p in par:
            for i in range(len(parqueadero1[p])):
                for y in range(len(parqueadero1[p][0])):
                    if(str(parqueadero1[p][i][y]) == placa):
                        parqueadero1[p][i][y] = parqueadero2[p][i][y]
                        nac+=1
        if(nac == 1):
            for i in range(len(user)):
                if(user[i][3] == placa):
                    vp = user[i][2]
                    tdp = user[i][5]
                    n+=1
            if(n == 1 and tdp == "Diario"):
                if(vp == "Estudiante"):
                    total = canh * 1000
                    print("Como Estudiante tendras el cobro de: $" + str(total))
                elif(vp == "Profesor"):
                    total = canh * 2000
                    print("Como Profesor tendras el cobro de: $" + str(total))
                elif(vp == "Personal Administrativo"):
                    total = canh * 1500
                    print("Como Personal Administrativo tendras el cobro de: $" + str(total))
            else:
                if(tdp == "Mensualidad"):
                    print("Usted tiene mensualidad, por lo tanto no necesita de cobro, puede salir.")
                else:
                    total = canh * 3000
                    print("Como visitante tendras el cobro de: $" + str(total))
        else:
            print("¡La placa no ha sido registrada en ningun momento!\nAsegurate de que hayas digitado la correcta.")
        with open("ocupacionParqueaderos.json", "w", encoding = "utf-8") as file:
            json.dump(parqueadero1, file, indent=1, ensure_ascii = False)

    opc = int(input("1. Ingreso de vehiculo\n2. Registro de usuario\n3. Retirar vehiculo\n4. Salir\nPor favor digite la opción que desea utilizar: "))
print("El programa a finalizado correctamente.")
placaspar = []
#Aquí generamos el reporte final de ocupación, tipos de usuarios, etc...
og = 0
pis1 = 0
pis2 = 0
pis3 = 0
pis4 = 0
pis5 = 0
pis6 = 0
estu = 0
prof = 0
persa = 0
car = 0
care = 0
mot = 0
disc = 0
#Ciclos los cuales me permiten recorrer completamente el diccionario del parqueadero.
for p in par:
    for i in range(len(parqueadero1[p])):
        for y in range(len(parqueadero1[p][0])):
            if(parqueadero1[p][i][y] != 1 and parqueadero1[p][i][y] != 2 and parqueadero1[p][i][y] != 3 and parqueadero1[p][i][y] != 4):
                placaspar.append(parqueadero1[p][i][y])
                if(p == "Piso1"):
                    pis1+=1
                elif(p == "Piso2"):
                    pis2+=1
                elif(p == "Piso3"):
                    pis3+=1
                elif(p == "Piso4"):
                    pis4+=1
                elif(p == "Piso5"):
                    pis5+=1
                elif(p == "Piso6"):
                    pis6+=1
                og+=1
pis1 = (pis1/100)*100
pis2 = (pis2/100)*100
pis3 = (pis3/100)*100
pis4 = (pis4/100)*100
pis5 = (pis5/100)*100
pis6 = (pis6/50)*100
og = (og/550)*100

if(len(placaspar) >= 1):
    for i in range(len(user)):
        for j in range(len(placaspar)):
            if(user[i][3] == placaspar[j]):
                #Condicionales para evaluar tipo de usuario
                if(user[i][2] == "Estudiante"):
                    estu+=1
                elif(user[i][2] == "Profesor"):
                    prof+=1
                elif(user[i][2] == "Personal Administrativo"):
                    persa+=1
                #Condicionales para evaluar el tipo de vehiculo
                if(user[i][4] == "Automóvil"):
                    car+=1
                elif(user[i][4] == "Automóvil Eléctrico"):
                    care+=1
                elif(user[i][4] == "Motocicleta"):
                    mot+=1
                elif(user[i][4] == "Discapacitado"):
                    disc+=1

reporte = open("Reporte.txt", "w")
reporte.writelines("Vehículos estacionados según el tipo de usuario:\n")
reporte.writelines("Estudiantes: " + str(estu) + "\n")
reporte.writelines("Profesores: " + str(prof) + "\n")
reporte.writelines("Personal administrativo: " + str(persa) + "\n")
reporte.writelines("\n")
reporte.writelines("Vehículos estacionados según el tipo de vehiculo:\n")
reporte.writelines("Automóvil: " + str(car) + "\n")
reporte.writelines("Automóvil Eléctrico: " + str(care) + "\n")
reporte.writelines("Motocicleta: " + str(mot) + "\n")
reporte.writelines("Discapacitado: " + str(disc) + "\n")
reporte.writelines("\n")
reporte.writelines("Porcentaje de ocupación global: " + str(og) + "%\n")
reporte.writelines("Porcentaje de ocupación por pisos:\n")
reporte.writelines("Piso 1: " + str(pis1) + "%\n")
reporte.writelines("Piso 2: " + str(pis2) + "%\n")
reporte.writelines("Piso 3: " + str(pis3) + "%\n")
reporte.writelines("Piso 4: " + str(pis4) + "%\n")
reporte.writelines("Piso 5: " + str(pis5) + "%\n")
reporte.writelines("Piso 6: " + str(pis6) + "%\n")

#Finalización del programa.
Load.close()
Load2.close()
Load3.close()
reporte.close()