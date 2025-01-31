# Importamos los módulos necesarios
import tkinter as tk  # Módulo principal para la interfaz gráfica
from tkinter import ttk, messagebox  # Widgets modernos y cuadros de diálogo
import pyperclip  # Para copiar texto al portapapeles
from password_generator import PasswordGenerator  # Nuestra clase generadora de contraseñas
import logging  # Para registro de eventos

class PasswordGeneratorGUI:
    """Clase para la interfaz gráfica del generador de contraseñas"""
    
    def __init__(self):
        """Constructor de la interfaz gráfica"""
        # Creamos una instancia del generador de contraseñas
        self.generator = PasswordGenerator()
        
        # Configuración de la ventana principal
        self.window = tk.Tk()
        self.window.title("Generador de Contraseñas")
        self.window.geometry("800x600")  # Tamaño inicial de la ventana
        self.window.configure(bg='#1e1e1e')  # Fondo oscuro
        
        # Configuración de estilos para los widgets
        style = ttk.Style()
        # Estilo para el marco principal
        style.configure('Futuristic.TFrame', background='#1e1e1e')
        # Estilo para las etiquetas normales
        style.configure('Futuristic.TLabel', 
                       background='#1e1e1e', 
                       foreground='#00ff00',
                       font=('Helvetica', 12, 'bold'))
        # Estilo para el título
        style.configure('Title.TLabel',
                       background='#1e1e1e',
                       foreground='#00ff00',
                       font=('Helvetica', 24, 'bold'))
        # Estilo para los botones
        style.configure('Futuristic.TButton', 
                       background='#333333', 
                       foreground='#00ff00',
                       font=('Helvetica', 10, 'bold'))
                       
        # Creación del marco principal
        self.main_frame = ttk.Frame(self.window, style='Futuristic.TFrame')
        self.main_frame.pack(padx=40, pady=30, fill='both', expand=True)
        
        # Título de la aplicación
        ttk.Label(self.main_frame, 
                 text="GENERADOR DE CONTRASEÑAS",
                 style='Title.TLabel').pack(pady=20)
        
        # Campo de entrada para las iteraciones
        ttk.Label(self.main_frame, 
                 text="Iteraciones (1000-50000):", 
                 style='Futuristic.TLabel').pack(pady=5)
        self.iterations = ttk.Entry(self.main_frame, justify='center', font=('Helvetica', 12))
        self.iterations.pack(pady=5)
        self.iterations.insert(0, "1000")  # Valor por defecto
        
        # Campo de entrada para la longitud
        ttk.Label(self.main_frame, 
                 text="Longitud (8-129):", 
                 style='Futuristic.TLabel').pack(pady=5)
        self.length = ttk.Entry(self.main_frame, justify='center', font=('Helvetica', 12))
        self.length.pack(pady=5)
        self.length.insert(0, "16")  # Valor por defecto
        
        # Botón para generar contraseña
        self.generate_btn = ttk.Button(
            self.main_frame,
            text="GENERAR CONTRASEÑA",
            command=self.generate_password,
            style='Futuristic.TButton'
        )
        self.generate_btn.pack(pady=30)
        
        # Campo para mostrar la contraseña generada
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(
            self.main_frame,
            textvariable=self.password_var,
            justify='center',
            state='readonly',  # Solo lectura
            font=('Helvetica', 14)
        )
        self.password_entry.pack(pady=20, fill='x', padx=40)
        
        # Botón para copiar al portapapeles
        self.copy_btn = ttk.Button(
            self.main_frame,
            text="COPIAR AL PORTAPAPELES",
            command=self.copy_to_clipboard,
            style='Futuristic.TButton'
        )
        self.copy_btn.pack(pady=20)
        
    def generate_password(self):
        """Maneja el evento de generación de contraseña"""
        try:
            # Obtiene y convierte los valores de entrada a enteros
            iterations = int(self.iterations.get())
            length = int(self.length.get())
            
            # Intenta generar la contraseña
            password = self.generator.generate_password(length, iterations)
            
            if password:
                # Si se generó correctamente, muestra la contraseña
                self.password_var.set(password)
                logging.info("Contraseña generada y mostrada en GUI")
            else:
                # Si hubo error, muestra mensaje de error
                messagebox.showerror(
                    "Error",
                    "Parámetros inválidos. La longitud debe estar entre 8 y 129, "
                    "y las iteraciones entre 1000 y 50000."
                )
        except ValueError:
            # Si los valores no son números válidos
            messagebox.showerror("Error", "Por favor, ingrese números válidos")
            
    def copy_to_clipboard(self):
        """Copia la contraseña generada al portapapeles"""
        password = self.password_var.get()
        if password:
            # Si hay una contraseña generada, la copia al portapapeles
            pyperclip.copy(password)
            messagebox.showinfo("Éxito", "Contraseña copiada al portapapeles")
            logging.info("Contraseña copiada al portapapeles")
            
    def run(self):
        """Inicia la aplicación"""
        self.window.mainloop()

# Punto de entrada del programa
if __name__ == "__main__":
    app = PasswordGeneratorGUI()  # Crea la instancia de la aplicación
    app.run()  # Inicia la aplicación