import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import csv
import os

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        process_file(file_path)

def process_file(file_path):
    clean_rows = []
    rows_id = []
    dict = {}

    with open(file_path, newline='', encoding='utf-8') as csv_entrada:
        lector_csv = csv.reader(csv_entrada)

        first_row = next(lector_csv)
        first_row[0] = "[OPERATOR]"
        clean_rows.append(first_row)
        clean_rows.append(first_row)
        next(lector_csv)

        for r in lector_csv:
            r.pop()
            r[0] = ""
            rows_id.append(r[-1])
            r.append("")
            dict[str(r[-2])] = r

        for x in dict:
            clean_rows.append(dict.get(x))

    # Construir la ruta del archivo de salida
    dir_path = os.path.dirname(file_path)
    save_path = os.path.join(dir_path, 'datos_limpios.csv')

    # Guardar el archivo CSV limpio
    with open(save_path, 'w', newline='', encoding='utf-8') as csv_output:
        write_csv = csv.writer(csv_output)
        write_csv.writerows(clean_rows)

    # Mostrar notificación
    messagebox.showinfo("Proceso finalizado", "Se ha creado el nuevo archivo CSV exitosamente.")

    # Cerrar la aplicación
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.geometry("500x350")
root.title("Procesamiento de suplencias CSV")

# Estilo para el botón
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), foreground="#FFFFFF", background="#4CAF50", borderwidth=0)
style.map("TButton", background=[('active', '#45a049')])
style.configure("TLabel", font=("Arial", 12), foreground="#333333")
style.configure("Custom.TButton", font=("Arial", 12, "bold"), foreground="black", background="#007bff", borderwidth=0)
style.map("Custom.TButton", background=[('active', '#0056b3')])

# Primer comentario
label_intro = ttk.Label(root, text="Introduce el archivo de SuplenciasUnified.csv que quieres limpiar.")
label_intro.pack(pady=10)

# Botón para seleccionar archivo
select_button = ttk.Button(root, text="Seleccionar archivo de suplencias CSV", style="Custom.TButton", command=select_file)
select_button.pack(pady=20)

# Segundo comentario
label_second_intro = ttk.Label(root, text="Una vez seleccionado se te creará un nuevo archivo \nen el mismo sitio donde esta el otro archivo llamado \n'datos_limpios.csv' con el formato limpio.")
label_second_intro.pack()

# Comentario autor
label_author = ttk.Label(root, text="Hecho por Pablo Mochon Ubiña", font=("Arial", 10), foreground="#555555")
label_author.pack(side=tk.BOTTOM, pady=10)

# Ejecutar la aplicación
root.mainloop()
