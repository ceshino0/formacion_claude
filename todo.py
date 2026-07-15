"""
To-Do List v2 - Con prioridades y fechas límite
Una lista de tareas simple que corre en la terminal.

Cómo usarla:
    python todo.py
"""

import json
import os

ARCHIVO_TAREAS = "tareas.json"

# Orden de prioridad para poder ordenar las tareas (menor número = más urgente)
ORDEN_PRIORIDAD = {"alta": 0, "media": 1, "baja": 2}

# Emoji para cada prioridad, así se ve más claro en la lista
ICONO_PRIORIDAD = {"alta": "🔴", "media": "🟡", "baja": "🟢"}


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


def pedir_prioridad():
    """Pregunta al usuario la prioridad y valida que sea una opción correcta."""
    while True:
        prioridad = input("Prioridad (alta / media / baja) [Enter = media]: ").strip().lower()
        if prioridad == "":
            return "media"
        if prioridad in ORDEN_PRIORIDAD:
            return prioridad
        print("Opción no válida. Escribe: alta, media o baja.")


def pedir_fecha():
    """Pregunta al usuario una fecha límite opcional, en formato AAAA-MM-DD."""
    fecha = input("Fecha límite (AAAA-MM-DD) [Enter = sin fecha]: ").strip()
    return fecha if fecha else None


def ordenar_tareas(tareas):
    """Devuelve las tareas ordenadas por prioridad: alta primero, baja al final."""
    return sorted(tareas, key=lambda t: ORDEN_PRIORIDAD.get(t.get("prioridad", "media"), 1))


def mostrar_tareas(tareas):
    """Imprime todas las tareas ordenadas por prioridad, con su estado y fecha."""
    if not tareas:
        print("\n No tienes tareas todavía.\n")
        return

    tareas_ordenadas = ordenar_tareas(tareas)

    print("\n--- Tus tareas (ordenadas por prioridad) ---")
    for i, tarea in enumerate(tareas_ordenadas, start=1):
        estado = "✅" if tarea["completada"] else "⬜"
        icono_prioridad = ICONO_PRIORIDAD.get(tarea.get("prioridad", "media"), "🟡")
        fecha = tarea.get("fecha_limite")
        texto_fecha = f" (para: {fecha})" if fecha else ""
        print(f"{i}. {estado} {icono_prioridad} {tarea['texto']}{texto_fecha}")
    print()


def agregar_tarea(tareas):
    texto = input("Escribe la nueva tarea: ").strip()
    if not texto:
        print("La tarea no puede estar vacía.\n")
        return

    prioridad = pedir_prioridad()
    fecha_limite = pedir_fecha()

    tareas.append({
        "texto": texto,
        "completada": False,
        "prioridad": prioridad,
        "fecha_limite": fecha_limite,
    })
    guardar_tareas(tareas)
    print("Tarea agregada.\n")


def completar_tarea(tareas):
    tareas_ordenadas = ordenar_tareas(tareas)
    mostrar_tareas(tareas)
    if not tareas:
        return
    try:
        numero = int(input("Número de la tarea a marcar como completada: "))
        tarea_elegida = tareas_ordenadas[numero - 1]
        tarea_elegida["completada"] = True
        guardar_tareas(tareas)
        print("Tarea marcada como completada.\n")
    except (ValueError, IndexError):
        print("Número inválido.\n")


def eliminar_tarea(tareas):
    tareas_ordenadas = ordenar_tareas(tareas)
    mostrar_tareas(tareas)
    if not tareas:
        return
    try:
        numero = int(input("Número de la tarea a eliminar: "))
        tarea_elegida = tareas_ordenadas[numero - 1]
        tareas.remove(tarea_elegida)
        guardar_tareas(tareas)
        print(f"Eliminada: {tarea_elegida['texto']}\n")
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
