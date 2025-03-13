import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, 'containers'):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    def draw(self):
        pass
    def update(self):
        pass
    def check_collision(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius