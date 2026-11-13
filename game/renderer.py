import pygame as game
class Renderer:
    def __init__(self,HEIGHT,WIDTH,CELL_SIZE):
        game.init()
        self.BLACK = (18, 18, 18)
        self.WHITE = (255, 255, 255)
        self.GREEN = (70, 200, 90)
        self.RED = (230, 60, 70)
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.CELL_SIZE = CELL_SIZE
        self.FPS = 10
        self.screen = game.display.set_mode((self.WIDTH, self.HEIGHT))
        game.display.set_caption("Snake Game")
        self.clock = game.time.Clock()
        self.font = game.font.Font(None, 30)
        self.message_font = game.font.Font(None, 40)
        self.small_font = game.font.Font(None, 24)
    def background(self):
        self.screen.fill(self.BLACK)
    def snake(self,snake):
        for segment in snake:
            game.draw.rect(
                self.screen,
                self.GREEN,
                (segment[0], segment[1], self.CELL_SIZE, self.CELL_SIZE)
            )
    def food (self,food):
        if food is not None:
            game.draw.rect(
                self.screen,
                self.RED,
                (food[0], food[1], self.CELL_SIZE, self.CELL_SIZE)
            )
    def score(self,score):
        score_text = self.font.render(f"Score: {score}", True, self.WHITE)
        self.screen.blit(score_text, (10, 10))
    def game_over(self,game_over):
        if game_over is not None:
            if game_over == "won":
                message = "You Win!!"
            else:
                message = "Game Over"
            
            message_text = self.message_font.render(message, True, self.WHITE)
            restart_text = self.small_font.render(
                "Press Enter to restart or Esc to quit",
                True,
                self.WHITE
            )
            self.screen.blit(
                message_text,
                message_text.get_rect(
                    center=(self.WIDTH // 2, self.HEIGHT // 2 - 20)
                )
            )
            self.screen.blit(
                restart_text,
                restart_text.get_rect(
                    center=(self.WIDTH // 2, self.HEIGHT // 2 + 20)
                )
            )
    def render(self,state):
        snake = state['snake']
        food = state['food']
        score = state['score']
        game_over = state['game_over']
        self.background()
        self.snake(snake)
        self.food(food)
        self.score(score)
        self.game_over(game_over)
        game.display.flip()
        self.clock.tick(self.FPS)
