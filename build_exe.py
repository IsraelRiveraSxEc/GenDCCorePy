"""
Script de construcción del ejecutable.
Utiliza PyInstaller para generar un ejecutable optimizado con todas las dependencias.
"""

import json
import os
import shutil
import sys
from typing import Dict, Any
import PyInstaller.__main__

def load_config() -> Dict[str, Any]:
    """Carga la configuración desde build_config.json"""
    try:
        with open('build_config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: No se encontró build_config.json")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: build_config.json está mal formateado")
        sys.exit(1)

def clean_build_dirs(config: Dict[str, Any]) -> None:
    """Limpia los directorios de construcción si está configurado"""
    if config['build']['clean_build']:
        dirs_to_clean = [
            config['build']['output_dir'],
            config['build']['temp_dir']
        ]
        for dir_path in dirs_to_clean:
            if os.path.exists(dir_path):
                shutil.rmtree(dir_path)
                print(f"Limpiando directorio: {dir_path}")

def build_executable(config: Dict[str, Any]) -> None:
    """Construye el ejecutable usando PyInstaller"""
    app_config = config['application']
    build_config = config['build']
    pyinstaller_config = config['pyinstaller']
    
    # Prepara los argumentos para PyInstaller
    args = [
        pyinstaller_config['main_script'],
        f"--name={app_config['name']}",
        f"--icon={app_config['icon']}",
        f"--distpath={build_config['output_dir']}",
        f"--workpath={build_config['temp_dir']}",
    ]

    # Agrega opciones condicionales
    if build_config['one_file']:
        args.append('--onefile')
    if not build_config['console']:
        args.append('--noconsole')
    if build_config['debug']:
        args.append('--debug')

    # Agrega imports ocultos
    for hidden_import in pyinstaller_config['hidden_imports']:
        args.append(f'--hidden-import={hidden_import}')

    # Agrega archivos adicionales
    for file in pyinstaller_config['additional_files']:
        args.append(f'--add-data={file}{os.pathsep}{os.path.dirname(file)}')

    print("Iniciando construcción del ejecutable...")
    PyInstaller.__main__.run(args)
    print("Construcción completada exitosamente")

def main() -> int:
    """Función principal del script de construcción"""
    try:
        print("Cargando configuración de construcción...")
        config = load_config()
        
        print("Preparando entorno de construcción...")
        clean_build_dirs(config)
        
        print("Iniciando proceso de construcción...")
        build_executable(config)
        
        print(f"Ejecutable creado exitosamente en: {config['build']['output_dir']}")
        return 0
        
    except Exception as e:
        print(f"Error durante la construcción: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
