"""
Módulo de generación de contraseñas seguras.
Implementa algoritmos criptográficamente seguros y validación multinivel.
"""

import secrets  # Para generación de números aleatorios criptográficamente seguros
import string   # Constantes de caracteres ASCII
import logging  # Sistema de registro de eventos
from enum import Enum
from typing import Tuple, Optional

# Definición de niveles de fortaleza para las contraseñas
class PasswordStrength(Enum):
    WEAK = "Débil"         # Contraseña con score <= 2
    MEDIUM = "Media"       # Contraseña con score <= 3
    STRONG = "Fuerte"      # Contraseña con score <= 4
    VERY_STRONG = "Muy Fuerte"  # Contraseña con score > 4

# Configuración básica del sistema de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class PasswordGenerator:
    """Clase principal para la generación y evaluación de contraseñas seguras"""
    
    def __init__(self):
        """
        Inicializa conjuntos de caracteres y configura logging.
        Los conjuntos se mantienen separados para mejor control y validación.
        """
        # Conjuntos de caracteres disponibles
        self.lowercase = string.ascii_lowercase  # a-z
        self.uppercase = string.ascii_uppercase  # A-Z
        self.digits = string.digits             # 0-9
        self.special = string.punctuation       # !@#$%^&*()_+-=[]{}|;:,.<>?
        
        # Configuración de logging
        self._setup_logging()
    
    def _setup_logging(self) -> None:
        """Configura el sistema de logging con formato detallado"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    
    def validate_params(self, length: int, iterations: int) -> bool:
        """
        Valida que los parámetros de entrada estén dentro de rangos seguros
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
            length: Longitud deseada de la contraseña
            iterations: Número máximo de intentos de generación
            use_lower: Incluir minúsculas
            use_upper: Incluir mayúsculas
            use_digits: Incluir números
            use_special: Incluir caracteres especiales
            
        Returns:
            Tuple[str, PasswordStrength]: Contraseña generada y su nivel de fortaleza
        """
        # Validación inicial de parámetros
        if not self.validate_params(length, iterations):
            logging.error(f"Parámetros inválidos: longitud={length}, iteraciones={iterations}")
            return "", PasswordStrength.WEAK
            
        # Construir el conjunto de caracteres según las opciones
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
            
        # Intentamos generar una contraseña que cumpla los requisitos
        for _ in range(iterations):
            password = ''.join(secrets.choice(chars) for _ in range(length))
            
            # Verificar que la contraseña contenga al menos un carácter de cada tipo seleccionado
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
        """Evalúa la fortaleza de la contraseña"""
        score = 0
        length = len(password)
        
        # Criterios de caracteres
        has_lower = any(c in self.lowercase for c in password)
        has_upper = any(c in self.uppercase for c in password)
        has_digit = any(c in self.digits for c in password)
        has_special = any(c in self.special for c in password)
        
        # Puntuación base por tipos de caracteres
        char_types = sum([has_lower, has_upper, has_digit, has_special])
        score += char_types
        
        # Puntuación adicional por longitud
        if length >= 16:
            score += 2
        elif length >= 12:
            score += 1
            
        # Determinar fortaleza final
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
