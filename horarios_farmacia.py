import tkinter as tk
from tkinter import messagebox

# Datos iniciales
empleados = ["Empleado_1", "Empleado_2", "Empleado_3", "Empleado_4"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Turnos predefinidos: cada día tiene asignaciones diferentes para cada empleado
turnos_predefinidos = {
    "Lunes": {
        "Empleado_1": "00:00-06:00", "Empleado_2": "06:00-12:00", "Empleado_3": "12:00-18:00", "Empleado_4": "18:00-23:59"
    },
    "Martes": {
        "Empleado_1": "06:00-12:00", "Empleado_2": "12:00-18:00", "Empleado_3": "18:00-23:59", "Empleado_4": "00:00-06:00"
    },
    "Miércoles": {
        "Empleado_1": "12:00-18:00", "Empleado_2": "18:00-23:59", "Empleado_3": "00:00-06:00", "Empleado_4": "06:00-12:00"
    },
    "Jueves": {
        "Empleado_1": "18:00-23:59", "Empleado_2": "00:00-06:00", "Empleado_3": "06:00-12:00", "Empleado_4": "12:00-18:00"
    },
    "Viernes": {
        "Empleado_1": "00:00-06:00", "Empleado_2": "06:00-12:00", "Empleado_3": "12:00-18:00", "Empleado_4": "18:00-23:59"
    },
    "Sábado": {
        "Empleado_1": "06:00-12:00", "Empleado_2": "12:00-18:00", "Empleado_3": "18:00-23:59", "Empleado_4": "00:00-06:00"
    },
    "Domingo": {
        "Empleado_1": "12:00-18:00", "Empleado_2": "18:00-23:59", "Empleado_3": "00:00-06:00", "Empleado_4": "06:00-12:00"
    }
}


# Algoritmo Bubble Sort
def ordenar_empleados(empleados_lista):
    n = len(empleados_lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if empleados_lista[j] > empleados_lista[j+1]:
                empleados_lista[j], empleados_lista[j+1] = empleados_lista[j+1], empleados_lista[j]


# Algoritmo de búsqueda binaria
def busqueda_binaria(lista, elemento):
    bajo = 0
    alto = len(lista) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == elemento:
            return medio  # Se encontró el elemento
        elif lista[medio] < elemento:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1  # No se encontró el elemento

# Función para obtener el turno de un empleado en un día específico utilizando búsqueda binaria
def consultar_turno():
    nombre_empleado = entry_empleado.get()
    dia_semana = entry_dia.get()

    # Validar si el empleado existe
    if nombre_empleado not in empleados:
        messagebox.showerror("Error", "El nombre del empleado no es válido.")
        return

    # Validar si el día ingresado es válido
    if dia_semana not in dias_semana:
        messagebox.showerror("Error", "El día ingresado no es válido.")
        return

    # Ordenar la lista de empleados alfabéticamente
    empleados_ordenados = list(turnos_predefinidos[dia_semana].keys())
    empleados_ordenados.sort()

    # Usamos búsqueda binaria para encontrar el empleado
    indice = busqueda_binaria(empleados_ordenados, nombre_empleado)

    if indice != -1:
        # Si el empleado es encontrado, mostramos su turno
        turno = turnos_predefinidos[dia_semana][empleados_ordenados[indice]]
        messagebox.showinfo("Turno encontrado", f"{nombre_empleado} tiene el turno {turno} el {dia_semana}.")
    else:
        messagebox.showerror("Error", f"No se encontró al empleado {nombre_empleado} en el día {dia_semana}.")

# Función para mostrar la tabla de horarios semanal
def mostrar_tabla_horarios():
    tabla = "Tabla de Horario Semanal\n\n"
    for dia in dias_semana:
        tabla += f"{dia}:\n"
        
        # Ordenamos los empleados alfabéticamente por su nombre
        empleados_ordenados = list(turnos_predefinidos[dia].keys())
        empleados_ordenados.sort()  # Ordenamos con sort() antes de aplicar la búsqueda binaria
        
        for empleado in empleados_ordenados:
            tabla += f"  {empleado}: {turnos_predefinidos[dia][empleado]}\n"
        tabla += "\n"
    
    messagebox.showinfo("Horario Semanal", tabla)

# Función para consultar quién está trabajando a una hora específica
def consultar_empleado_a_hora():
    hora = entry_hora.get()
    dia_semana = entry_dia_consulta.get()

    # Validar si el día ingresado es válido
    if dia_semana not in dias_semana:
        messagebox.showerror("Error", "El día ingresado no es válido.")
        return

    # Validar que la hora esté en el formato correcto
    if not (hora >= "00:00" and hora <= "23:59"):
        messagebox.showerror("Error", "La hora debe estar en formato HH:MM (00:00 a 23:59).")
        return
    
    # Buscar qué empleados están trabajando en esa hora
    empleados_trabajando = []
    for empleado, turno in turnos_predefinidos[dia_semana].items():
        turno_inicio, turno_fin = turno.split('-')
        
        # Verificar si la hora está dentro del turno
        if turno_inicio <= hora < turno_fin:
            empleados_trabajando.append(empleado)

    if empleados_trabajando:
        empleados_str = ", ".join(empleados_trabajando)
        messagebox.showinfo("Empleado Trabajando", f"A las {hora} en {dia_semana}, {empleados_str} está trabajando")
    else:
        messagebox.showinfo("Empleado Trabajando", f"No hay empleados trabajando a las {hora} en {dia_semana}.")

# Interfaz gráfica
root = tk.Tk()
root.title("Consulta de Turnos de Farmacia")

# Etiqueta y entrada para el nombre del empleado
tk.Label(root, text="Nombre del Empleado:").grid(row=0, column=0, padx=10, pady=10)
entry_empleado = tk.Entry(root)
entry_empleado.grid(row=0, column=1, padx=10, pady=10)

# Etiqueta y entrada para el día de la semana
tk.Label(root, text="Día de la Semana:").grid(row=1, column=0, padx=10, pady=10)
entry_dia = tk.Entry(root)
entry_dia.grid(row=1, column=1, padx=10, pady=10)

# Botón para consultar el turno
btn_consultar = tk.Button(root, text="Consultar Turno", command=consultar_turno)
btn_consultar.grid(row=2, column=0, columnspan=2, pady=10)

# Botón para ver la tabla de horarios semanal
btn_tabla_horarios = tk.Button(root, text="Ver Tabla de Horarios Semanal", command=mostrar_tabla_horarios)
btn_tabla_horarios.grid(row=3, column=0, columnspan=2, pady=10)

# Etiqueta y entrada para consultar empleados a una hora específica
tk.Label(root, text="Hora (HH:MM):").grid(row=4, column=0, padx=10, pady=10)
entry_hora = tk.Entry(root)
entry_hora.grid(row=4, column=1, padx=10, pady=10)

# Etiqueta y entrada para el día de la semana
tk.Label(root, text="Día de la Semana:").grid(row=5, column=0, padx=10, pady=10)
entry_dia_consulta = tk.Entry(root)
entry_dia_consulta.grid(row=5, column=1, padx=10, pady=10)

# Botón para consultar qué empleados están trabajando a una hora específica
btn_empleados_a_hora = tk.Button(root, text="Consultar Empleado(s) a Hora Específica", command=consultar_empleado_a_hora)
btn_empleados_a_hora.grid(row=6, column=0, columnspan=2, pady=10)

# Iniciar la aplicación
root.mainloop()
