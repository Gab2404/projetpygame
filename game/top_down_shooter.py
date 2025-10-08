import pygame
from sys import exit
import math
from settings import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top Down Shooter")
clock = pygame.time.Clock()

background = pygame.transform.scale(pygame.image.load("game/background/sasakeyo.png").convert(), (WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)
        self.image = pygame.transform.rotozoom(
            pygame.image.load("game/player/0.png").convert_alpha(), 0, PLAYER_SIZE)
        self.base_player_image = self.image
        self.hitbox_rect = self.image.get_rect(center = self.pos)
        self.rect = self.hitbox_rect.copy()
        self.speed = PLAYER_SPEED
        self.velocity_x = 0
        self.velocity_y = 0

    def player_rotation(self):
        self.mouse_cord = pygame.mouse.get_pos()
        self.x_change_mouse_player = (self.mouse_cord[0] - self.hitbox_rect.x)
        self.y_change_mouse_player = (self.mouse_cord[1] - self.hitbox_rect.y)
        self.angle = math.degrees(math.atan2(self.y_change_mouse_player, self.x_change_mouse_player))
        self.image = pygame.transform.rotate(self.base_player_image, -self.angle)
        selfrect = self.image.get_rect(center=self.hitbox_rect.center)
    
    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            self.velocity_y = -self.speed  # vers le haut
        if keys[pygame.K_s]:
            self.velocity_y = self.speed   # vers le bas
        if keys[pygame.K_d]:
            self.velocity_x = self.speed   # droite
        if keys[pygame.K_q]:
            self.velocity_x = -self.speed  # gauche

        if self.velocity_x != 0 and self.velocity_y != 0:
            self.velocity_x /= math.sqrt(2)
            self.velocity_y /= math.sqrt(2)

    def move(self):
        self.pos += pygame.math.Vector2(self.velocity_x, self.velocity_y)

    def update(self):
        self.user_input()
        self.move()

player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))
    player.update()
    screen.blit(player.image, player.pos)

    pygame.display.update()
    clock.tick(FPS)
