"""
To-Do List - Mi primer proyecto real
Una lista de tareas simple que corre en la terminal.

Cómo usarla:
    python todo.py
"""

import json
import os

ARCHIVO_TAREAS = "tareas.json"


def cargar_tareas():
    """Lee las tareas guardadas en el archivo JSON. Si no existe, empieza vacío."""
    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def guardar_tareas(tareas):
    """Guarda la lista de tareas en el archivo JSON."""
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=2, ensure_ascii=False)


def mostrar_tareas(tareas):
    """Imprime todas las tareas con su estado."""
    if not tareas:
        print("\n No tienes tareas todavía.\n")
        return

    print("\n--- Tus tareas ---")
    for i, tarea in enumerate(tareas, start=1):
        estado = "✅" if tarea["completada"] else "⬜"
        print(f"{i}. {estado} {tarea['texto']}")
    print()


def agregar_tarea(tareas):
    texto = input("Escribe la nueva tarea: ").strip()
    if texto:
        tareas.append({"texto": texto, "completada": False})
        guardar_tareas(tareas)
        print("Tarea agregada.\n")
    else:
        print("La tarea no puede estar vacía.\n")


def completar_tarea(tareas):
    mostrar_tareas(tareas)
    if not tareas:
        return
    try:
        numero = int(input("Número de la tarea a marcar como completada: "))
        tareas[numero - 1]["completada"] = True
        guardar_tareas(tareas)
        print("Tarea marcada como completada.\n")
    except (ValueError, IndexError):
        print("Número inválido.\n")


def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    if not tareas:
        return
    try:
        numero = int(input("Número de la tarea a eliminar: "))
        eliminada = tareas.pop(numero - 1)
        guardar_tareas(tareas)
        print(f"Eliminada: {eliminada['texto']}\n")
    except (ValueError, IndexError):
        print("Número inválido.\n")


def menu():
    print("=" * 30)
    print("       MI LISTA DE TAREAS")
    print("=" * 30)
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


def main():
    tareas = cargar_tareas()

    while True:
        menu()
        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.\n")


if __name__ == "__main__":
    main()