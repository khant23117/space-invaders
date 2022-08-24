
from pickle import TRUE
import pygame
import random
import math
import entities
import time







#initialize pygame
pygame.init()

#create screen

screen = pygame.display.set_mode((640,640))

#background 
background = pygame.image.load("images\_background_space.png")

#title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load ("images\space_invader_grunt.png")

pygame.display.set_icon(icon)

# player
health = 10
speed = 5
boost = 3
melee = 5
range = 5
player1 = entities.player  (health,  speed, boost,  melee ,  range)
#player spawn
player_state = entities.player.face("up")
#initial spawn player
drift = 0
player_x= 300 
player_y = 570
movex = 0
movey= 0

#initial spawn enemy
enemy1 = entities.grunt (1000)
enemy_x = 300
enemy_y = 50
path_x = enemy_x - player_x
path_y = enemy_y - player_y

def call_player(player_state,x,y):
    screen.blit(player_state,(x,y))

def call_enemy(enemy_state,x,y):
    screen.blit(enemy_state,(x,y))




damage = False

#game loop
running = True
while running:

    enemy1.spawn(screen,enemy_x,enemy_y)
    
    for event in pygame.event.get():
        
        
        #exit condition
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN :
            #movement x axis
            if event.key == pygame.K_LEFT:
                player_state = entities.player.face("left")
                movex = -speed
            if pygame.key.get_pressed()[pygame.K_LEFT] and pygame.key.get_pressed()[pygame.K_SPACE]:
                player_state = entities.player.boost("left")
                movex= -boost *speed
                damage = True
            
                

                

                
            if event.key == pygame.K_RIGHT:
                player_state = entities.player.face("right")
                movex = speed
            if pygame.key.get_pressed()[pygame.K_RIGHT] and pygame.key.get_pressed()[pygame.K_SPACE]:
                player_state = entities.player.boost("right")
                movex = boost *speed
                damage = True
                
            #movement y axis

            if event.key == pygame.K_UP:
                player_state = entities.player.face("up")
                movey = -speed

            if pygame.key.get_pressed()[pygame.K_UP] and pygame.key.get_pressed()[pygame.K_SPACE]:
                player_state = entities.player.boost("up")
                movey = -boost *speed
                damage = True

            if event.key == pygame.K_DOWN:
                player_state =  entities.player.face("down")    

                movey = speed
            if pygame.key.get_pressed()[pygame.K_DOWN] and pygame.key.get_pressed()[pygame.K_SPACE]:
                    player_state = entities.player.boost("down")
                    movey = boost *speed
                    damage = True
            
            
                


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                movex = -0.5
                movey=0  
            
            if event.key == pygame.K_UP:
                
                movey = -0.5
                movex=0
                
            if event.key == pygame.K_RIGHT:

                movex = 0.5
                movey=0

            if event.key == pygame.K_DOWN:
                movey = 0.5
                movex=0
            
            

            

            

        
       
      
    
   
        
    
    distance =math.sqrt( ((enemy_x - player_x)**2) + ((enemy_y - player_y)**2))

    
    if distance >= 350:

        enemy = enemy1.state(2) 

        
            
        

        if distance >=400:
            
            
            enemy_x = player_x - 50
            enemy_y = player_y - 50 
           
            

    else : 
        enemy = enemy1.state(1)


    # damage condition
    if distance <= 60 and damage:
        
        enemy1.damaged(melee)
        enemy = enemy1.state(3)
        print(enemy1.health)

    if enemy1.get_health() <= 0:
        enemy = enemy1.state(4)

            
            
        
    



    
       
                
                
               

                

# ===================================       Boundaries`    =================================
                
    if player_x <= 0:
        player_x = 0
    if player_x >= 580:
        player_x =580
    
    if player_y <= 0:
        player_y = 0 
    if player_y >= 570:
        player_y =570

    
    if enemy_x <= 0:
        enemy_x = 0
    if enemy_x >= 580:
        enemy_x =580
    
    if enemy_y <= 0:
        enemy_y = 0
    if enemy_y >= 570:
        enemy_y =570

    # ==============================    Boundaries      =============================
    player_x += movex
    player_y +=movey
    screen.fill((100,50,100))

    screen.blit (background,(0,0))
        
    call_player(player_state,player_x,player_y)
    call_enemy (enemy,enemy_x,enemy_y)
    enemy1.attack(screen,path_x,path_y)
    pygame.display.update()



pygame.quit()
