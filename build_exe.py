"""
Script de construcción del ejecutable.
Utiliza PyInstaller para generar un ejecutable optimizado con todas las dependencias.
"""

import os
import sys
import logging
import shutil
from typing import List, Optional
import PyInstaller.__main__

# Constantes de configuración
EXECUTABLE_NAME = "GeneradorContraseñas"
REQUIRED_FILES = [
    "password_gui.py",
    "password_generator.py",
    "manager_theme.py",
    "icon.ico"
]
BUILD_OPTIONS = [
    f'--name={EXECUTABLE_NAME}',
    '--onefile',           # Genera un único ejecutable
    '--noconsole',        # Sin ventana de consola
    '--clean',            # Limpia archivos temporales
    '--noupx',            # No usar UPX
    '--exclude-module=unittest',  # Excluye módulos de prueba
    '--exclude-module=test',
    '--exclude-module=distutils',
    '--strip',            # Reduce tamaño
    '--optimize=2',       # Optimización máxima
    '--log-level=ERROR'   # Solo errores en log
]

def setup_logging() -> logging.Logger:
    """
    Configura y retorna un logger personalizado para el proceso de construcción.
    
    Returns:
        logging.Logger: Logger configurado
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger(__name__)

def verify_required_files(current_dir: str, logger: logging.Logger) -> bool:
    """
    Verifica que todos los archivos necesarios existan.
    
    Args:
        current_dir (str): Directorio actual del proyecto
        logger (Logger): Logger configurado para mensajes
        
    Returns:
        bool: True si todos los archivos existen, False en caso contrario
    """
    for file in REQUIRED_FILES:
        file_path = os.path.join(current_dir, file)
        if not os.path.exists(file_path):
            logger.error(f"Archivo no encontrado: {file}")
            return False
    return True

def clean_build_files(logger: logging.Logger):
    """
    Limpia los archivos temporales de construcción.
    
    Args:
        logger (Logger): Logger configurado para mensajes
    """
    try:
        if os.path.exists('build'):
            shutil.rmtree('build')
        spec_file = f'{EXECUTABLE_NAME}.spec'
        if os.path.exists(spec_file):
            os.remove(spec_file)
        logger.info("Archivos temporales limpiados exitosamente")
    except Exception as e:
        logger.warning(f"Error al limpiar archivos temporales: {e}")

def build_executable(logger: logging.Logger) -> bool:
    """
    Construye el ejecutable usando PyInstaller.
    
    Args:
        logger (Logger): Logger configurado para mensajes
        
    Returns:
        bool: True si la construcción fue exitosa, False en caso contrario
    """
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_dir, "icon.ico")

        if not verify_required_files(current_dir, logger):
            return False

        logger.info("Iniciando construcción del ejecutable...")

        # Preparar opciones de construcción
        build_command = [
            'password_gui.py',
            f'--icon={icon_path}',
            *BUILD_OPTIONS,
            '--add-data=password_generator.py;.',
            '--add-data=manager_theme.py;.',
            '--add-data=icon.ico;.'
        ]

        # Ejecutar PyInstaller (sin stdout y stderr)
        PyInstaller.__main__.run(build_command)

        # Verificar resultado
        exe_path = os.path.join(current_dir, 'dist', f'{EXECUTABLE_NAME}.exe')
        if os.path.exists(exe_path):
            logger.info(f"Ejecutable creado exitosamente en: {exe_path}")
            return True
        
        logger.error("No se pudo encontrar el ejecutable generado")
        return False

    except Exception as e:
        logger.error(f"Error durante la construcción: {str(e)}")
        return False

def main():
    """Función principal que coordina el proceso de construcción."""
    logger = setup_logging()
    
    try:
        logger.info("=== Iniciando proceso de construcción ===")
        
        if build_executable(logger):
            logger.info("=== Proceso completado exitosamente ===")
            clean_build_files(logger)
            return 0
        
        logger.error("=== El proceso falló ===")
        return 1

    except KeyboardInterrupt:
        logger.info("\nProceso interrumpido por el usuario")
        return 1

if __name__ == "__main__":
    sys.exit(main())
