from interpreter import draw
from chessPictures import *

# Obtener la representación negativa del cuadrado y el cuadrado original
square_negative = square.negative()
square_image = square.img

# Concatenar la representación negativa y el cuadrado original para formar una imagen
image = Picture(square_negative.img + square_image)
image_repeated = image.verticalRepeat(2) # Repetir verticalmente la imagen dos veces
image_repeated_negative = image_repeated.negative() # Obtener la representación negativa de la imagen repetida
concatenated_image = image_repeated.join(image_repeated_negative)
final_image = concatenated_image.horizontalRepeat(4)

draw(final_image)
