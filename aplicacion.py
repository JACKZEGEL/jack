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
        
    usuario={"nombre":nombre, "apellido": apellido, "email":email, "password":password, "rol": rol}
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
    criterio = input("ingrese el criterio de ordenamiento (nombre o apellido): ")
    if criterio not in ["nombre", "apellido"]:
        print ("criterio no valido.")


#integrantes : luna ruiz & ader diestra (borrador)



        

        



    
 
    



    
   

    

