import tkinter as tk
from tkinter import messagebox
import json
import os

# --- AJUSTE DE RUTA AUTOMÁTICA ---
# Esto detecta la carpeta donde está guardado este archivo 'interfaz.py'
DIRECTORIO_APP = os.path.dirname(os.path.abspath(__file__))
# Une la carpeta con el nombre del archivo de forma segura
ARCHIVO_JSON = os.path.join(DIRECTORIO_APP, 'cumpleanos.json')
# ---------------------------------

def guardar_datos():
    nombre = entry_nombre.get().strip()
    fecha = entry_fecha.get().strip()

    if not nombre or not fecha:
        messagebox.showwarning("Advertencia", "Por favor, completa ambos campos.")
        return

    # Cargar datos existentes
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as archivo:
            try:
                datos = json.load(archivo)
            except json.JSONDecodeError:
                datos = {} 
    else:
        datos = {}

    # Agregar el nuevo registro
    datos[nombre] = fecha
    
    # Guardar todo de vuelta en el JSON (añadimos encoding para tildes y eñes)
    with open(ARCHIVO_JSON, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

    messagebox.showinfo("Éxito", f"Cumpleaños de {nombre} guardado correctamente.")
    entry_nombre.delete(0, tk.END)
    entry_fecha.delete(0, tk.END)

def ver_guardados():
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as archivo:
            try:
                datos = json.load(archivo)
                if not datos:
                    messagebox.showinfo("Lista de Amigos", "Aún no hay cumpleaños guardados.")
                    return
                
                texto = "Cumpleaños registrados:\n\n"
                for nom, fec in datos.items():
                    texto += f"• {nom}: {fec}\n"
                
                messagebox.showinfo("Lista de Amigos", texto)
            except json.JSONDecodeError:
                messagebox.showerror("Error", "El archivo de datos tiene un problema de formato.")
    else:
        messagebox.showinfo("Lista de Amigos", "Aún no hay cumpleaños guardados.")

# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("Gestor de Cumpleaños")
ventana.geometry("300x300")

tk.Label(ventana, text="Nombre del amigo:").pack(pady=(20, 5))
entry_nombre = tk.Entry(ventana, width=25)
entry_nombre.pack()

tk.Label(ventana, text="Fecha de cumpleaños (MM-DD):\nEjemplo: 02-25").pack(pady=(15, 5))
entry_fecha = tk.Entry(ventana, width=25)
entry_fecha.pack()

btn_guardar = tk.Button(ventana, text="Guardar Nuevo / Actualizar", command=guardar_datos, bg="lightblue")
btn_guardar.pack(pady=(20, 10))

btn_ver = tk.Button(ventana, text="Ver Todos los Cumpleaños", command=ver_guardados, bg="lightgreen")
btn_ver.pack(pady=5)

ventana.mainloop()