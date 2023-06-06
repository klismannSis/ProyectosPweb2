from interpreter import draw
from chessPictures import *

# Obtener la representación negativa del cuadrado
square_negative = square.negative()
concatenated = square_negative.join(square)
repeated = concatenated.horizontalRepeat(4)  # Repetir horizontalmente el patrón cuatro veces

draw(repeated)
