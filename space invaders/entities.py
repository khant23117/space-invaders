import pygame
class grunt:
    def __init__ (self, health):

        self.health = health
 
       
        
    def damaged (self,x):
       
         self.health = self.health - x
         return self.health
    def get_health(self):
        return self.health
    
       
    
        
    
    def get_visibilit(self):
        return self.visibile
        
        


    def spawn (self,screen, x,y):
        return screen.blit (self.state(1),(x,y))

    def state (self,state):
        if state == 1:
            return pygame.image.load("images\space_invader_grunt.png")
        elif state == 2:
            return pygame.image.load ("images\space_invader_grunt_teleport.png")

        if state == 3:
            return pygame.image.load ("images\grunt_hurt.png")
        
        if state==4:
           return pygame.image.load("images\dead.png")
    
    def attack(self,screen,x,y):
        attack = pygame.image.load("images\grunt_attack.png")
        return screen.blit (attack,(x,y))


        

        




class player:
    def __init__(self, health:int, speed:int, boost: int, melee:int, range:int ):
        self.melee = melee
        self.health = health
        self.range = range
        self.speed = speed
        self.boost = boost

    
    def get_health(self):
        return(self.health)
    
    def get_speed (self):
        return self.speed
    def get_boost(self):
        return self.boost 
    
    def get_range_damage(self):
        return self.range_damage
    
    def get_melee_damage (self):
        return self.melee_damage

    def damage(self,x) :
         self.health = self.health - x
         return self.health
    
    def face (x):
        if x == "left":
            return pygame.image.load("images\playerleft.png")
        if x == "right":
            return pygame.image.load("images\playerright.png")
        if x == "up":
            return pygame.image.load("images\playerup.png")
        if x == "down":
            return pygame.image.load("images\playerdown.png")
    
    def boost(direction):

        if direction == "up":
            return pygame.image.load("images\_boost_up.png")
        if direction == "down":
            return pygame.image.load("images\_boost_down.png")
        if direction == "left":
            return pygame.image.load("images\_boost_left.png")
        if direction == "right":
            return pygame.image.load("images\_boost_right.png")

  
    





    
       