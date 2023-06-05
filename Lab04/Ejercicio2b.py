from interpreter import draw
from chessPictures import *

knight = Picture(...)  # Aquí se proporcionar la imagen adecuada

knightP = knight.negative()# Obtenemos la imagen negativa de 'knight'
line1 = knight.join(knightP)

knightP2 = knightP.verticalMirror()# Se obtener el reflejo vertical de 'knightP'
line2 = knightP2.join(knight.verticalMirror())

final = line1.up(line2) # Combinar verticalmente 'line1' y 'line2'
draw(final)
