from utils.gestor_json import guardar_datos

def cambiar_informacion(datos, usuario_actual):
    print("\n--- ACTUALIZAR INFORMACIÓN ---")
    print("Deje en blanco el campo que no desee cambiar y presione Enter.")
    
    telefono = input(f"Teléfono actual ({usuario_actual['telefono']}): ")
    if telefono.strip(): usuario_actual['telefono'] = telefono
        
    direccion = input(f"Dirección actual ({usuario_actual['direccion']}): ")
    if direccion.strip(): usuario_actual['direccion'] = direccion
        
    correo = input(f"Correo actual ({usuario_actual['correo']}): ")
    if correo.strip(): usuario_actual['correo'] = correo

    guardar_datos(datos)
    print("Información actualizada exitosamente.")
