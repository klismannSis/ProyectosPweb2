from interpreter import draw
from chessPictures import *

#Creamos varias variables para almacenar el resultado de concatenar la cadena "queen" en diferentes momentos.
queen_times_1 = queen
queen_times_2 = queen_times_1 + queen_times_1
queen_times_3 = queen_times_2 + queen_times_1
queen_times_4 = queen_times_3 + queen_times_1

final = queen_times_4
draw(final)
