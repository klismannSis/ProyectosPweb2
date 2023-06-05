from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])
    return Picture(vertical) 

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = []
    for row in self.img: """Permite obtener una versión reflejada horizontalmente de una imagen."""
    horizontal.insert(0, row)
    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative = [
      ''.join(self._invColor(char) for char in value)
    for value in self.img
    ]
    return Picture(negative)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    join = []  
    """Almacenará las filas combinadas de las dos imágenes."""
    for i in range(len(self.img)):
      join.append(self.img[i] + "" + p.img[i])  
    return Picture(join)
"""Permite combinar verticalmente dos imágenes, apilando una encima de la otra."""
def up(self, p):
  image = self.img + p.img
  return Picture(image)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    image = []
    for i in range(len(self.img)):
      line = ""   """almacenará la fila combinada."""
      for j in range(self.img[i]):
        if p.img[i][j] != " ":  
          line += p.img[i][j]
        else:
          line += self.img[i][j]
      image.append(line)
    return Picture(image)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    image = []
    for i in range(0,len(self.img)):
        image.append(self.img[i] * n)
    return Picture(image)

  def verticalRepeat(self, n):
    image = self.img * n       
    """permite repetir verticalmente la imagen actual"""
    return Picture(image)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

