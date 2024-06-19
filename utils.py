import pygame

GAME_SIZE = 640, 360

class Utils:
    scaled_screen_rect = None

    def norm_cursor_pos():
        rect = Utils.scaled_screen_rect
        mx, my = pygame.mouse.get_pos()
        dx = mx - rect.left
        dy = my - rect.top
        mouse_norm_x = dx * GAME_SIZE[0] / rect.width
        mouse_norm_y = dy * GAME_SIZE[1] / rect.height

        return mouse_norm_x, mouse_norm_y
