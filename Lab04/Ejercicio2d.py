from interpreter import draw
from chessPictures import *

square_negative = square.negative()
square_concatenated = square.join(square_negative) #crea una nueva cadena o estructura que combina las representaciones gráficas de square y square_negative.
final = square_concatenated.horizontalRepeat(4)
draw(final)