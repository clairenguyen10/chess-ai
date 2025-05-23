import pygame  

from const import *
from board import Board
from dragger import Dragger

class Game: 
    
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
    

    # blit methods
  
    def show_background(self, surface):
        for row in range(ROWS): 
            for col in range(COLS): 
                if (row + col) % 2 == 0:
                  colour = (255, 237, 243) # light pink
                else: 
                  colour = (255, 99, 151) # dark pink 

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, colour, rect)
                
    def show_pieces(self, surface): 
       for row in range(ROWS):                             
          for col in range(COLS): 
             # piece?
             if self.board.squares[row][col].has_piece():
                piece = self.board.squares[row][col].piece

                # all pieces except dragger piece
                if piece is not self.dragger.piece: 
                    piece.set_texture()
                    img = pygame.image.load(piece.texture)
                    img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)

    
    def show_moves(self, surface): 
       if self.dragger.dragging: 
          piece = self.dragger.piece 
          
          # loop all valid moves 
          for move in piece.moves: 
             # colour 
             colour = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'
             # rect
             rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
             # blit
             pygame.draw.rect(surface, colour, rect)

