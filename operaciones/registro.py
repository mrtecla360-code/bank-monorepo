from utils.gestor_json import guardar_datos, buscar_usuario

def registrar_usuario(datos):
    print("\n--- REGISTRO DE NUEVO USUARIO ---")
    id_user = input("ID (Cédula): ")
    if buscar_usuario(datos, id_user):
        print("Error: El usuario ya existe.")
        return

    try:
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = int(input("Edad: "))
        telefono = input("Teléfono: ")
        direccion = input("Dirección: ")
        correo = input("Correo electrónico: ")
        password = input("Contraseña: ")
        
        nuevo_usuario = {
            "id": id_user,
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "telefono": telefono,
            "direccion": direccion,
            "correo": correo,
            "password": password,
            "saldo": 0.0,
            "deuda": 0.0,
            "intentos_fallidos": 0,
            "historial": []
        }
        datos["usuarios"].append(nuevo_usuario)
        guardar_datos(datos)
        print("¡Usuario registrado con éxito!")
    except ValueError:
        print("Error en el registro: La edad debe ser un número entero.")
