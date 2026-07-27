from utils.gestor_json import guardar_datos

def pedir_prestamo(datos, usuario_actual):
    print("\n" + "="*35)
    print("   FORMULARIO DE SOLICITUD DE PRÉSTAMO")
    print("="*35)
    
    # Verificamos si ya tiene deudas
    if usuario_actual['deuda'] > 0:
        print(f"Lo sentimos {usuario_actual['nombre']}, ya tienes una deuda activa de ${usuario_actual['deuda']}.")
        print("Debes pagarla antes de solicitar un nuevo crédito.")
        return

    # Usamos los datos que ya existen del usuario
    print(f"Hola, {usuario_actual['nombre']} {usuario_actual['apellido']}.")
    print("Como ya tenemos tus datos personales actualizados, solo necesitamos algunos detalles financieros para el estudio de crédito.\n")
    
    try:
        # Preguntas nuevas para el formulario
        ingresos = float(input("1. ¿Cuáles son tus ingresos mensuales aproximados?: $"))
        motivo = input("2. ¿Cuál es el motivo del préstamo? (Ej: Estudio, Vivienda, Libre inversión): ")
        meses = int(input("3. ¿A cuántos meses deseas diferir el pago? (Ej: 12, 24, 36): "))
        monto = float(input("4. Monto del préstamo a solicitar: $"))
        
        if monto <= 0 or meses <= 0 or ingresos <= 0:
            print("Error: Los valores numéricos deben ser mayores a cero.")
            return
            
        # Lógica de aprobación: el banco no presta más de 10 veces el salario mensual
        if monto > (ingresos * 10):
            print("\nPréstamo DENEGADO: El monto supera nuestra política de riesgo para tus ingresos reportados.")
            return

        # Cálculos de intereses (15% fijo sobre el total)
        interes = monto * 0.15 
        total_deuda = monto + interes
        cuota_mensual = total_deuda / meses
        
        print("\n--- RESUMEN DE APROBACIÓN ---")
        print(f"Motivo: {motivo}")
        print(f"Monto aprobado: ${monto}")
        print(f"Interés total del banco (15%): ${interes}")
        print(f"Deuda total a pagar: ${total_deuda}")
        print(f"Cuota mensual aproximada: ${cuota_mensual:.2f} durante {meses} meses")
        
        # Confirmación final
        confirmacion = input("\n¿Aceptas las condiciones del préstamo? (S/N): ").strip().lower()
        
        if confirmacion == 's':
            usuario_actual['saldo'] += monto
            usuario_actual['deuda'] += total_deuda
            usuario_actual['historial'].append(f"Préstamo aprobado: ${monto} a {meses} meses (Motivo: {motivo})")
            
            guardar_datos(datos)
            print(f"\n¡Felicidades {usuario_actual['nombre']}! Préstamo desembolsado exitosamente.")
            print(f"Tu nuevo saldo disponible es: ${usuario_actual['saldo']}")
        else:
            print("Solicitud cancelada por el usuario.")
            
    except ValueError:
        print("Error: Por favor ingresa valores numéricos válidos en los campos de dinero y meses.")
        