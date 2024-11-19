import pygame
import sys


class PygameDisplay:
    def __init__(self, win_size, game_manager):
        self.gm = game_manager

        self.board = game_manager.board
        self.window_size = 1000
        self.board_size = game_manager.board.size
        self.square_size = win_size / game_manager.size
        self.colors = [(255, 0, 0), (0, 0, 0)]

        pygame.init()
        self.screen = pygame.display.set_mode((win_size, win_size))

    def draw_board(self):
        s = self.board.size
        for row in range(s):
            for col in range(s):
                if self.board.fields[row * s + col].alive:
                    c = self.colors[0]
                else:
                    c = self.colors[1]
                x = col * self.square_size
                y = row * self.square_size
                pygame.draw.rect(self.screen, c, (x, y, self.square_size, self.square_size))

    def run(self):
        paused = True
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = not paused
                    if event.key == pygame.K_k:
                        if paused:
                            self.gm.do_moves()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    col = int(mouse_x // self.square_size)
                    row = int(mouse_y // self.square_size)
                    field = self.board.fields[row * self.board_size + col]
                    field.set_alive(not field.alive)



            if not paused:
                self.gm.do_moves()

            #pygame.time.delay(50)
            clock.tick(60)

            self.screen.fill((0, 0, 0))
            self.draw_board()
            pygame.display.flip()





