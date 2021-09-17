import pygame

class sword1:
    def __init__(self):
        self.lastAttack = 0
        self.attackDelay = 20
        self.damage = 10
        self.atkVariance = 2

    def action(self, player):
        self.player = player
        now = pygame.time.get_ticks()
        if now - self.lastAttack >= self.player.stats.atkSpeed+self.attackDelay:
            self.player.animations.setMode('hit')
            self.lastAttack = now