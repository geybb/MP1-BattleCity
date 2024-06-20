import pyxel
from functions import boundingBox

class Block:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
    
    def update(self):
        pass
    def draw(self):
        pass

class Brick(Block):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 20
        self.type = 'brick'
    
    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 16, self.height, self.width)

class crackedBrick(Block):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 20
        self.type = 'cracked_brick'

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 16, self.height, self.width)

class Water(Block):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'water'

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 32, self.height, self.width)

class Forest(Block):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'forest'
    
    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 0, self.height, self.width, 0)

class Stone(Block):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'stone'
    
    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, self.height, self.width)

class Home(Block):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.health = 20
        self.type = 'home'
        self.u = 0
        self.v = 48
    
    def update(self):
        if self.health == 0:
            self.u = 16
            self.v = 48

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.u, self.v, self.height, self.width, 0)

class Mirror(Block):

    def __init__(self, x, y, orientation):
        super().__init__(x, y)
        self.type = 'mirror'
        self.orientation = orientation # 0 = positive slope, 1 = negative slope
        self.pixels = []
        self.bulletsCollided = []
        if self.orientation == 0:
            self.pixels = [(self.x, self.y + self.width + i) for i in range(self.height)]
            self.u = 0
            self.v = 64
        if self.orientation == 1:
            self.u = 16
            self.v = 64

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.u, self.v, self.height, self.width, 0)

class enemySpawn(Block):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.type = 'enemySpawn'
        self.u = 0
        self.v = 16

    def update(self):
        if pyxel.frame_count % 60 == 0:
            self.u, self.v = 0, 16
        elif pyxel.frame_count % 30 == 0:
            self.u, self.v = 16, 16
        elif pyxel.frame_count % 15 == 0:
            self.u, self.v = 32, 16
        elif pyxel.frame_count % 5 == 0:
            self.u, self.v = 48, 16

    def draw(self):
        pyxel.blt(self.x, self.y, 2, self.u, self.v, self.height, self.width, 0)
