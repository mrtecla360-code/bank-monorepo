from utils.gestor_json import guardar_datos

def pedir_prestamo(datos, usuario_actual):
    print("\n--- SOLICITUD DE PRÉSTAMO ---")
    if usuario_actual['deuda'] > 0:
        print(f"Ya tienes una deuda activa de ${usuario_actual['deuda']}. Págala antes de pedir otro préstamo.")
        return

    try:
        monto = float(input("Monto del préstamo solicitado: $"))
        if monto > 0:
            interes = monto * 0.15 # 15% de interés
            total_deuda = monto + interes
            
            usuario_actual['saldo'] += monto
            usuario_actual['deuda'] += total_deuda
            usuario_actual['historial'].append(f"Préstamo aprobado: ${monto} (Deuda con 15% interés: ${total_deuda})")
            
            guardar_datos(datos)
            print(f"Préstamo aprobado. Se han añadido ${monto} a tu cuenta.")
            print(f"La deuda total a pagar con interés es de ${total_deuda}.")
        else:
            print("Monto inválido.")
    except ValueError:
        print("Error: Por favor ingresa un valor numérico válido.")
