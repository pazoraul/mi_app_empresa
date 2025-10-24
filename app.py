import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

# --- CONFIGURACIÓN DE COLORES ---
COLOR_FONDO = "#f0f9f1"       # Fondo verde claro
COLOR_BOTON = "#2e8b57"       # Verde oscuro
COLOR_TEXTO_BOTON = "white"   # Texto blanco

# --- FUNCIÓN PARA GUARDAR DATOS ---
def guardar_producto():
    nombre = entry_nombre.get()
    cantidad = entry_cantidad.get()
    precio = entry_precio.get()
    descripcion = entry_descripcion.get()
    
    if not (nombre and cantidad and precio):
        messagebox.showwarning("Atención", "Por favor, completa todos los campos.")
        return

    archivo = "productos.csv"
    nuevo = not os.path.exists(archivo)
    
    with open(archivo, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if nuevo:
            writer.writerow(["id", "name", "qty", "price", "desc"])
        writer.writerow([len(tree.get_children())+1, nombre, cantidad, precio, descripcion])

    tree.insert("", "end", values=(len(tree.get_children())+1, nombre, cantidad, precio, descripcion))
    entry_nombre.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)

# --- FUNCIÓN PARA CARGAR DATOS EXISTENTES ---
def cargar_productos():
    archivo = "productos.csv"
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for fila in reader:
                tree.insert("", "end", values=(fila["id"], fila["name"], fila["qty"], fila["price"], fila["desc"]))

# --- INTERFAZ ---
root = tk.Tk()
root.title("Sistema de Productos - Mi Mini Empresa")
root.geometry("900x600")
root.config(bg=COLOR_FONDO)

# --- LOGO Y TÍTULO ---
try:
    logo = tk.PhotoImage(file="logo.png")
    lbl_logo = tk.Label(root, image=logo, bg=COLOR_FONDO)
    lbl_logo.pack(pady=10)
except:
    lbl_logo = tk.Label(root, text="Mi Mini Empresa", font=("Helvetica", 20, "bold"), bg=COLOR_FONDO, fg=COLOR_BOTON)
    lbl_logo.pack(pady=20)

titulo = tk.Label(root, text="📦 Control de Productos", font=("Arial", 16, "bold"), bg=COLOR_FONDO, fg="#1f5132")
titulo.pack(pady=5)

# --- FORMULARIO ---
frame_form = tk.Frame(root, bg=COLOR_FONDO)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Nombre:", bg=COLOR_FONDO).grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(frame_form)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Cantidad:", bg=COLOR_FONDO).grid(row=1, column=0, padx=5, pady=5)
entry_cantidad = tk.Entry(frame_form)
entry_cantidad.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Precio:", bg=COLOR_FONDO).grid(row=2, column=0, padx=5, pady=5)
entry_precio = tk.Entry(frame_form)
entry_precio.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Descripción:", bg=COLOR_FONDO).grid(row=3, column=0, padx=5, pady=5)
entry_descripcion = tk.Entry(frame_form)
entry_descripcion.grid(row=3, column=1, padx=5, pady=5)

# --- BOTONES ---
style = ttk.Style()
style.configure("TButton", background=COLOR_BOTON, foreground=COLOR_TEXTO_BOTON, font=("Arial", 10, "bold"))
style.map("TButton", background=[("active", "#3cb371")])

ttk.Button(frame_form, text="Guardar Producto", command=guardar_producto).grid(row=4, column=0, columnspan=2, pady=10)

# --- TABLA ---
cols = ("ID", "Nombre", "Cantidad", "Precio", "Descripción")
tree = ttk.Treeview(root, columns=cols, show="headings", height=10)
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=150)
tree.pack(pady=10)

cargar_productos()
root.mainloop()

