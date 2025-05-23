import pygame
import sys 

from const import *
from game import Game


class Main: 
    
    # called first when create main object
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) ) # create screen 
        pygame.display.set_caption('Chess')
        self.game = Game()
    
    
    def mainloop(self):
        
        screen = self.screen
        game = self.game 
        board = self.game.board
        dragger = self.game.dragger


        # loop through all events 
        while True: 
            game.show_background(screen)
            game.show_pieces(screen)

            if dragger.dragging: 
                dragger.update_blit(screen)

            for event in pygame.event.get():

                # click event 
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    dragger.update_mouse(event.pos)
                    print(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    # test output
                    print(dragger.mouseY, clicked_row)
                    print(dragger.mouseX, clicked_col)

                    # if clicked square has a piece
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                # mouse motion
                elif event.type == pygame.MOUSEMOTION: 
                    if dragger.dragging: 
                        dragger.update_mouse(event.pos)
                        game.show_background(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)

                # click release 
                elif event.type == pygame.MOUSEBUTTONUP: 
                    dragger.undrag_piece()
                        
                # quit application
                elif event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()


            pygame.display.update()


main = Main()
main.mainloop()