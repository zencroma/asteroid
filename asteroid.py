import pygame
from circleshape import CircleShape
from constant import *
import random
class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self,dt):
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        asteroid_1_vel = self.velocity.rotate(angle)
        asteroid_2_vel = self.velocity.rotate(-angle)
        self.radius -= ASTEROID_MIN_RADIUS
        
        Asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius)
        Asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius)
        Asteroid_1.velocity = asteroid_1_vel * 1.2
        Asteroid_2.velocity = asteroid_2_vel * 1.2
        
        