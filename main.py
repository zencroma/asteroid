import pygame
import sys
from constant import * 
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
def main():
    pygame.init()
    print ("Starting Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    
    updatable  = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    
    AsteroidField.containers = updatable
    Asteroid.containers = (updatable, drawable, asteroids)
    
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable,shots)
    asteroidField = AsteroidField()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        for obj in updatable:
            obj.update(dt)
        for obj in asteroids:
            if player.check_collision(obj):
                print("Game Over!") 
                return 
            for shot in shots:
                if shot.check_collision(obj):
                    shot.kill()
                    obj.split()
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
            
if __name__ == '__main__':
    main()