from utils.gestor_json import guardar_datos, buscar_usuario

def iniciar_sesion(datos):
    print("\n--- INICIAR SESIÓN ---")
    id_user = input("ID (Cédula): ")
    usuario = buscar_usuario(datos, id_user)

    if not usuario:
        print("El usuario no existe.")
        return None

    if usuario.get("intentos_fallidos", 0) >= 3:
        print("CUENTA BLOQUEADA por seguridad debido a múltiples intentos fallidos.")
        return None

    password = input("Contraseña: ")
    if usuario["password"] == password:
        usuario["intentos_fallidos"] = 0
        guardar_datos(datos)
        print(f"Bienvenido/a, {usuario['nombre']} {usuario['apellido']}.")
        return usuario
    else:
        usuario["intentos_fallidos"] = usuario.get("intentos_fallidos", 0) + 1
        guardar_datos(datos)
        print(f"Credenciales incorrectas. Intento fallido {usuario['intentos_fallidos']}/3.")
        return None
