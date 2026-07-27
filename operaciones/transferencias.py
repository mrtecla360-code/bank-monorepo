from utils.gestor_json import guardar_datos, buscar_usuario

def enviar_plata(datos, usuario_actual):
    print("\n--- TRANSFERENCIA ---")
    id_destino = input("ID del usuario destino: ")
    destino = buscar_usuario(datos, id_destino)
    
    if not destino:
        print("El usuario destino no existe.")
        return
    if destino["id"] == usuario_actual["id"]:
        print("No puedes transferirte a ti mismo.")
        return

    try:
        monto = float(input("Monto a enviar: $"))
        if monto <= 0:
            print("El monto debe ser mayor a cero.")
            return
            
        if monto <= usuario_actual['saldo']:
            usuario_actual['saldo'] -= monto
            destino['saldo'] += monto
            
            usuario_actual['historial'].append(f"Transferencia enviada de ${monto} a {destino['nombre']}")
            destino['historial'].append(f"Transferencia recibida de ${monto} de {usuario_actual['nombre']}")
            
            guardar_datos(datos)
            print(f"Transferencia de ${monto} a {destino['nombre']} exitosa.")
        else:
            print("Fondos insuficientes.")
    except ValueError:
        print("Error: Por favor ingresa un valor numérico válido.")
