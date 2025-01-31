# Generador de Contraseñas

Una aplicación de escritorio simple y segura para generar contraseñas aleatorias.

## Estado del Proyecto

🚀 **Versión actual:** 1.0.0
📅 **Última actualización:** [30/1/2025]

### Progreso

- ✅ Implementación del generador de contraseñas
- ✅ Interfaz gráfica con Tkinter
- ✅ Sistema de logging
- ✅ Script de configuración de Python PATH
- ✅ Generación de ejecutable
- ✅ Documentación básica

### Próximas Características

- Por Definir

## Características

- Interfaz gráfica intuitiva
- Generación de contraseñas seguras
- Personalización de longitud y tipos de caracteres
- Ejecutable standalone para Windows

## Instalación

### Opción 1: Ejecutable (Windows)
1. Ve a la página principal del repositorio https://github.com/IsraelRiveraSxEc/GenDCCorePy
2. Descarga `GeneradorContraseñas.exe`
3. Ejecuta el archivo descargado

### Opción 2: Desde el código fuente
```bash
# Clonar el repositorio
git clone https://github.com/IsraelRiveraSxEc/GenDCCorePy.git

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python password_gui.py
```

## Crear el ejecutable

Para crear el ejecutable desde el código fuente:

```bash
python build_exe.py
```

El ejecutable se generará en la carpeta `dist/`.

## Estructura del Proyecto

```
GenDCCorePy/
├── password_gui.py       # Interfaz gráfica principal
├── password_generator.py # Lógica de generación de contraseñas
├── build_exe.py         # Script para crear el ejecutable
├── requirements.txt     # Dependencias del proyecto
├── setup_python_path.ps1# Script de configuración de PATH
└── README.md           # Documentación
```

## Tecnologías utilizadas

- Python 3.13
- Tkinter (GUI)
- PyInstaller (empaquetado)
- pyperclip (copiar al portapapeles)
- Git (control de versiones)

## Contribuir

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Fork el repositorio
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Realiza tus cambios
4. Commit tus cambios (`git commit -m 'Add: alguna característica asombrosa'`)
5. Push a la rama (`git push origin feature/AmazingFeature`)
6. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Israel Rivera - [@IsraelRiveraSxEc](https://github.com/IsraelRiveraSxEc)

Link del proyecto: [https://github.com/IsraelRiveraSxEc/GenDCCorePy](https://github.com/IsraelRiveraSxEc/GenDCCorePy)
