#direction dictionary, key is direction, and value is list of amendments to coords (x,y)
# 0,0 coords are top left
#assume field is 50x50

import pygame

# pygame setup
#0 is North, going clockwise 45 degrees each facing



pygame.init()
game_plane = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Tanks go pew pew!')
clock = pygame.time.Clock()
running = True
dt = 0


move_directions = {
    '0' : [0 , -1, 0],
    '1' : [1 , -1, -45],
    '2' : [1 , 0, -90],
    '3' : [1 , 1, -135],
    '4' : [0 , 1, 180],
    '5' : [-1 , 1, 135],
    '6' : [-1 , 0, 90],
    '7' : [-1 , -1, 45]}


class Tank():

    def __init__(self, side = "blue", model = "light", status = "intact", facing = "0",
                location = pygame.Vector2(game_plane.get_width() / 2, game_plane.get_height() / 2), sprite_path = "placeholder.png"):
        self.side = side
        self.model = model
        self.status = status
        self.facing = facing
        self.location = location
        self.sprite_path = sprite_path
        self.sprite_surface = pygame.image.load(self.sprite_path)
        self.sprite_on_field = pygame.transform.rotate(self.sprite_surface, 0)
        # self.sprite_on_field = pygame.transform.rotate(self.sprite_on_field, 45) use if I want to turn the tank at init

    def turn(self, turn_direction):
            
        self.facing = int(self.facing)
        if turn_direction == 'L':
            self.facing -= 1
            if self.facing < 0:
                self.facing = 7
        if turn_direction == 'R':
            self.facing += 1
            if self.facing > 7:
                self.facing = 0
        self.sprite_on_field = pygame.transform.rotate(self.sprite_surface, move_directions[str(self.facing)][2])

    def drive(self, direction):
        self.location[0] += 5*move_directions[direction][0]
        self.location[1] += 5*move_directions[direction][1]
        
    def fire_main_gun(self):
        projectile = Projectile(self.facing)
        projectile_object_list.append(projectile) 


class Projectile():
    def __init__(self, facing, location = (50,50), velocity_multiplier = 10, sprite_path = "placeholder.png"):
        self.facing = facing
        self.location = location
        self.velocity_multiplier = velocity_multiplier
        self.sprite_path = sprite_path
        self.sprite_surface = pygame.image.load(self.sprite_path)
        self.sprite_on_field = pygame.transform.scale_by(self.sprite_surface, 1/10)
    
    def fly(self, facing):
        self.location[0] += self.velocity_multiplier*move_directions[facing][0]
        self.location[1] += self.velocity_multiplier*move_directions[facing][1]

def event_queue_execute ():
    for i in range(0, len(projectile_object_list)-1):
        projectile_object_list[i].fly


my_tank = Tank()

# tank_object_list = () for when there are more tanks


projectile_object_list = []




while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the game_plane with a color to wipe away anything from last frame
        game_plane.fill("chartreuse4")
        game_plane.blit(my_tank.sprite_on_field, my_tank.location)
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            my_tank.drive(str(my_tank.facing))
            my_tank.fire_main_gun()
            

        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_a:
                my_tank.turn('L')
              

            if event.key == pygame.K_d:
                my_tank.turn('R')
                
        game_plane.blit(my_tank.sprite_on_field, my_tank.location)

    pygame.display.flip() 


    # flip() the display to put your work on game_plane


    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
dt = clock.tick(60) / 1000

pygame.quit()