"""
Módulo de gestión de temas visuales.
Implementa un sistema flexible de temas con soporte para personalización.
"""

from typing import Dict, Any, List
from enum import Enum

class ThemeNames(Enum):
    """
    Enumeración de temas disponibles en la aplicación.
    Cada tema tiene una configuración visual completa.
    """
    CYBERPUNK = "Cyberpunk"  # Tema futurista con neón
    MIDNIGHT = "Midnight"     # Tema oscuro profesional
    MATRIX = "Matrix"         # Tema inspirado en Matrix
    SUNSET = "Sunset"        # Tema cálido y suave
    LIGHT = "Light"          # Tema claro estándar

class ThemeManager:
    """
    Gestor de temas para la interfaz gráfica.
    Maneja la configuración visual y cambios de tema en tiempo real.
    """
    
    def __init__(self):
        """Inicializa el gestor de temas con las configuraciones predefinidas"""
        self.themes: Dict[str, Dict[str, Any]] = {
            ThemeNames.CYBERPUNK.value: {
                "bg": "#1e1e1e",        # Fondo principal
                "fg": "#00ff00",        # Texto principal
                "button_bg": "#333333", # Fondo de botones
                "accent": "#00ffff",    # Color de acento
                "font": "Helvetica",    # Fuente principal
                "description": "Tema futurista con tonos neón"
            },
            ThemeNames.MIDNIGHT.value: {
                "bg": "#000033",
                "fg": "#4d4dff",
                "button_bg": "#000066",
                "accent": "#0000ff",
                "font": "Helvetica",
                "description": "Tema oscuro con tonos azules profundos"
            },
            ThemeNames.MATRIX.value: {
                "bg": "#000000",
                "fg": "#00ff00",
                "button_bg": "#003300",
                "accent": "#00cc00",
                "font": "Courier",
                "description": "Tema inspirado en Matrix"
            },
            ThemeNames.SUNSET.value: {
                "bg": "#2d1b2d",
                "fg": "#ff9966",
                "button_bg": "#4d2e4d",
                "accent": "#ff6600",
                "font": "Helvetica",
                "description": "Tema cálido con tonos atardecer"
            },
            ThemeNames.LIGHT.value: {
                "bg": "#ffffff",           # Fondo blanco
                "fg": "#333333",           # Texto gris oscuro
                "button_bg": "#f0f0f0",    # Botones gris muy claro
                "accent": "#007bff",       # Acento azul moderno
                "font": "Helvetica",
                "description": "Tema claro y minimalista"
            }
        }
        self.default_theme = ThemeNames.CYBERPUNK.value

    def get_theme(self, theme_name: str) -> Dict[str, Any]:
        """
        Obtiene la configuración de un tema específico
        
        Args:
            theme_name: Nombre del tema a obtener
            
        Returns:
            Diccionario con la configuración del tema
        """
        return self.themes.get(theme_name, self.themes[self.default_theme])

    def get_theme_names(self) -> list[str]:
        """
        Obtiene la lista de nombres de temas disponibles
        
        Returns:
            Lista de nombres de temas
        """
        return list(self.themes.keys())

    def get_default_theme(self) -> str:
        """
        Obtiene el nombre del tema por defecto
        
        Returns:
            Nombre del tema por defecto
        """
        return self.default_theme

    def get_strength_color(self, strength: str, current_theme: str) -> str:
        """
        Obtiene el color correspondiente al nivel de fortaleza de la contraseña
        
        Args:
            strength: Nivel de fortaleza ('Débil', 'Media', 'Fuerte', 'Muy Fuerte')
            current_theme: Nombre del tema actual
            
        Returns:
            Código de color hexadecimal
        """
        # Los colores de fortaleza son consistentes en todos los temas
        if "Débil" in strength:
            return "#ff0000"  # Rojo
        elif "Media" in strength:
            return "#ffff00"  # Amarillo
        elif "Fuerte" in strength:
            return "#00ff00"  # Verde
        else:
            return self.themes[current_theme]["accent"]  # Color de acento del tema
