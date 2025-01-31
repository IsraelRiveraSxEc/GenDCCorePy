# Script para construir el ejecutable
import PyInstaller.__main__
import os

# Obtiene el directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Configura las opciones de PyInstaller
PyInstaller.__main__.run([
    'password_gui.py',  # Archivo principal
    '--name=GeneradorContraseñas',  # Nombre del ejecutable
    '--onefile',  # Crear un solo archivo ejecutable
    '--noconsole',  # Sin consola (modo ventana)
    '--clean',  # Limpiar caché antes de construir
    '--add-data=password_generator.py;.',  # Incluir archivo adicional
])