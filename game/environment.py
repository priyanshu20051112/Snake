import random
import pygame as game
game.init()
HEIGHT = 400
WIDTH = 600
CELL_SIZE = 20
FPS = 10
BLACK = (18, 18, 18)
WHITE = (255, 255, 255)
GREEN = (70, 200, 90)
RED = (230, 60, 70)
screen = game.display.set_mode((WIDTH, HEIGHT))
game.display.set_caption("Snake Game")
clock = game.time.Clock()
font = game.font.Font(None, 30)
message_font = game.font.Font(None, 40)
small_font = game.font.Font(None, 24)
def create_food(snake):
    free_cell = [
        [x, y]
        for x in range(0, WIDTH, CELL_SIZE)
        for y in range(0, HEIGHT, CELL_SIZE)
        if [x, y] not in snake
    ]
    return random.choice(free_cell) if free_cell else None
def reset_game():
    snake = [
        [120, 100],
        [100, 100],
        [80, 100]
    ]
    direction = (CELL_SIZE, 0)
    food = create_food(snake)
    score = 0
    game_over = "won" if food is None else None
    return snake, food, direction, game_over, score
snake, food, direction, game_over, score = reset_game()
running = True
while running:
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
        elif event.type == game.KEYDOWN:
            if event.key == game.K_ESCAPE:
                running = False
            elif game_over is not None and event.key == game.K_RETURN:
                snake, food, direction, game_over, score = reset_game()
            elif game_over is None:
                if event.key == game.K_UP and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                elif event.key == game.K_DOWN and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif event.key == game.K_LEFT and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                elif event.key == game.K_RIGHT and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)
    if not running:
        break
    if game_over is None:
        new_head = [
            snake[0][0] + direction[0],
            snake[0][1] + direction[1]
        ]
        eating = new_head == food
        body = snake if eating else snake[:-1]
        if (
            new_head[0] < 0
            or new_head[0] >= WIDTH
            or new_head[1] < 0
            or new_head[1] >= HEIGHT
            or new_head in body
        ):
            game_over = "lost"
        else:
            snake.insert(0, new_head)
            if eating:
                score += 1
                food = create_food(snake)

                if food is None:
                    game_over = "won"
            else:
                snake.pop()
    screen.fill(BLACK)
    for segment in snake:
        game.draw.rect(
            screen,
            GREEN,
            (segment[0], segment[1], CELL_SIZE, CELL_SIZE)
        )
    if food is not None:
        game.draw.rect(
            screen,
            RED,
            (food[0], food[1], CELL_SIZE, CELL_SIZE)
        )
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    if game_over is not None:
        if game_over == "won":
            message = "You Win!!"
        else:
            message = "Game Over"
        message_text = message_font.render(message, True, WHITE)
        restart_text = small_font.render(
            "Press Enter to restart or Esc to quit",
            True,
            WHITE
        )
        screen.blit(
            message_text,
            message_text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2 - 20)
            )
        )
        screen.blit(
            restart_text,
            restart_text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2 + 20)
            )
        )
    game.display.flip()
    clock.tick(FPS)
game.quit()
