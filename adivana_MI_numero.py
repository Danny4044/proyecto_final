"""
PROYECTO INTEGRADOR - ADIVINA EL NÚMERO
Versión final completa con todas las funcionalidades
"""

import random
import os
import sys

class Configuracion:
    def __init__(self):
        self.rango_min = 1
        self.rango_max = 100
        self.max_intentos = 10
        self.dificultad = "normal"
        self.mostrar_pistas = True
        self.sonidos = False

class Estadisticas:
    def __init__(self):
        self.partidas_jugadas = 0
        self.partidas_ganadas = 0
        self.mejor_puntuacion = float('inf')
        self.total_intentos = 0
        self.historial_partidas = []

config = Configuracion()
stats = Estadisticas()

def mostrar_bienvenida():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 60)
    print("           🎮 ADIVINA EL NÚMERO 🎮")
    print("=" * 60)
    print("  ¡La computadora adivinará tu número secreto!")
    print("=" * 60)
    print("\nINSTRUCCIONES RÁPIDAS:")
    print("  M = Mi número es MAYOR")
    print("  N = Mi número es MENOR")
    print("  C = ¡CORRECTO! Adivinaste")
    print("=" * 60)
    input("\nPresiona ENTER para continuar...")

def mostrar_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "═" * 40)
    print("         MENÚ PRINCIPAL")
    print("═" * 40)
    print("  1. 🎯 Jugar nueva partida")
    print("  2. 📊 Ver estadísticas")
    print("  3. ⚙️  Configurar juego")
    print("  4. 📖 Instrucciones completas")
    print("  5. 🚪 Salir del juego")
    print("═" * 40)
    
    while True:
        opcion = input("\n  Seleccione opción (1-5): ").strip()
        if opcion in ['1', '2', '3', '4', '5']:
            return opcion
        print("  ❌ Opción no válida. Intente de nuevo.")

def jugar_partida():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 50)
    print("         NUEVA PARTIDA")
    print("=" * 50)
    print(f"\n  Piensa un número entre {config.rango_min} y {config.rango_max}")
    print("  La computadora intentará adivinarlo...")
    input("\n  Presiona ENTER cuando estés listo...")
    
    inferior = config.rango_min
    superior = config.rango_max
    intentos = 0
    adivinado = False
    historial = []
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "─" * 50)
    print("¡COMIENZA LA ADIVINANZA!")
    print("─" * 50)
    
    while intentos < config.max_intentos and not adivinado:
        intentos += 1
        
        # Calcular propuesta según dificultad
        if config.dificultad == "facil":
            propuesta = random.randint(inferior, superior)
        elif config.dificultad == "experto":
            medio = (inferior + superior) // 2
            ruido = random.randint(-3, 3)
            propuesta = max(inferior, min(superior, medio + ruido))
        else:
            propuesta = (inferior + superior) // 2
        
        historial.append({
            'intento': intentos,
            'propuesta': propuesta,
            'rango': (inferior, superior)
        })
        
        print(f"\n  🎯 INTENTO #{intentos}")
        if config.mostrar_pistas:
            rango = superior - inferior + 1
            print(f"  🔍 Rango actual: {inferior}-{superior}")
            print(f"  📊 Opciones posibles: {rango}")
            if rango > 0:
                print(f"  📈 Probabilidad: {100/rango:.1f}%")
        
        print(f"\n  ¿Es {propuesta} tu número?")
        print("  Responde: (M)ayor, (N)enor, (C)orrecto")
        
        while True:
            respuesta = input("  Tu respuesta: ").strip().upper()
            if respuesta in ['M', 'MAYOR']:
                respuesta = 'M'
                break
            elif respuesta in ['N', 'MENOR']:
                respuesta = 'N'
                break
            elif respuesta in ['C', 'CORRECTO', 'SI', 'S']:
                respuesta = 'C'
                break
            print("  ❌ Respuesta no válida. Use M, N o C")
        
        if respuesta == 'C':
            adivinado = True
            stats.partidas_ganadas += 1
            if intentos < stats.mejor_puntuacion:
                stats.mejor_puntuacion = intentos
            
            print("\n" + "🎉" * 25)
            print("         ¡FELICIDADES!")
            print(f"      Adivinado en {intentos} intentos")
            print("🎉" * 25)
            
            optimo = 7  # log2(100)
            eficiencia = (optimo / intentos) * 100
            print(f"\n  📈 Análisis de rendimiento:")
            print(f"    Óptimo teórico: {optimo} intentos")
            print(f"    Eficiencia: {eficiencia:.1f}%")
            
            if eficiencia >= 100:
                print("    ⭐ ¡Rendimiento PERFECTO!")
            elif eficiencia >= 90:
                print("    👍 ¡Excelente rendimiento!")
            
        elif respuesta == 'M':
            inferior = propuesta + 1
            print(f"  📈 Entonces es MAYOR que {propuesta}")
        elif respuesta == 'N':
            superior = propuesta - 1
            print(f"  📉 Entonces es MENOR que {propuesta}")
        
        if inferior > superior:
            print("\n  ⚠️  ¡Algo no cuadra! Revisa tus respuestas.")
            inferior = config.rango_min
            superior = config.rango_max
    
    if not adivinado:
        print("\n" + "😔" * 20)
        print("  No pude adivinar tu número")
        print(f"  Último rango: {inferior}-{superior}")
        print("😔" * 20)
    
    stats.partidas_jugadas += 1
    stats.total_intentos += intentos
    stats.historial_partidas.append({
        'intentos': intentos,
        'adivinado': adivinado,
        'historial': historial[-5:] if len(historial) > 5 else historial
    })
    
    input("\n  Presiona ENTER para continuar...")

