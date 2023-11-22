import pygame


def render_text(text, font_size, color=(255, 255, 255)):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()

welcome_text, welcome_rect = render_text("Welcome to Text Adventure!", 48)
welcome_rect.center = (screen_width // 2, screen_height // 2)
screen.blit(welcome_text, welcome_rect)