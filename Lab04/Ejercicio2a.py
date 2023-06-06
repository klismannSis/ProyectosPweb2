from interpreter import draw
from chessPictures import *

caballo1 = knight.negative()
line1 = knight.join(caballo1)

line2 = caballo1.join(knight)
final = line1.up(line2)
draw(final)