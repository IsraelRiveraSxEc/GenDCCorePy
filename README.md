# Generador de Contraseñas NEIR

Una aplicación de escritorio segura y optimizada para generar contraseñas aleatorias con interfaz gráfica.

## Estado del Proyecto

🚀 **Versión actual:** 1.2.0
📅 **Última actualización:** [22/2/2025]
🔒 **Estado:** Estable

### Características Principales

- ✅ **Generación Segura**
  - Uso del módulo `secrets` para aleatoriedad criptográfica
  - Validación multinivel de parámetros (8-129 caracteres)
  - Sistema de puntuación de fortaleza en tiempo real
  - Rango de iteraciones configurable (1000-50000)

- ✅ **Interfaz Responsiva**
  - Diseño responsivo optimizado (699x480)
  - 10 temas visuales predefinidos
  - Retroalimentación visual inmediata
  - Indicadores de fortaleza con código de colores

- ✅ **Características Avanzadas**
  - Sistema de logging detallado
  - Manejo robusto de errores
  - Copiado seguro al portapapeles
  - Validación en tiempo real

### Temas Visuales Disponibles

1. 🌐 Cyberpunk
2. 🌙 Midnight
3. 🖥️ Matrix
4. 🌅 Sunset
5. ☀️ Light
6. 🌊 Ocean
7. 💛 Yellow
8. 🌈 Aurora
9. 🔥 Fire
10. 🎮 Purgan

## Requisitos Técnicos

### Sistema
- Python 3.13+
- 100MB espacio en disco
- 2GB RAM
- Windows 10/11

### Dependencias
```python
pyperclip>=1.8.2    # Gestión del portapapeles
pyinstaller>=6.11.0 # Construcción del ejecutable
```

## Estructura del Proyecto

```
generador-contraseñas/
├── password_generator.py # Core de generación
├── password_gui.py      # Interfaz gráfica
├── manager_theme.py     # Gestión de temas
├── build_config.json    # Configuración de construcción
├── build_exe.py        # Script de construcción
├── requirements.txt    # Dependencias
└── README.md          # Documentación
```

## Instalación

### Método 1: Ejecutable (Windows)
1. Descarga el último release
2. Ejecuta el archivo `.exe`
3. No requiere instalación adicional

### Método 2: Desde Código Fuente
```bash
git clone https://github.com/IsraelRiveraSxEc/GenDCCorePy.git
cd GenDCCorePy
pip install -r requirements.txt
python build_exe.py
```

## Uso

1. **Configuración de Contraseña**
   - Selecciona tipos de caracteres (a-z, A-Z, 0-9, !@#$%^&*)
   - Ajusta longitud (8-129)
   - Define iteraciones (1000-50000)

2. **Personalización Visual**
   - Elige entre 10 temas predefinidos
   - Interfaz adaptativa
   - Indicadores de fortaleza dinámicos

3. **Generación y Copiado**
   - Genera contraseña segura
   - Copia al portapapeles
   - Validación visual inmediata

## Desarrollo y Contribución

### Flujo de Trabajo
1. Fork del repositorio
2. Crear rama (`git checkout -b feature/NuevaCaracteristica`)
3. Commit (`git commit -m 'Añade nueva característica'`)
4. Push (`git push origin feature/NuevaCaracteristica`)
5. Pull Request

## Licencia

MIT License - Ver `LICENSE` para detalles

## Contacto

Nelson Espinosa Ec: 0961705423
[Repositorio del Proyecto](https://github.com/IsraelRiveraSxEc/GenDCCorePy)
