"""
Módulo de gestión de temas visuales para la aplicación.
Implementa un sistema de temas personalizables con 10 diseños predefinidos.

Autor: Nelson Espinosa
Versión: 1.2.0
"""

from typing import Dict, Any, List
from enum import Enum

class ThemeNames(Enum):
    """
    Enumeración de temas disponibles en la aplicación.
    Cada tema tiene una configuración visual completa.
    """
    CYBERPUNK = "Cyberpunk"
    MIDNIGHT = "Midnight"
    MATRIX = "Matrix"
    SUNSET = "Sunset"
    LIGHT = "Light"
    OCEAN = "Ocean"
    YELLOW = "Yellow"
    AURORA = "Aurora"
    FIRE = "Fire"
    PURGAN = "Purgan"

class ThemeManager:
    """
    Gestor de temas para la interfaz gráfica.
    
    Implementa:
    - Gestión de temas visuales
    - Cambios de tema en tiempo real
    - Configuraciones de color y estilo
    - Validación de temas
    
    Atributos:
        themes (Dict[str, Dict[str, Any]]): Diccionario de configuraciones de temas
        current_theme (str): Nombre del tema actual
    """
    
    def __init__(self):
        """
        Inicializa el gestor de temas con las configuraciones predefinidas.
        Establece el tema por defecto y carga las configuraciones.
        """
        self.themes: Dict[str, Dict[str, Any]] = {
            ThemeNames.CYBERPUNK.value: {
                "bg": "#0A1929",
                "fg": "#00FF41",
                "accent": "#FFD700",
                "font": "Comic Sans MS",
            },
            ThemeNames.MIDNIGHT.value: {
                "bg": "#F3E5F5",
                "fg": "#4A148C",
                "accent": "#9C27B0",
                "font": "Lora",
            },
            ThemeNames.MATRIX.value: {
                "bg": "#0f0117",
                "fg": "#0e6655",
                "accent": "#00cc00",
                "font": "Impact",
            },
            ThemeNames.SUNSET.value: {
                "bg": "#2d1b2d",
                "fg": "#4CAF50",
                "accent": "#ff6600",
                "font": "Nunito",
            },
            ThemeNames.LIGHT.value: {
                "bg": "#ffffff",
                "fg": "#333333",
                "accent": "#007bff",
                "font": "Poppins",
            },
            ThemeNames.OCEAN.value: {
                "bg": "#002b36",
                "fg": "#3e7582",
                "accent": "#268bd2",
                "font": "Merriweather",
            },
            ThemeNames.YELLOW.value: {
                "bg": "#e7e23a",
                "fg": "#4D3D00",
                "accent": "#ff6666",
                "font": "Courier",
            },
            ThemeNames.AURORA.value: {
                "bg": "#1A1A2E",
                "fg": "#5A8589",
                "accent": "#E94560",
                "font": "Orbitron",
            },
            ThemeNames.FIRE.value: {
                "bg": "#2c0703",
                "fg": "#994C30",
                "accent": "#bc3908",
                "font": "Raleway",
            },
            ThemeNames.PURGAN.value: {
                "bg": "#670906",
                "fg": "#d85707",
                "accent": "#2196F3",
                "font": "Blackletter",
            }
        }
        # Cambia el tema predeterminado a LIGHT
        self.default_theme = ThemeNames.MIDNIGHT.value

    def get_theme(self, theme_name: str) -> Dict[str, Any]:
        """
        Obtiene la configuración de un tema específico.
        
        Args:
            theme_name (str): Nombre del tema a obtener
            
        Returns:
            Dict[str, Any]: Configuración completa del tema
            
        Raises:
            ValueError: Si el tema no existe
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
