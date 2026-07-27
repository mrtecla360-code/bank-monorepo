from utils.gestor_json import guardar_datos, buscar_usuario

def enviar_plata(datos, usuario_actual):
    print("\n--- TRANSFERENCIA ---")
    id_destino = input("ID (Cédula) del usuario destino: ")
    destino = buscar_usuario(datos, id_destino)
    
    if not destino:
        print("El usuario destino no existe en el sistema.")
        return
    if destino["id"] == usuario_actual["id"]:
        print("No puedes transferir dinero a tu propia cuenta.")
        return

    try:
        monto = float(input(f"Monto a enviar a {destino['nombre']} {destino['apellido']}: $"))
        if monto <= 0:
            print("El monto debe ser mayor a cero.")
            return
            
        if monto <= usuario_actual['saldo']:
            usuario_actual['saldo'] -= monto
            destino['saldo'] += monto
            
            # Actualizamos el historial de ambos usuarios
            usuario_actual['historial'].append(f"Transferencia enviada de ${monto} a {destino['nombre']}")
            destino['historial'].append(f"Transferencia recibida de ${monto} de {usuario_actual['nombre']}")
            
            guardar_datos(datos)
            print(f"Transferencia de ${monto} a {destino['nombre']} realizada con éxito.")
        else:
            print("Fondos insuficientes para la transferencia.")
    except ValueError:
        print("Error: Por favor ingresa un valor numérico válido.")
        