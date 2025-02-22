"""
Módulo principal para la generación de contraseñas seguras.
Implementa la lógica de generación y validación de contraseñas
utilizando el módulo secrets para garantizar la seguridad criptográfica.

Autor: Nelson Espinosa
Versión: 1.2.0
"""

import secrets
import string
import logging
from enum import Enum
from typing import Tuple, Optional

class PasswordStrength(Enum):
    """Enumeración para los niveles de fortaleza de contraseña"""
    WEAK = "Débil"
    MEDIUM = "Media"
    STRONG = "Fuerte"
    VERY_STRONG = "Muy Fuerte"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class PasswordGenerator:
    """
    Clase principal para la generación y evaluación de contraseñas seguras.
    
    Implementa métodos para:
    - Generación de contraseñas criptográficamente seguras
    - Validación de parámetros de entrada
    - Evaluación de fortaleza de contraseñas
    - Logging de operaciones
    
    Atributos:
        lowercase (str): Caracteres en minúscula disponibles
        uppercase (str): Caracteres en mayúscula disponibles
        digits (str): Dígitos disponibles
        special (str): Caracteres especiales disponibles
    """
    
    def __init__(self):
        """
        Inicializa el generador con los conjuntos de caracteres predefinidos
        y configura el sistema de logging.
        """
        self.lowercase = string.ascii_lowercase  # a-z
        self.uppercase = string.ascii_uppercase  # A-Z
        self.digits = string.digits             # 0-9
        self.special = string.punctuation       # !@#$%^&*()_+-=[]{}|;:,.<>?
        
        self._setup_logging()
    
    def _setup_logging(self) -> None:
        """
        Configura el sistema de logging con formato detallado.
        Incluye timestamp, nivel, archivo y número de línea.
        """
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    
    def validate_params(self, length: int, iterations: int) -> bool:
        """
        Valida los parámetros de entrada para la generación de contraseñas.
        
        Args:
            length (int): Longitud deseada de la contraseña (8-129)
            iterations (int): Número de iteraciones máximo (1000-50000)
            
        Returns:
            bool: True si los parámetros son válidos, False en caso contrario
        """
        try:
            return 8 <= length <= 129 and 1000 <= iterations <= 50000
        except (ValueError, TypeError):
            return False
            
    def generate_password(self, length: int, iterations: int, use_lower: bool = True,
                         use_upper: bool = True, use_digits: bool = True,
                         use_special: bool = True) -> tuple[str, PasswordStrength]:
        """
        Genera una contraseña segura con los parámetros especificados.
        
        Args:
            length (int): Longitud deseada de la contraseña
            iterations (int): Número máximo de intentos de generación
            use_lower (bool): Incluir minúsculas
            use_upper (bool): Incluir mayúsculas
            use_digits (bool): Incluir números
            use_special (bool): Incluir caracteres especiales
            
        Returns:
            tuple[str, PasswordStrength]: Contraseña generada y su nivel de fortaleza
            
        Raises:
            ValueError: Si los parámetros no son válidos
        """
        if not self.validate_params(length, iterations):
            logging.error(f"Parámetros inválidos: longitud={length}, iteraciones={iterations}")
            return "", PasswordStrength.WEAK
            
        chars = ""
        if use_lower:
            chars += self.lowercase
        if use_upper:
            chars += self.uppercase
        if use_digits:
            chars += self.digits
        if use_special:
            chars += self.special
            
        if not chars:
            logging.error("No se seleccionaron tipos de caracteres")
            return "", PasswordStrength.WEAK
            
        for _ in range(iterations):
            password = ''.join(secrets.choice(chars) for _ in range(length))
            
            valid = True
            if use_lower and not any(c in self.lowercase for c in password):
                valid = False
            if use_upper and not any(c in self.uppercase for c in password):
                valid = False
            if use_digits and not any(c in self.digits for c in password):
                valid = False
            if use_special and not any(c in self.special for c in password):
                valid = False
                
            if valid:
                strength = self._evaluate_password_strength(password)
                if strength != PasswordStrength.WEAK:
                    logging.info("Contraseña generada exitosamente")
                    return password, strength
        
        logging.warning("No se logró generar una contraseña válida")
        return "", PasswordStrength.WEAK
        
    def _evaluate_password_strength(self, password: str) -> PasswordStrength:
        """
        Evalúa la fortaleza de una contraseña basándose en múltiples criterios.
        
        Criterios:
        - Longitud de la contraseña
        - Variedad de caracteres
        - Complejidad de la combinación
        
        Args:
            password (str): Contraseña a evaluar
            
        Returns:
            PasswordStrength: Nivel de fortaleza de la contraseña
        """
        score = 0
        length = len(password)
        
        has_lower = any(c in self.lowercase for c in password)
        has_upper = any(c in self.uppercase for c in password)
        has_digit = any(c in self.digits for c in password)
        has_special = any(c in self.special for c in password)
        
        char_types = sum([has_lower, has_upper, has_digit, has_special])
        score += char_types
        
        if length >= 16:
            score += 2
        elif length >= 12:
            score += 1
            
        if length <= 8:
            return PasswordStrength.WEAK if char_types < 2 else PasswordStrength.MEDIUM
        elif length <= 12:
            if char_types < 2:
                return PasswordStrength.WEAK
            elif char_types < 3:
                return PasswordStrength.MEDIUM
            return PasswordStrength.STRONG
        else:
            if char_types < 2:
                return PasswordStrength.WEAK
            elif char_types < 3:
                return PasswordStrength.MEDIUM
            elif char_types < 4:
                return PasswordStrength.STRONG
            return PasswordStrength.VERY_STRONG
