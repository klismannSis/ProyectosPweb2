from interpreter import draw
from chessPictures import *

# Obtener la representación negativa del knight
knightA = knight.negative()
line1 = knight.join(knightA)
knightA2 = knightA.verticalMirror() # Obtener la versión espejada verticalmente de knightN
line2 = knight.verticalMirror().join(knightA2)
final = line1.up(line2)

draw(final)
