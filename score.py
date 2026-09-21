import pygame


class Score():
    def __init__(self, screen:pygame.Surface, font_size, font_type):
        self.font = pygame.font.Font(font_type,font_size)
        self.score = 0
        self.screen = screen

    def show_score(self):
        score_text = self.font.render(str(self.score),True,(255,255,255))
        self.screen.blit(score_text,(10,10))
