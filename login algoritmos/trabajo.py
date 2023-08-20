# Crear un array para almacenar los usuarios registrados
usuarios = []

# Crear un array para almacenar los roles disponibles
roles = ["administrador", "usuario"]

#BIEN, UNA VEZ CREADOS LOS ARRAYS, PASAMOS A CREAR UNA FUNCIÓN PARA REGISTRAR UN NUEVO USUARIO.
def registrar_usuario():
    
    # Pedir al usuario que ingrese sus datos
    nombre=input("Ingrese el Nombre del Usuario: ")
    apellido= input ("Ingrese Apellido: ")
    email=input("ingrese Email: ")
    password=input("Ingrese Password: ")
    rol = input("ingrese su rol(administrador o usuario): ")
   
    # Validar que el rol sea válido
    if rol not in roles:
        print("rol no válido. intente de nuevo")
        return 
    
    # Validamos también, que el correo no esté registrado.
    for usuario in usuarios:
        if usuario["email"]==email:
            print("email ya existe, ingrese uno diferente.")
            return
        
    #Creamos un diccionario con los datos del usuario.    
    usuario={"nombre":nombre,
            "apellido": apellido,
            "email":email, 
            "password":password,
            "rol": rol}
    
    #Agregamos el usuario al array de usuarios.
    usuarios.append(usuario)

    #Luego de registrarse, vamos a mostrar un mensaje de éxito
    print("\n Usuario Registrado con exito!.")

#CREAMOS UNA FUNCIÓN PARA INICIAR SESIÓN.
def iniciar_sesion ():

    #Pasamos a pedir al usuario que ingrese su correo y contraseña
    email = input("ingrese su email: ")
    password = input("ingrese su password: ")

    #Buscamos al usuario en el array de usuarios
    for usuario in usuarios:
        if usuario["email"]==email and usuario["password"]==password:
          
          #Mostramos un mensaje de bienvenida  
          print(f"bienvenido {usuario['nombre']} {usuario['apellido']} .tu rol es -> {usuario['rol']}.")

          #Retornamos al usuario encontrado
          return usuario
        
    #Si no se encuentra el usuario, mostrar un mensaje de error.
    print("email o password incorrectos. intente de nuevo")
    return None

#CREAMOS UNA FUNCIÓN PARA LISTAR LOS USUARIOS REGISTRADOS
def listar_usuarios():

    #Verificamos que haya usuarios registrados
    if len(usuarios) == 0:
        print("No hay Usuarios registrados. ")
        return
    
    #Mostrar los datos de cada usuario en una tabla
    print("lista de usuarios regitrados: ")
    print("-"*75)
    print(f"{'nombre':<20}{'apellido':<20} {'email':<20}{'rol':<20}")
    print("-"*75)
    for usuario in usuarios:
     print(f"{usuario['nombre']:<20}{usuario['apellido']:<20}{usuario['email']:<20}{usuario['rol']:<20}")
    print("-"*75)

#CREAR UNA FUNCIÓN PARA ORDENAR LOS USUARIOS POR NOMBRE O APELLIDO
def ordenar_usuarios():

    #Pedir al usuario que ingrese el criterio de ordenamiento (nombre o apellido)
    criterio = input("ingrese el criterio de orden (nombre o apellido): ")
    
    #Validar que el criterio sea válido

    if criterio not in ["nombre", "apellido"]:
        print ("criterio no válido. inténtelo de nuevo.")
        return
    
    #Pedir al usuario que ingrese el sentido de ordenamiento (ascendente o descendente)
    sentido = input("ingrese el sentido de ordenamiento(ascendente o descendente)")
    
    #Validar que el sentido sea válido.
    if sentido not in ["ascendente", "descendente"]:
        print("sentido no válido, intente nuevamente.")
        return
    
    #Ordenar el array de usuarios según el criterio y el sentido elegidos
    usuarios.sort(key=lambda x:x[criterio], reverse=(sentido=="descendente"))
    
    #Mostramos un mensaje de éxito
    print(f"usuarios ordenados por {criterio} en sentido {sentido}.")

