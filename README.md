# Sistema de Gestión de Turnos de Farmacia

Este programa permite gestionar y consultar los turnos de empleados de una farmacia. Funciona mediante una interfaz gráfica creada con Tkinter, y permite realizar consultas de turnos específicos, verificar quién está trabajando a cierta hora y visualizar la tabla completa de horarios semanal.


## Funcionalidades principales

- **Consulta de turnos por empleado y día.**
- **Visualización completa de horarios semanales.**
- **Consulta de empleados trabajando en una hora específica.**

## Cómo usar el programa

1. **Ejecutar el programa:**
   Ejecuta el archivo en Python. Aparecerá una ventana con la interfaz gráfica para realizar consultas.

2. **Consultar turno por empleado:**
   - Introduce el nombre del empleado en el campo "Nombre del Empleado". 
   - Escribe el día de la semana en el campo "Día de la Semana".
   - Presiona el botón "Consultar Turno". Si el empleado tiene un turno ese día, se mostrará un mensaje con la información.

3. **Consultar tabla de horarios semanal:**
   - Haz clic en el botón "Ver Tabla de Horarios Semanal".
   - Aparecerá una ventana emergente mostrando los turnos de todos los empleados para cada día de la semana.

4. **Consultar empleado trabajando a una hora específica:**
   - Escribe la hora en formato `HH:MM` (por ejemplo: "15:30") en el campo "Hora (HH:MM)".
   - Introduce el día de la semana en el campo "Día de la Semana".
   - Presiona el botón "Consultar Empleado(s) a Hora Específica". Verás quién está trabajando en esa hora y día, si corresponde.

## Notas importantes

- Los nombres de los empleados deben coincidir exactamente con los definidos en el programa. Por ejemplo: "Empleado_1", "Empleado_2"... hasta el 4.
- Los días de la semana deben escribirse correctamente: "Lunes", "Martes", etc.
- La hora debe estar en el formato de 24 horas (HH:MM), dentro del rango 00:00 a 23:59.


## Modificaciones

Los turnos predefinidos y los nombres de los empleados pueden ser editados directamente en el código en las estructuras turnos_predefinidos y empleados.
