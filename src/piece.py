import os


class Piece: 
    
    def __init__(self, name, colour, value, texture=None, texture_rect=None):
        self.name = name
        self.colour = colour 
        value_sign = 1 if colour == 'white' else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self, size=80): 
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.colour}_{self.name}.png')
    
    def add_move(self, move): 
        self.moves.append(move)
    

  
class Pawn(Piece):
    
    def __init__(self, colour): 
        # self.dir = -1 if colour == 'white' else 1
        if colour == 'white': 
            self.dir = -1
        else: 
            self.dir = 1
        super().__init__('pawn', colour, 1.0)


class Knight(Piece):
    
    def __init__(self, colour): 
        super().__init__('knight', colour, 3.0)


class Bishop(Piece):
    
    def __init__(self, colour): 
        super().__init__('bishop', colour, 3.001)


class Rook(Piece):
    
    def __init__(self, colour): 
        super().__init__('rook', colour, 5.0)
      

class Queen(Piece):
    
    def __init__(self, colour): 
        super().__init__('queen', colour, 9.0)


class King(Piece):
    
    def __init__(self, colour): 
        super().__init__('king', colour, 10000.0)