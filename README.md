# Generador de Contraseñas

Una aplicación de escritorio segura y optimizada para generar contraseñas aleatorias.

## Estado del Proyecto

🚀 **Versión actual:** 1.1.0
📅 **Última actualización:** [15/2/2025]

### Características Implementadas

- ✅ Generador de contraseñas seguras con validación multinivel
- ✅ Interfaz gráfica moderna con Tkinter
- ✅ Sistema de temas visuales (5 temas personalizables)
- ✅ Ejecutable optimizado con PyInstaller
- ✅ Validación de seguridad de contraseñas (4 niveles)
- ✅ Copiado al portapapeles con retroalimentación
- ✅ Sistema de logging detallado
- ✅ Manejo de errores robusto

### Próximas Características

- 🔄 Sistema de pruebas automatizadas (unittest/pytest)
- 💾 Persistencia de configuraciones (JSON/SQLite)
- 🌍 Soporte multiidioma (i18n)
- 🎨 Más temas visuales
- ♿ Modo de alto contraste para accesibilidad

## Requisitos Técnicos

- Python 3.13+
- 100MB espacio en disco
- 2GB RAM
- Windows 10/11

## Instalación

### Opción 1: Ejecutable (Windows)
1. Descarga `GeneradorContraseñas.exe` desde releases
2. Ejecuta directamente - No requiere instalación

### Opción 2: Desde código fuente
```bash
git clone https://github.com/IsraelRiveraSxEc/GenDCCorePy.git
cd GenDCCorePy
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python password_gui.py
```

## Estructura del Proyecto

```
GenDCCorePy/
├── password_gui.py       # Interfaz gráfica principal
├── password_generator.py # Lógica de generación
├── manager_theme.py      # Gestor de temas
├── build_exe.py         # Script de compilación
├── icon.ico             # Icono de la aplicación
├── requirements.txt     # Dependencias
└── README.md           # Documentación
```

## Desarrollo

### Configuración del entorno
```bash
# Instalar dependencias de desarrollo
pip install -r requirements-dev.txt

# Ejecutar pruebas
python -m pytest

# Generar ejecutable
python build_exe.py
```

### Convenciones de código
- PEP 8 para estilo de código
- Docstrings en formato Google
- Type hints para todas las funciones
- Comentarios en español

## Seguridad

- Uso de `secrets` para generación aleatoria
- Validación de entrada robusta
- Manejo seguro del portapapeles
- Logging de eventos críticos

## Contribuir

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/NuevaCaracteristica`)
3. Commit (`git commit -m 'Add: nueva característica'`)
4. Push (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## Licencia

MIT License - Ver `LICENSE` para detalles

## Contacto

Israel Rivera - [@IsraelRiveraSxEc](https://github.com/IsraelRiveraSxEc)

Link del proyecto: [https://github.com/IsraelRiveraSxEc/GenDCCorePy](https://github.com/IsraelRiveraSxEc/GenDCCorePy)
