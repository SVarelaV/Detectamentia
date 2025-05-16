import tkinter as tk
from tkinter import messagebox
from paciente import Paciente
from pacientes import Pacientes

class GestionPacientes:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Pacientes")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f8ff")

        # Instancia para gestionar la lista de pacientes
        self.lista_pacientes = Pacientes()

        # Frame para los campos de entrada
        frame_campos = tk.LabelFrame(self.root, text="Datos del Paciente", bg="#f0f8ff", font=("Arial", 12, "bold"))
        frame_campos.pack(fill="x", padx=10, pady=10)

        tk.Label(frame_campos, text="ID Paciente:", bg="#f0f8ff").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.id_entry = tk.Entry(frame_campos)
        self.id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame_campos, text="Nombre:", bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.nombre_entry = tk.Entry(frame_campos)
        self.nombre_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame_campos, text="Primer Apellido:", bg="#f0f8ff").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.apellido1_entry = tk.Entry(frame_campos)
        self.apellido1_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(frame_campos, text="Segundo Apellido:", bg="#f0f8ff").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.apellido2_entry = tk.Entry(frame_campos)
        self.apellido2_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(frame_campos, text="Fecha de Nacimiento:", bg="#f0f8ff").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.fecha_nacimiento_entry = tk.Entry(frame_campos)
        self.fecha_nacimiento_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(frame_campos, text="Género:", bg="#f0f8ff").grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.genero_entry = tk.Entry(frame_campos)
        self.genero_entry.grid(row=5, column=1, padx=10, pady=5)

        # Frame para los botones
        frame_botones = tk.Frame(self.root, bg="#f0f8ff")
        frame_botones.pack(fill="x", padx=10, pady=10)

        tk.Button(frame_botones, text="Agregar", command=self.boton_agregar, bg="#007acc", fg="black").grid(row=0, column=0, padx=10, pady=10)
        tk.Button(frame_botones, text="Buscar", command=self.boton_buscar, bg="#007acc", fg="black").grid(row=0, column=1, padx=10, pady=10)
        tk.Button(frame_botones, text="Eliminar", command=self.boton_eliminar, bg="#007acc", fg="black").grid(row=0, column=2, padx=10, pady=10)
        tk.Button(frame_botones, text="Mostrar", command=self.boton_mostrar, bg="#007acc", fg="black").grid(row=0, column=3, padx=10, pady=10)

        # Área de texto para mostrar pacientes
        self.text_area = tk.Text(self.root, height=10, width=70, state="disabled")
        self.text_area.pack(padx=10, pady=10)

    def boton_agregar(self):
        id_paciente = self.id_entry.get()
        nombre = self.nombre_entry.get()
        apellido1 = self.apellido1_entry.get()
        apellido2 = self.apellido2_entry.get()
        fecha_nacimiento = self.fecha_nacimiento_entry.get()
        genero = self.genero_entry.get()

        if not id_paciente or not nombre or not apellido1 or not apellido2 or not fecha_nacimiento or not genero:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        if self.lista_pacientes.existe_paciente(id_paciente):
            messagebox.showerror("Error", "El ID del paciente ya existe.")
            return

        paciente = Paciente(id_paciente, nombre, apellido1, apellido2, fecha_nacimiento, genero)
        self.lista_pacientes.agregar_paciente(paciente)
        messagebox.showinfo("Éxito", "Paciente agregado correctamente.")
        self.limpiar_campos()

    def boton_buscar(self):
        id_paciente = self.id_entry.get()

        if not id_paciente:
            messagebox.showerror("Error", "El campo ID Paciente es obligatorio.")
            return

        paciente = self.lista_pacientes.buscar_paciente(id_paciente)
        if paciente:
            messagebox.showinfo("Paciente encontrado", f"ID: {paciente.id_paciente}\nNombre: {paciente.nombre}\nApellido 1: {paciente.apellido1}\nApellido 2: {paciente.apellido2}\nFecha de Nacimiento: {paciente.fecha_nacimiento}\nGénero: {paciente.genero}")
        else:
            messagebox.showerror("Error", "Paciente no encontrado.")

    def boton_eliminar(self):
        id_paciente = self.id_entry.get()

        if not id_paciente:
            messagebox.showerror("Error", "El campo ID Paciente es obligatorio.")
            return

        if self.lista_pacientes.eliminar_paciente(id_paciente):
            messagebox.showinfo("Éxito", "Paciente eliminado correctamente.")

    def boton_mostrar(self):
        self.text_area.configure(state="normal")
        self.text_area.delete(1.0, tk.END)

        pacientes = self.lista_pacientes.lista_pacientes
        if not pacientes:
            self.text_area.insert(tk.END, "No hay pacientes registrados.\n")
        else:
            for paciente in pacientes:
                self.text_area.insert(tk.END, f"ID: {paciente.id_paciente}, Nombre: {paciente.nombre}, Apellido 1: {paciente.apellido1}, Apellido 2: {paciente.apellido2}, Fecha de Nacimiento: {paciente.fecha_nacimiento}, Género: {paciente.genero}\n")

        self.text_area.configure(state="disabled")

    def limpiar_campos(self):
        self.id_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.apellido1_entry.delete(0, tk.END)
        self.apellido2_entry.delete(0, tk.END)
        self.fecha_nacimiento_entry.delete(0, tk.END)
        self.genero_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = GestionPacientes(root)
    root.mainloop()