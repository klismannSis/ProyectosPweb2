from interpreter import draw
from chessPictures import *

# Obtener las representaciones negativas de las figuras
rockN = rock.negative()
knightA = knight.negative()
bishopN = bishop.negative()
queenN = queen.negative()
kingN = king.negative()
pawnN = pawn.negative()
squareN = square.negative()

# Figuras negras en cuadrados claros
rockNsquare = square.under(rockN)
knightAsquare = square.under(knightA)
bishopNsquare = square.under(bishopN)
queenNsquare = square.under(queenN)
kingNsquare = square.under(kingN)

# Figuras negras en cuadrados oscuros
rockNsquareN = squareN.under(rockN)
knightAsquareN = squareN.under(knightA)
bishopNsquareN = squareN.under(bishopN)
pawnNsquareN = squareN.under(pawnN)

# Figuras blancas en cuadrados claros
rockSquare = square.under(rock)
knightSquare = square.under(knight)
bishopSquare = square.under(bishop)
queenSquare = square.under(queen)
kingSquare = square.under(king)
pawnSquare = square.under(pawn)

# Figuras blancas en cuadrados oscuros
rockSquareN = squareN.under(rock)
knightSquareN = squareN.under(knight)
bishopSquareN = squareN.under(bishop)
pawnSquareN = squareN.under(pawn)

# Reyes y reinas en sus respectivos cuadrados
kingNSquare = square.under(kingN)
kingSquareN = squareN.under(king)
queenNSquare = squareN.under(queenN)
queenSquare = square.under(queen)

# Crear las filas del tablero
fila1 = rockNsquare.join(knightAsquareN).join(bishopNsquare).join(queenNSquare).join(kingNSquare).join(bishopNsquareN).join(knightNsquare).join(rockNsquareN)
fila2 = pawnNsquareN.join(pawnNsquare).horizontalRepeat(4)

centro1 = square.join(squareN).horizontalRepeat(4)
centro2 = centro1.verticalMirror()
centro = centro1.up(centro2).verticalRepeat(2)

fila3 = pawnSquare.join(pawnSquareN).horizontalRepeat(4)
fila4 = rockSquareN.join(knightSquare).join(bishopSquareN).join(queenSquare).join(kingSquare).join(bishopSquare).join(knightSquareN).join(rockSquare)

# Dibujar el tablero
tablero = fila1.up(fila2).up(centro).up(fila3).up(fila4)
draw(tablero)