#CREAR UNA FUNCIÓN PARA CREAR UN NUEVO ROL
def crear_rol():
    
    #Pedir al usuario que ingrese el nuevo rol
    nuevo_rol = input("ingrese el nombre del nuevo rol: ")
    
    #Validar que el rol no exista
    if nuevo_rol in roles:
        print("el rol agregado ya existe, inténtelo de nuevo.")
        return
    
    #Agregar el rol al array de roles
    roles.append(nuevo_rol)
    
    #Luego pasamos a mostrar un mensaje de éxito
    print("rol agregado satisfactoriamente.")

#CREAMOS UNA FUNCIÓN PARA LISTAR LOS ROLES DISPONIBLES.
def listar_roles():

    #Verificamos que haya roles disponibles
    if len(roles) == 0:
     print("no hay roles dsiponibles.")
     return
    
    #Mostramos los roles en una lista
    print("lista de roles disponibles: ")
    for rol in roles:
        print(f"-{rol}")

#CREAR UNA FUNCIÓN PARA MOSTRAR EL MENÚ DE OPCIONES SEGÚN EL ROL DEL USUARIO
def mostrar_menu(usuario):

    #Mostrar el menú según el rol de usuario
    if usuario["rol"] == "administrador":
        print("menú de opciones para administrador.")
        print("1. listar usuarios")
        print("2. ordenar usuarios")
        print("3. crear rol")
        print("4. listar roles")
        print("5. salir")
    elif usuario["rol"] =="usuario":
        print("menú de opciones para usuario.")
        print("1. listar usuarios.")
        print("2. listar roles")
        print("3. salir")
    else:
        print(f"no hay opciones para el rol {usuario['rol']}.")

#CREAR UNA FUNCIÓN PARA EJECUTAR LA OPCIÓN ELEGIDA POR EL USUARIO
def ejecutar_opcion(opcion,usuario):
    
    #Ejecutar la opción según el rol de usuario
    if usuario["rol"] == "administrador":
      if opcion == "1":
        listar_usuarios()
      elif opcion == "2":
        ordenar_usuarios()
      elif opcion == "3":
        crear_rol()
      elif opcion == "4":
        listar_roles()
      elif opcion == "5":
       return False
      else:
       print("Opción inválida. Intente de nuevo.")
    
    elif usuario["rol"] == "usuario":
      if opcion == "1":
          listar_usuarios()
      elif opcion == "2":
          listar_roles()
      elif opcion == "3":
         return
      else:
         print("Opción inválida. Intente de nuevo.")
    else:
       print(f"no hay opciones para el rol {usuario['rol']}.")

    #Retornar true si se quiere continuar con el programa
    return True
#Creamos una variable para controlar el ciclo principal del programa
continuar  = True



#Mostrar un mensaje de bienvenida
print("bienvenidos al aplicativo desarrollado por jack_luna.")

#Iniciar el ciclo principal del programa
while continuar :
   
   #Mostrar las opciones de inicio
   print("opciones de inicio: ")
   print("1. REGISTRARSE")
   print("2. INICIAR SESIÓN")
   print("3. SALIR")

   #Pedir al usuario que ingrese una opción
   opcion = input("ingrese una opción: ")

   #Ejecutar la opción elegida
   if opcion == "1":
      registrar_usuario()
   elif opcion == "2":
      usuario = iniciar_sesion()
      if usuario is not None:
         #	Iniciar un ciclo secundario para mostrar el menú según el rol del usuario
         while True:
            mostrar_menu(usuario)
            opcion = input("ingrese una opción: ")
            continuar = ejecutar_opcion(opcion, usuario)
            if not continuar:
               break
   elif opcion == "3":
     continuar = False  
   else:
      print ("la opción ingresada no es válida!, intente de nuevo.")

      #Mostrar un mensaje de despedida
      print("GRACIAS POR USAR EL APLICATIVO JACK_LUNA. HASTA PRONTO")