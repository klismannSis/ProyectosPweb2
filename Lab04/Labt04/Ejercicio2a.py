from interpreter import draw
from chessPictures import *

knight_negative = knight.negative()
line1 = "".join([knight, knight_negative])

line2 = "".join([knight_negative, knight])
final = line1.up(line2)

draw(final)




