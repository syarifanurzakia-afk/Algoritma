#Nama Sy Nur Zakia Tau
#Kelas A Sistem Informasi 
#Nim D0425330
#Tugas Algoritma 

import pygame
import sys
import time
import math

pygame.init()


WIDTH, HEIGHT = 360, 360
CELL = WIDTH // 3

BG_COLOR = (240, 240, 245)
LINE_COLOR = (180, 180, 190)
X_COLOR = (235, 75, 75)
O_COLOR = (60, 120, 230)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


class Board:
    def __init__(self):
        self.grid = [[0] * 3 for _ in range(3)]
        self.current = 1
        self.winner_line = None  # Menyimpan posisi garis menang

    def reset(self):
        self.grid = [[0] * 3 for _ in range(3)]
        self.current = 1
        self.winner_line = None

    def mark(self, row, col):
        if self.grid[row][col] == 0:
            self.grid[row][col] = self.current
            self.current = 2 if self.current == 1 else 1
            return True
        return False

    def check_winner(self):
        g = self.grid

        # Baris
        for r in range(3):
            if g[r][0] == g[r][1] == g[r][2] != 0:
                self.winner_line = ("row", r)
                return g[r][0]

        # Kolom
        for c in range(3):
            if g[0][c] == g[1][c] == g[2][c] != 0:
                self.winner_line = ("col", c)
                return g[0][c]

        # Diagonal
        if g[0][0] == g[1][1] == g[2][2] != 0:
            self.winner_line = ("diag", 0)
            return g[0][0]
        if g[0][2] == g[1][1] == g[2][0] != 0:
            self.winner_line = ("diag", 1)
            return g[0][2]

        return 0

    def full(self):
        return all(all(cell != 0 for cell in row) for row in self.grid)


board = Board()


# Papan

def draw_board():
    screen.fill(BG_COLOR)
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, CELL * i), (WIDTH, CELL * i), 3)
        pygame.draw.line(screen, LINE_COLOR, (CELL * i, 0), (CELL * i, HEIGHT), 3)


def animate_mark(x, y, player):
    steps = 15
    for t in range(steps + 1):
        draw_board()
        draw_marks(except_pos=(x, y))
        progress = t / steps

        if player == 1:  # X
            pygame.draw.line(screen, X_COLOR,
                             (x * CELL + 20, y * CELL + 20),
                             (x * CELL + 20 + int(100 * progress), y * CELL + 20 + int(100 * progress)), 6)
            pygame.draw.line(screen, X_COLOR,
                             (x * CELL + 100, y * CELL + 20),
                             (x * CELL + 100 - int(80 * progress), y * CELL + 20 + int(80 * progress)), 6)

        else:  # O
            pygame.draw.circle(screen, O_COLOR,
                               (x * CELL + CELL // 2, y * CELL + CELL // 2),
                               int(40 * progress), 6)

        pygame.display.update()
        pygame.time.delay(12)

# Gambar semua X/O

def draw_marks(except_pos=None):
    for r in range(3):
        for c in range(3):
            if board.grid[r][c] != 0:
                if except_pos == (c, r):
                    continue  
                if board.grid[r][c] == 1:
                    pygame.draw.line(screen, X_COLOR, (c * CELL + 20, r * CELL + 20),
                                     (c * CELL + 100, r * CELL + 100), 6)
                    pygame.draw.line(screen, X_COLOR, (c * CELL + 100, r * CELL + 20),
                                     (c * CELL + 20, r * CELL + 100), 6)
                else:
                    pygame.draw.circle(screen, O_COLOR,
                                       (c * CELL + CELL // 2, r * CELL + CELL // 2),
                                       40, 6)


# Animasi garis kemenangan
def draw_winner_line(info):
    kind, idx = info

    if kind == "row":
        start = (20, idx * CELL + CELL // 2)
        end = (WIDTH - 20, idx * CELL + CELL // 2)

    elif kind == "col":
        start = (idx * CELL + CELL // 2, 20)
        end = (idx * CELL + CELL // 2, HEIGHT - 20)

    else:  # diagonal
        if idx == 0:
            start = (20, 20)
            end = (WIDTH - 20, HEIGHT - 20)
        else:
            start = (WIDTH - 20, 20)
            end = (20, HEIGHT - 20)

    #  line draw
    for i in range(25):
        p = i / 25
        x = start[0] + (end[0] - start[0]) * p
        y = start[1] + (end[1] - start[1]) * p
        draw_board()
        draw_marks()
        pygame.draw.line(screen, (0, 200, 90), start, (x, y), 8)
        pygame.display.update()
        pygame.time.delay(20)


# MAIN LOOP
running = True
draw_board()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and board.winner_line is None:
            mx, my = event.pos
            col = mx // CELL
            row = my // CELL

            # Lakukan mark + animasi
            if board.mark(row, col):
                animate_mark(col, row, board.grid[row][col])

                w = board.check_winner()
                if w != 0:
                    draw_winner_line(board.winner_line)
                    pygame.time.wait(1500)
                    board.reset()

                elif board.full():
                    pygame.time.wait(800)
                    board.reset()

            draw_board()
            draw_marks()

    pygame.display.update()
