from utils.gestor_json import guardar_datos

def pagar_servicio(datos, usuario_actual):
    print("\n--- PAGO DE SERVICIOS ---")
    print("1. Agua ($35.000)")
    print("2. Luz ($60.000)")
    print("3. Internet ($80.000)")
    print("4. Volver")
    
    opcion = input("Elige un servicio a pagar: ")
    precios = {'1': 35000, '2': 60000, '3': 80000}
    nombres = {'1': 'Agua', '2': 'Luz', '3': 'Internet'}
    
    if opcion in precios:
        monto = precios[opcion]
        servicio = nombres[opcion]
        
        if usuario_actual['saldo'] >= monto:
            usuario_actual['saldo'] -= monto
            usuario_actual['historial'].append(f"Pago de servicio: {servicio} por ${monto}")
            guardar_datos(datos)
            print(f"Pago de {servicio} exitoso. Nuevo saldo: ${usuario_actual['saldo']}")
        else:
            print(f"Fondos insuficientes para pagar {servicio}.")
    elif opcion == '4':
        return
    else:
        print("Opción inválida.")
