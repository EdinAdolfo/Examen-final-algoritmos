import tkinter as tk
import csv
import tkinter.messagebox
import os

def save_data():
    name = entry_name.get()
    grade = entry_grade.get()

    # Verificar que los campos no estén vacíos
    if name == "" or grade == "":
        tkinter.messagebox.showerror("Error", "Los campos no pueden estar vacíos.")
        return

    # Validar que la nota sea un número
    try:
        grade = int(grade)
    except ValueError:
        tkinter.messagebox.showerror("Error", "La nota debe ser un número.")
        return

    # Guardar datos en el archivo CSV
    with open('notas.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, grade])

    # Limpiar campos de entrada
    entry_name.delete(0, tk.END)
    entry_grade.delete(0, tk.END)

    # Mostrar mensaje de éxito
    tkinter.messagebox.showinfo("Éxito", "Datos guardados correctamente.")

# Crear ventana principal
root = tk.Tk()
root.title("Gestor de Notas")

# Verificar si el archivo CSV existe y crear encabezados si es necesario
if not os.path.exists('notas.csv'):
    with open('notas.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Nota"])

# Configurar interfaz gráfica
label_name = tk.Label(root, text="Nombre:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_grade = tk.Label(root, text="Nota:")
label_grade.pack()
entry_grade = tk.Entry(root)
entry_grade.pack()

save_button = tk.Button(root, text="Guardar", command=save_data)
save_button.pack(pady=10)

# Configurar tamaño de la ventana
root.geometry("300x200")

# Iniciar el bucle de la interfaz gráfica
root.mainloop()
