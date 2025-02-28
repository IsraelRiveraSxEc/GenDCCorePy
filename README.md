# Generador de Contraseñas NEIR

Una aplicación de escritorio segura y optimizada para generar contraseñas aleatorias con interfaz gráfica.

## Antecedentes

En la era digital actual, la seguridad de nuestras cuentas en línea es más crítica que nunca. Las contraseñas débiles o reutilizadas son la principal causa de vulnerabilidades en la seguridad digital personal. Este proyecto nace de la necesidad de proporcionar una herramienta accesible y confiable para la generación de contraseñas seguras.

## Objetivo

Desarrollar una aplicación de escritorio que permita a usuarios de todos los niveles técnicos generar contraseñas seguras, implementando las mejores prácticas de seguridad y una interfaz intuitiva que eduque sobre la importancia de la seguridad digital.

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

## Desarrollo

El proyecto se desarrolló siguiendo un enfoque centrado en la seguridad y usabilidad:

1. **Fase de Investigación**
   - Análisis de mejores prácticas de seguridad
   - Estudio de patrones de diseño UI/UX
   - Evaluación de tecnologías disponibles

2. **Fase de Implementación**
   - Desarrollo del core criptográfico
   - Diseño de interfaz responsiva
   - Implementación de sistema de temas
   - Integración de validaciones en tiempo real

3. **Fase de Pruebas**
   - Validación de seguridad
   - Pruebas de usabilidad
   - Optimización de rendimiento

## Problemas Enfrentados

1. **Seguridad vs Usabilidad**
   - Equilibrar la complejidad de las contraseñas con la facilidad de uso
   - Implementar validaciones sin frustrar al usuario

2. **Rendimiento**
   - Optimizar el proceso de generación para grandes iteraciones
   - Mantener la responsividad de la interfaz

3. **Compatibilidad**
   - Asegurar funcionamiento en diferentes versiones de Windows
   - Manejar diferentes configuraciones de sistema

## Resolución de Problemas

1. **Mejoras de Seguridad**
   - Implementación de módulo `secrets` para aleatoriedad criptográfica
   - Sistema de validación multinivel
   - Retroalimentación visual inmediata

2. **Optimizaciones**
   - Procesamiento asíncrono para operaciones pesadas
   - Caché de temas visuales
   - Validación en tiempo real optimizada

3. **Compatibilidad**
   - Pruebas exhaustivas en diferentes entornos
   - Sistema de logging detallado
   - Manejo robusto de errores

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

## Conclusión

El Generador de Contraseñas NEIR representa un paso significativo hacia la democratización de la seguridad digital. A través de su desarrollo, hemos demostrado que es posible crear herramientas de seguridad que sean tanto robustas como accesibles para usuarios no técnicos.

## Reflexión Final

En un mundo donde la seguridad digital es cada vez más crucial, debemos preguntarnos: ¿Estamos haciendo lo suficiente para proteger nuestra información? Este proyecto no es solo una herramienta, es una invitación a reflexionar sobre nuestros hábitos digitales y a tomar acción para mejorar nuestra seguridad en línea.

¿Cuándo fue la última vez que actualizaste tus contraseñas? ¿Estás utilizando contraseñas lo suficientemente seguras? La seguridad digital no es solo una responsabilidad personal, es un compromiso colectivo que nos afecta a todos.

## Licencia

MIT License - Ver `LICENSE` para detalles

## Contacto

Nelson Espinosa Ec: 0961705423
[Repositorio del Proyecto](https://github.com/IsraelRiveraSxEc/GenDCCorePy)
