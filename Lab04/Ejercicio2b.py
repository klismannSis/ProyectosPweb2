from interpreter import draw
from chessPictures import *

# Obtener la representación negativa del knight
knightN = knight.negative()
line1 = knight.join(knightN)
knightN2 = knightN.verticalMirror() # Obtener la versión espejada verticalmente de knightN
line2 = knight.verticalMirror().join(knightN2)
final = line1.up(line2)

draw(final)