def mostrar_estadisticas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 50)
    print("         ESTADÍSTICAS")
    print("=" * 50)
    
    print(f"\n  📊 PARTIDAS:")
    print(f"    Total jugadas: {stats.partidas_jugadas}")
    
    if stats.partidas_jugadas > 0:
        porcentaje = (stats.partidas_ganadas / stats.partidas_jugadas) * 100
        print(f"    Ganadas: {stats.partidas_ganadas} ({porcentaje:.1f}%)")
    else:
        print("    Ganadas: 0 (0%)")
    
    if stats.mejor_puntuacion < float('inf'):
        print(f"    Mejor puntuación: {stats.mejor_puntuacion} intentos")
    else:
        print("    Mejor puntuación: --")
    
    if stats.partidas_ganadas > 0:
        promedio = stats.total_intentos / stats.partidas_ganadas
        print(f"    Promedio de intentos: {promedio:.1f}")
    
    print(f"\n  ⚙️  CONFIGURACIÓN ACTUAL:")
    print(f"    Dificultad: {config.dificultad}")
    print(f"    Pistas: {'Activadas' if config.mostrar_pistas else 'Desactivadas'}")
    print(f"    Rango: {config.rango_min}-{config.rango_max}")
    print(f"    Máx. intentos: {config.max_intentos}")
    
    print("\n" + "=" * 50)
    input("\n  Presiona ENTER para continuar...")

def configurar_juego():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 50)
        print("         CONFIGURACIÓN")
        print("=" * 50)
        
        print(f"\n  1. Dificultad: {config.dificultad}")
        print(f"  2. Pistas: {'Activadas' if config.mostrar_pistas else 'Desactivadas'}")
        print(f"  3. Rango: {config.rango_min}-{config.rango_max}")
        print(f"  4. Máx. intentos: {config.max_intentos}")
        print(f"  5. Volver al menú")
        
        opcion = input("\n  Seleccione opción (1-5): ").strip()
        
        if opcion == "1":
            print("\n  Niveles:")
            print("    1. Fácil (aleatorio)")
            print("    2. Normal (búsqueda binaria)")
            print("    3. Experto (con ruido)")
            nivel = input("\n  Seleccione (1-3): ").strip()
            if nivel == "1":
                config.dificultad = "facil"
                config.max_intentos = 15
                print("  ✅ Dificultad: FÁCIL")
            elif nivel == "2":
                config.dificultad = "normal"
                config.max_intentos = 10
                print("  ✅ Dificultad: NORMAL")
            elif nivel == "3":
                config.dificultad = "experto"
                config.max_intentos = 7
                print("  ✅ Dificultad: EXPERTO")
        
        elif opcion == "2":
            config.mostrar_pistas = not config.mostrar_pistas
            print(f"  ✅ Pistas {'activadas' if config.mostrar_pistas else 'desactivadas'}")
        
        elif opcion == "3":
            try:
                min_val = int(input("  Nuevo mínimo (1-1000): "))
                max_val = int(input(f"  Nuevo máximo ({min_val+1}-1000): "))
                if 1 <= min_val < max_val <= 1000:
                    config.rango_min = min_val
                    config.rango_max = max_val
                    print(f"  ✅ Rango: {min_val}-{max_val}")
                else:
                    print("  ❌ Rango inválido")
            except:
                print("  ❌ Debe ingresar números")
        
        elif opcion == "4":
            try:
                max_int = int(input("  Nuevo máximo (3-20): "))
                if 3 <= max_int <= 20:
                    config.max_intentos = max_int
                    print(f"  ✅ Máx. intentos: {max_int}")
                else:
                    print("  ❌ Debe ser 3-20")
            except:
                print("  ❌ Debe ingresar número")
        
        elif opcion == "5":
            break
        
        input("\n  Presiona ENTER para continuar...")

def mostrar_instrucciones():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 60)
    print("               INSTRUCCIONES COMPLETAS")
    print("=" * 60)
    
    print("=" * 60)
    input("\n  Presiona ENTER para continuar...")

def main():
    mostrar_bienvenida()
    juego_activo = True
    
    while juego_activo:
        opcion = mostrar_menu()
        
        if opcion == "1":
            jugar_partida()
        elif opcion == "2":
            mostrar_estadisticas()
        elif opcion == "3":
            configurar_juego()
        elif opcion == "4":
            mostrar_instrucciones()
        elif opcion == "5":
            print("\n" + "=" * 50)
            print("  ¡Gracias por jugar AdivinaMiNúmero!")
            print("  Proyecto Integrador - Lógica de Programación")
            print("=" * 50)
            juego_activo = False
    
    input("\n  Presiona ENTER para salir...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  ⚠️  Juego interrumpido por el usuario")
    except Exception as e:
        print(f"\n  ❌ Error inesperado: {e}")
