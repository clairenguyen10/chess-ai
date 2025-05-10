from const import *
from square import Square
from piece import *

class Board: 
    
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]  # create 2D array of 8 0's for each column 

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')


    def _create(self): 
      for row in range(ROWS): 
        for col in range(COLS): 
          self.squares[row][col] = Square(row, col)  # looping the array to replace 0's with squares


    def _add_pieces(self, colour):
      if colour == 'white': 
        row_pawn, row_other = (6, 7)
      else: 
        row_pawn, row_other = (1, 0)
      # condensed version: row_pawn, row_other = (6, 7) if colour == 'white' else (1, 0)

      # pawns
      for col in range(COLS): 
         self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(colour))

      # knights 
      self.squares[row_other][1] = Square(row_other, 1, Knight(colour))
      self.squares[row_other][6] = Square(row_other, 1, Knight(colour))

      # bishops 
      self.squares[row_other][2] = Square(row_other, 2, Bishop(colour))
      self.squares[row_other][5] = Square(row_other, 5, Bishop(colour))

      # rooks 
      self.squares[row_other][0] = Square(row_other, 0, Rook(colour))
      self.squares[row_other][7] = Square(row_other, 7, Rook(colour))

      # queen 
      self.squares[row_other][3] = Square(row_other, 3, Queen(colour))

      # king
      self.squares[row_other][4] = Square(row_other, 4, King(colour))

