from interpreter import draw
from chessPictures import *

knightP = knight.negative()
line1 = knight.join(knightP)

line2 = knightP.join(knight)
final = line1.up(line2)
draw(final)