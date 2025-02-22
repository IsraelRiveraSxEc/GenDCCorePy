import secrets
import string
import logging
from enum import Enum
from typing import Tuple, Optional

class PasswordStrength(Enum):
    WEAK = "Débil"
    MEDIUM = "Media"
    STRONG = "Fuerte"
    VERY_STRONG = "Muy Fuerte"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class PasswordGenerator:
    """Clase principal para la generación y evaluación de contraseñas seguras"""
    
    def __init__(self):
        self.lowercase = string.ascii_lowercase  # a-z
        self.uppercase = string.ascii_uppercase  # A-Z
        self.digits = string.digits             # 0-9
        self.special = string.punctuation       # !@#$%^&*()_+-=[]{}|;:,.<>?
        
        self._setup_logging()
    
    def _setup_logging(self) -> None:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    
    def validate_params(self, length: int, iterations: int) -> bool:
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
        """Evalúa la fortaleza de la contraseña"""
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