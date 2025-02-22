# Generador de Contraseñas NEIR

Una aplicación de escritorio segura y optimizada para generar contraseñas aleatorias con interfaz gráfica moderna y personalizable.

## Estado del Proyecto

🚀 **Versión actual:** 1.2.0
📅 **Última actualización:** [21/2/2025]
🔒 **Estado:** Estable

### Características Implementadas

- ✅ Generador de contraseñas seguras con validación multinivel
- ✅ Interfaz gráfica moderna con Tkinter
- ✅ Sistema de temas visuales personalizables
  - 10 temas predefinidos optimizados
  - Combinaciones de colores mejoradas para mejor legibilidad
- ✅ Validación de seguridad en tiempo real
  - Análisis de fortaleza de contraseñas
  - Retroalimentación visual inmediata
- ✅ Optimizaciones de rendimiento
  - Tamaño de ventana optimizado (699x480)
  - Mejor gestión de recursos
- ✅ Características de seguridad
  - Uso de `secrets` para generación criptográficamente segura
  - Validación multinivel de parámetros
  - Mensajes de error detallados
- ✅ Funcionalidades adicionales
  - Copiado al portapapeles con confirmación
  - Sistema de logging para diagnóstico
  - Manejo robusto de errores

## Requisitos Técnicos

### Requisitos Mínimos
- Python 3.13+
- 100MB espacio en disco
- 2GB RAM
- Windows 10/11

### Dependencias Principales
- tkinter (incluido en Python)
- pyperclip
- typing
- secrets
- logging

## Instalación

Ejecutable (Windows)
1. Descarga la última versión desde la sección de releases
2. Ejecuta el archivo `.exe` descargado
3. No requiere instalación adicional

# Instalación 2 

1. Clona el repositorio: `git clone https://github.com/IsraelRiveraSxEc/GenDCCorePy.git`
2. Navega al directorio: `cd GenDCCorePy`
3. Instala las dependencias: `pip install -r requirements.txt`
4. Ejecuta la aplicación: `python build_exe.py`

## Uso

1. Selecciona los tipos de caracteres deseados:
   - Minúsculas (a-z)
   - Mayúsculas (A-Z)
   - Números (0-9)
   - Caracteres especiales (!@#$%^&*)

2. Configura los parámetros:
   - Longitud (8-129 caracteres)
   - Iteraciones (1000-50000)

3. Selecciona un tema visual: (opcional)
   - Cyberpunk
   - Midnight
   - Matrix
   - Sunset
   - Light
   - Ocean
   - Yellow
   - Aurora
   - Fire
   - Purgan

4. Genera y copia tu contraseña segura

# Desarrollo

### Estructura del Proyecto
```
generador-contraseñas/
├── password_gui.py      # Interfaz gráfica principal
├── password_generator.py # Lógica de generación
├── manager_theme.py     # Gestión de temas
├── build_config.json    # Configuración de construcción
├── build_exe.py        # Script de construcción
├── requirements.txt     # Dependencias de producción
└── README.md           # Documentación
```

## Contribución

1. Fork el proyecto
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

Nelson Espinosa Ec: 0961705423

Link del proyecto: [https://github.com/IsraelRiveraSxEc/GenDCCorePy](https://github.com/IsraelRiveraSxEc/GenDCCorePy)
