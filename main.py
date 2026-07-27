import sys
import os
from utils.gestor_json import cargar_datos
from operaciones.login import iniciar_sesion
from operaciones.registro import registrar_usuario
from operaciones.retiros import retirar_dinero
from operaciones.transferencias import enviar_plata
from operaciones.prestamos import pedir_prestamo
from operaciones.perfil import cambiar_informacion
from operaciones.servicios import pagar_servicio

# --- ESTILOS VISUALES PARA LA TERMINAL ---
class Color:
    VERDE = '\033[92m'
    AMARILLO = '\033[93m'
    ROJO = '\033[91m'
    AZUL = '\033[94m'
    CIAN = '\033[96m'
    NEGRITA = '\033[1m'
    RESET = '\033[0m'

def limpiar_pantalla():
    """Limpia la terminal dependiendo del sistema operativo (Windows o Linux/Mac)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Pausa la ejecución para que el usuario pueda leer los mensajes"""
    input(f"\n{Color.AMARILLO}Presiona ENTER para continuar...{Color.RESET}")

# --- MENÚ PRINCIPAL ---
def menu_principal():
    datos = cargar_datos()
    usuario_actual = None

    while True:
        limpiar_pantalla()
        
        # MENÚ 1: SI NO HAY NADIE LOGUEADO
        if not usuario_actual:
            print(f"{Color.AZUL}{Color.NEGRITA}")
            print("╔════════════════════════════════════════════╗")
            print("║           SISTEMA BANCARIO ADSO            ║")
            print("╚════════════════════════════════════════════╝")
            print(f"{Color.RESET}")
            print(f"  {Color.VERDE}[1]{Color.RESET} Iniciar Sesión")
            print(f"  {Color.VERDE}[2]{Color.RESET} Registrarse")
            print(f"  {Color.ROJO}[3]{Color.RESET} Salir")
            print("──────────────────────────────────────────────")
            
            opcion = input(f"{Color.CIAN}➤ Elige una opción: {Color.RESET}")

            if opcion == '1':
                limpiar_pantalla()
                usuario_actual = iniciar_sesion(datos)
                pausar()
            elif opcion == '2':
                limpiar_pantalla()
                registrar_usuario(datos)
                pausar()
            elif opcion == '3':
                limpiar_pantalla()
                print(f"{Color.VERDE}¡Gracias por usar nuestro sistema bancario! Hasta pronto.{Color.RESET}\n")
                sys.exit(0)
            else:
                print(f"\n{Color.ROJO}✖ Opción no válida. Por favor, elige 1, 2 o 3.{Color.RESET}")
                pausar()
                
        # MENÚ 2: SI EL USUARIO YA INICIÓ SESIÓN
        else:
            nombre_completo = f"{usuario_actual['nombre']} {usuario_actual['apellido']}".upper()
            
            print(f"{Color.AZUL}{Color.NEGRITA}")
            print("╔═════════════════════════════════════════════════════════╗")
            print(f"║  BIENVENIDO/A: {nombre_completo:<40} ║")
            print("╚═════════════════════════════════════════════════════════╝")
            print(f"{Color.RESET}")
            
            # Mostramos el saldo en verde y la deuda en rojo
            print(f"  💰 {Color.NEGRITA}Saldo Disponible:{Color.RESET} {Color.VERDE}${usuario_actual['saldo']:,.2f}{Color.RESET}")
            if usuario_actual['deuda'] > 0:
                print(f"  💳 {Color.NEGRITA}Deuda Actual:{Color.RESET}     {Color.ROJO}${usuario_actual['deuda']:,.2f}{Color.RESET}")
            print("───────────────────────────────────────────────────────────")
            
            print(f"  {Color.CIAN}[1]{Color.RESET} Retirar plata")
            print(f"  {Color.CIAN}[2]{Color.RESET} Enviar plata")
            print(f"  {Color.CIAN}[3]{Color.RESET} Pedir un préstamo")
            print(f"  {Color.CIAN}[4]{Color.RESET} Pagar servicios (Agua, Luz, etc)")
            print(f"  {Color.CIAN}[5]{Color.RESET} Ver historial de movimientos")
            print(f"  {Color.CIAN}[6]{Color.RESET} Cambiar mi información")
            print(f"  {Color.ROJO}[7]{Color.RESET} Cerrar Sesión")
            print("───────────────────────────────────────────────────────────")
            
            opcion = input(f"{Color.AMARILLO}➤ ¿Qué deseas hacer hoy?: {Color.RESET}")

            if opcion == '1':
                limpiar_pantalla()
                retirar_dinero(datos, usuario_actual)
                pausar()
            elif opcion == '2':
                limpiar_pantalla()
                enviar_plata(datos, usuario_actual)
                pausar()
            elif opcion == '3':
                limpiar_pantalla()
                pedir_prestamo(datos, usuario_actual)
                pausar()
            elif opcion == '4':
                limpiar_pantalla()
                pagar_servicio(datos, usuario_actual)
                pausar()
            elif opcion == '5':
                limpiar_pantalla()
                print(f"{Color.CIAN}{Color.NEGRITA}--- HISTORIAL DE MOVIMIENTOS ---{Color.RESET}\n")
                if not usuario_actual["historial"]:
                    print(f"{Color.AMARILLO}No hay movimientos recientes.{Color.RESET}")
                else:
                    for mov in usuario_actual["historial"]:
                        # Un pequeño efecto para que los retiros y pagos se vean mejor
                        if "Retiro" in mov or "Pago" in mov or "enviada" in mov:
                            print(f"{Color.ROJO}↘ {mov}{Color.RESET}")
                        else:
                            print(f"{Color.VERDE}↗ {mov}{Color.RESET}")
                pausar()
            elif opcion == '6':
                limpiar_pantalla()
                cambiar_informacion(datos, usuario_actual)
                pausar()
            elif opcion == '7':
                limpiar_pantalla()
                usuario_actual = None 
                print(f"{Color.VERDE}✓ Sesión cerrada correctamente. ¡Vuelve pronto!{Color.RESET}")
                pausar()
            else:
                print(f"\n{Color.ROJO}✖ Opción no válida. Por favor, elige un número del 1 al 7.{Color.RESET}")
                pausar()

if __name__ == "__main__":
    menu_principal()
