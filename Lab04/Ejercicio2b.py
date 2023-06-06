from interpreter import draw
from chessPictures import *

caballo = Picture(...)  # Aquí se proporcionar la imagen adecuada

caballo1 = caballo .negative()# Obtenemos la imagen negativa de 'caballo'
line1 = caballo .join(caballo1)

caballo2 = caballo1.verticalMirror()# Se obtener el reflejo vertical de 'caballo1'
line2 = caballo2 .join(caballo .verticalMirror())

final = line1.up(line2) # Combinar verticalmente 'line1' y 'line2'
draw(final)
