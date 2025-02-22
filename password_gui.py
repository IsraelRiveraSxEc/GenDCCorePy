import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
from password_generator import PasswordGenerator, PasswordStrength
import logging
from manager_theme import ThemeManager

class PasswordGeneratorGUI:
    """Clase para la interfaz gráfica del generador de contraseñas"""
    
    def __init__(self):
        """
        Inicializa la ventana principal y configura todos los componentes.
        Establece el tema inicial y crea la estructura base de la GUI.
        """
        self.theme_manager = ThemeManager()
        
        self.generator = PasswordGenerator()
        
        self.window = tk.Tk()
        self.window.title("Generador de Contraseñas NEIR")
        self.window.geometry("699x480")
        
        self.use_lower = tk.BooleanVar(value=True)
        self.use_upper = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_special = tk.BooleanVar(value=True)
        self.current_theme = tk.StringVar(value=self.theme_manager.get_default_theme())
        
        initial_theme = self.theme_manager.get_theme(self.current_theme.get())
        self.window.configure(bg=initial_theme["bg"])
        
        self.setup_styles()
        self.create_widgets()

    def setup_styles(self):
        """Configuración de estilos usando el tema actual"""
        theme = self.theme_manager.get_theme(self.current_theme.get())
        style = ttk.Style()
        
        style.configure('Futuristic.TFrame', background=theme["bg"])
        style.configure('Futuristic.TLabel', 
                       background=theme["bg"], 
                       foreground=theme["fg"],
                       font=(theme["font"], 12, 'bold'))
        style.configure('Title.TLabel',
                       background=theme["bg"],
                       foreground=theme["fg"],
                       font=(theme["font"], 24, 'bold'))
        style.configure('Futuristic.TButton', 
                       foreground=theme["fg"],
                       font=(theme["font"], 10, 'bold'))
        
    def create_widgets(self):
        """Crea todos los widgets de la interfaz"""
        self.main_frame = ttk.Frame(self.window, style='Futuristic.TFrame')
        self.main_frame.pack(padx=2, pady=2, fill='both', expand=True)
        
        ttk.Label(self.main_frame, 
                 text="GENERADOR DE CONTRASEÑAS NEIR",
                 style='Title.TLabel').pack(pady=15)
        
        theme_frame = ttk.Frame(self.main_frame, style='Futuristic.TFrame')
        theme_frame.pack(pady=8)
        
        ttk.Label(theme_frame, 
                 text="Tema:",
                 style='Futuristic.TLabel').pack(side=tk.LEFT, padx=5)
        
        theme_menu = ttk.OptionMenu(
            theme_frame,
            self.current_theme,
            self.theme_manager.get_default_theme(),
            *self.theme_manager.get_theme_names(),
            command=self.change_theme
        )
        theme_menu.pack(side=tk.LEFT, padx=5)
        
        self.create_character_options()
        
        self.create_input_fields()
        
        self.generate_btn = ttk.Button(
            self.main_frame,
            text="GENERAR CONTRASEÑA",
            command=self.generate_password,
            style='Futuristic.TButton'
        )
        self.generate_btn.pack(pady=8)
        
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(
            self.main_frame,
            textvariable=self.password_var,
            justify='center',
            state='readonly',
            font=('Helvetica', 14)
        )
        self.password_entry.pack(pady=8, fill='x', padx=8)
        
        self.strength_var = tk.StringVar()
        self.strength_label = ttk.Label(
            self.main_frame,
            textvariable=self.strength_var,
            style='Futuristic.TLabel'
        )
        self.strength_label.pack(pady=8)
        
        self.copy_btn = ttk.Button(
            self.main_frame,
            text="COPIAR AL PORTAPAPELES",
            command=self.copy_to_clipboard,
            style='Futuristic.TButton'
        )
        self.copy_btn.pack(pady=5)
        
    def create_character_options(self):
        options_frame = ttk.Frame(self.main_frame, style='Futuristic.TFrame')
        options_frame.pack(pady=2)
        
        ttk.Checkbutton(options_frame, 
                       text="Minúsculas",
                       variable=self.use_lower).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(options_frame,
                       text="Mayúsculas",
                       variable=self.use_upper).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(options_frame,
                       text="Números",
                       variable=self.use_digits).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(options_frame,
                       text="Especiales",
                       variable=self.use_special).pack(side=tk.LEFT, padx=5)
        
    def create_input_fields(self):
        ttk.Label(self.main_frame, 
                 text="Iteraciones (1000-50000):", 
                 style='Futuristic.TLabel').pack(pady=5)
        self.iterations = ttk.Entry(self.main_frame, justify='center')
        self.iterations.pack(pady=5)
        self.iterations.insert(0, "1000")
        
        ttk.Label(self.main_frame, 
                 text="Longitud (8-129):", 
                 style='Futuristic.TLabel').pack(pady=5)
        self.length = ttk.Entry(self.main_frame, justify='center')
        self.length.pack(pady=5)
        self.length.insert(0, "16")
        
    def generate_password(self):
        """Maneja el evento de generación de contraseña"""
        try:
            iterations = int(self.iterations.get())
            length = int(self.length.get())
            
            selected_options = sum([
                self.use_lower.get(),
                self.use_upper.get(),
                self.use_digits.get(),
                self.use_special.get()
            ])
            
            if length < 8:
                messagebox.showerror(
                    "Error - Longitud Insuficiente",
                    "⚠️ LONGITUD MUY CORTA:\n"
                    f"Has ingresado {length} caracteres\n\n"
                    "🛡️ REQUISITOS MÍNIMOS:\n"
                    "• La longitud mínima es 8 caracteres\n\n"
                    "📝 RECOMENDACIONES:\n"
                    "1. Usa 12 caracteres o más para mayor seguridad\n"
                    "2. Combina diferentes tipos de caracteres"
                )
                return
                
            if length <= 8:
                if selected_options < 3:
                    messagebox.showwarning(
                        "Advertencia - Seguridad Crítica",
                        "⚠️ ALERTA DE SEGURIDAD:\n"
                        f"Longitud actual: {length} caracteres\n\n"
                        "🔒 REQUISITOS PARA ESTA LONGITUD:\n"
                        "• Necesitas usar al menos 3 tipos de caracteres:\n"
                        f"  ▸ Minúsculas: {'✓' if self.use_lower.get() else '✗'}\n"
                        f"  ▸ Mayúsculas: {'✓' if self.use_upper.get() else '✗'}\n"
                        f"  ▸ Números: {'✓' if self.use_digits.get() else '✗'}\n"
                        f"  ▸ Especiales: {'✓' if self.use_special.get() else '✗'}\n\n"
                        "💡 SUGERENCIAS:\n"
                        "1. Selecciona al menos 3 tipos de caracteres, o\n"
                        "2. Aumenta la longitud a más de 8 caracteres\n"
                        "3. Se recomienda usar los 4 tipos para mayor seguridad"
                    )
                    return
            elif length <= 10:
                if selected_options < 2:
                    messagebox.showwarning(
                        "Advertencia - Seguridad Baja",
                        "⚠️ ALERTA DE SEGURIDAD:\n"
                        f"Longitud actual: {length} caracteres\n\n"
                        "🔒 REQUISITOS PARA ESTA LONGITUD:\n"
                        "• Necesitas usar al menos 2 tipos de caracteres:\n"
                        f"  ▸ Minúsculas: {'✓' if self.use_lower.get() else '✗'}\n"
                        f"  ▸ Mayúsculas: {'✓' if self.use_upper.get() else '✗'}\n"
                        f"  ▸ Números: {'✓' if self.use_digits.get() else '✗'}\n"
                        f"  ▸ Especiales: {'✓' if self.use_special.get() else '✗'}\n\n"
                        "💡 SUGERENCIAS:\n"
                        "1. Selecciona al menos 2 tipos de caracteres, o\n"
                        "2. Aumenta la longitud a más de 10 caracteres\n"
                        "3. Se recomienda usar 3 o más tipos para mayor seguridad"
                    )
                    return
            elif length <= 12:
                if selected_options < 2:
                    messagebox.showwarning(
                        "Advertencia - Seguridad Media",
                        "⚠️ ALERTA DE SEGURIDAD:\n"
                        f"Longitud actual: {length} caracteres\n\n"
                        "🔒 REQUISITOS PARA ESTA LONGITUD:\n"
                        "• Necesitas usar al menos 2 tipos de caracteres:\n"
                        f"  ▸ Minúsculas: {'✓' if self.use_lower.get() else '✗'}\n"
                        f"  ▸ Mayúsculas: {'✓' if self.use_upper.get() else '✗'}\n"
                        f"  ▸ Números: {'✓' if self.use_digits.get() else '✗'}\n"
                        f"  ▸ Especiales: {'✓' if self.use_special.get() else '✗'}\n\n"
                        "💡 SUGERENCIAS:\n"
                        "1. Selecciona al menos 2 tipos de caracteres, o\n"
                        "2. Aumenta la longitud a más de 12 caracteres\n"
                        "3. Se recomienda usar 3 o más tipos para mayor seguridad"
                    )
                    return
            elif length <= 15:
                if selected_options < 2:
                    messagebox.showwarning(
                        "Advertencia - Seguridad Media",
                        "⚠️ ALERTA DE SEGURIDAD:\n"
                        f"Longitud actual: {length} caracteres\n\n"
                        "🔒 REQUISITOS PARA ESTA LONGITUD:\n"
                        "• Necesitas usar al menos 2 tipos de caracteres:\n"
                        f"  ▸ Minúsculas: {'✓' if self.use_lower.get() else '✗'}\n"
                        f"  ▸ Mayúsculas: {'✓' if self.use_upper.get() else '✗'}\n"
                        f"  ▸ Números: {'✓' if self.use_digits.get() else '✗'}\n"
                        f"  ▸ Especiales: {'✓' if self.use_special.get() else '✗'}\n\n"
                        "💡 SUGERENCIAS:\n"
                        "1. Selecciona al menos 2 tipos de caracteres\n"
                        "2. Se recomienda usar 3 o más tipos para mayor seguridad"
                    )
                    return

            if not (1000 <= iterations <= 50000):
                messagebox.showerror(
                    "Error - Iteraciones Inválidas",
                    "⚠️ CONFIGURACIÓN INCORRECTA:\n"
                    f"Iteraciones actuales: {iterations}\n\n"
                    "🔒 REQUISITOS:\n"
                    "• Mínimo: 1,000 iteraciones\n"
                    "• Máximo: 50,000 iteraciones\n\n"
                    "💡 SUGERENCIA:\n"
                    "• Valor recomendado: 1,000 iteraciones"
                )
                return

            password, strength = self.generator.generate_password(
                length, iterations,
                self.use_lower.get(),
                self.use_upper.get(),
                self.use_digits.get(),
                self.use_special.get()
            )
            
            if password:
                self.password_var.set(password)
                self.strength_var.set(f"Fortaleza: {strength.value}")
                color = {
                    PasswordStrength.WEAK: "#ff0000",
                    PasswordStrength.MEDIUM: "#ffa500",
                    PasswordStrength.STRONG: "#00ff00",
                    PasswordStrength.VERY_STRONG: "#00ffff"
                }[strength]
                self.strength_label.configure(foreground=color)
            else:
                messagebox.showerror(
                    "Error - Parámetros Inválidos",
                    "⚠️ PROBLEMAS DETECTADOS:\n\n"
                    "📏 LONGITUD:\n"
                    f"• Valor actual: {length}\n"
                    "• Rango permitido: 8-129 caracteres\n\n"
                    "🔄 ITERACIONES:\n"
                    f"• Valor actual: {iterations}\n"
                    "• Rango permitido: 1000-50000\n\n"
                    "🔒 PARA SOLUCIONAR:\n"
                    "1. Ajusta la longitud entre 8 y 129 caracteres\n"
                    "2. Ajusta las iteraciones entre 1000 y 50000\n"
                    "3. Asegúrate de tener al menos dos tipos de caracteres seleccionados"
                )
            
        except ValueError:
            messagebox.showerror(
                "Error - Valores Inválidos",
                "⚠️ ENTRADA INCORRECTA:\n"
                "Los valores ingresados no son números válidos\n\n"
                "📝 VALORES ACTUALES:\n"
                f"• Longitud: '{self.length.get()}'\n"
                f"• Iteraciones: '{self.iterations.get()}'\n\n"
                "✅ FORMATO CORRECTO:\n"
                "• Longitud: número entero (8-129)\n"
                "• Iteraciones: número entero (1000-50000)\n\n"
                "❌ NO PERMITIDO:\n"
                "• Letras\n"
                "• Símbolos\n"
                "• Espacios"
            )
            
    def copy_to_clipboard(self):
        """Copia la contraseña generada al portapapeles"""
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo(
            "Éxito",
            "Contraseña copiada al portapapeles"
            )
        else:
            messagebox.showwarning(
            "Advertencia",
            "No hay nada que copiar. Primero genera una contraseña."
            )
            
    def run(self):
        """Inicia la aplicación"""
        self.window.mainloop()

    def change_theme(self, *args):
        """Cambia el tema de la aplicación"""
        theme = self.theme_manager.get_theme(self.current_theme.get())
        self.window.configure(bg=theme["bg"])
        self.setup_styles()
        
        self.main_frame.configure(style='Futuristic.TFrame')
        
        if self.strength_var.get():
            strength_text = self.strength_var.get()

if __name__ == "__main__":
    app = PasswordGeneratorGUI()  # Crea la instancia de la aplicación
    app.run()  # Inicia la aplicación