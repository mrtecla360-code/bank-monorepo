from utils.gestor_json import guardar_datos

def retirar_dinero(datos, usuario_actual):
    print(f"\nSaldo actual: ${usuario_actual['saldo']}")
    try:
        monto = float(input("Monto a retirar: $"))
        if monto <= 0:
            print("El monto debe ser mayor a cero.")
            return
            
        if monto <= usuario_actual['saldo']:
            usuario_actual['saldo'] -= monto
            usuario_actual['historial'].append(f"Retiro de ${monto}")
            guardar_datos(datos)
            print(f"Retiro exitoso. Nuevo saldo: ${usuario_actual['saldo']}")
        else:
            print("Fondos insuficientes.")
    except ValueError:
        print("Error: Por favor ingresa un valor numérico válido.")
