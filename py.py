usuarios = []
roles = ["administrador", "usuarios"]

def registrar_usuario():
    nombre=input("Ingrese el Nombre del Usuario: ")
    apellido= input ("Ingrese Apellido: ")
    email=input("ingrese Email: ")
    password=input("Ingrese Password:")
    rol = input("ingrese su rol(administardor o usuario): ")
    #validar que los datos sean correctos

    if rol not in roles:
        print("rol no válido. intente de nuevo")
        return 
    for usuario in usuarios:
        if usuario["email"]==email:
            print("email ya existe, ingrese uno diferente.")
        
    usuario={"nombre":nombre,
              "apellido": apellido,
                "email":email, 
                "password":password,
                  "rol": rol}
    
    usuarios.append(usuario)
    print("\n Usuario Registrado con exito!")



def iniciar_sesion ():
    email = input("ingrese su email: ")
    password = input("ingrese su password: ")
    for usuario in usuarios:
        if usuario["email"]==email and usuario["password"]==password:
            print(f"bienvenido{usuario['nombre']} {usuario['apellido']} .tu rol es{usuario['rol']}")
            return
        print("email o password incorrectos. intente de nuevo")

def listar_usuarios():
    if len(usuarios) == 0:
        print("No hay Usuarios")
    print("lista de usuarios regitrados")
    print("-"*75)
    print(f"{'nombre':<20}{'apellido':<20} {'email':<20}{'rol':<20}")
    print("-"*75)
    for usuario in usuarios:
     print(f"{usuario['nombre']:<20}{usuario['apellido']:<20}{usuario['email']:<20}{usuario['rol']:<20}")
    print("-"*75)

def ordenar_usuarios():

    criterio = input("ingrese el criterio de orden (nombre o apellido): ")
    if criterio not in ["nombre", "apellido"]:
        print ("criterio no válido. inténtelo de nuevo")
    
    sentido = input("ingrese el sentido de ordenamiento(ascendente o descendente)")
    if sentido not in ["ascendente", "descendente"]:
        print("sentido no válido, intente nuevamente")

    usuarios.sort(key=lambda x:x[criterio], reverse=(sentido=="descendente"))
    
    print(f"usuarios ordenados por {criterio} en sentido {sentido}.")

def crear_rol():
    nuevo_rol = input("ingrese el nombre del nuevo rol")
    if nuevo_rol in roles:
        print("el rol agregado ya existe, inténtelo de nuevo.")

    roles.append(nuevo_rol)
    print("rol agregado satisfactoriamente")

def listar_roles():
    if len(roles) == 0:
     print("no hay roles disponible.")
    
    print("lista de roles disponibles: ")
    for rol in roles:
        print(f"-{rol}")

def mostrar_menu(usuario):
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

def ejecutar_opcion(opcion,usuario):
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

continuar  = True

print("bienvenidos al aplicativo desarrollado por jack_luna.")
while continuar :
   print("opciones de inicio: ")
   print("1. REGISTRARSE")
   print("2. INICIAR SESIÓN")
   print("3. SALIR")
   opcion = input("ingrese una opción: ")
   if opcion == "1":
      registrar_usuario()
   elif opcion == "2":
      usuario = iniciar_sesion()
      if usuario is not None:
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
      print("GRACIAS POR USAR EL APLICATIVI JACK_LUNA. HASTA PRONTO")
