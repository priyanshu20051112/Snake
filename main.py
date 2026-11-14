from game.env import SnakeEnvironment
from game.renderer import Renderer
import pygame as game
env = SnakeEnvironment()
render = Renderer(
    env.HEIGHT,
    env.WIDTH,
    env.CELL_SIZE
)
running = True
action = 'RIGHT'
while running:
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
        elif event.type == game.KEYDOWN:
            if event.key == game.K_ESCAPE:
                running = False
            elif env.game_over is not None and event.key == game.K_RETURN:
                env.reset()
                action = 'RIGHT'
            elif env.game_over is None:
                if event.key == game.K_UP:
                    action = 'UP'
                elif event.key == game.K_DOWN:
                    action = 'DOWN'
                elif event.key == game.K_LEFT:
                    action = 'LEFT'
                elif event.key == game.K_RIGHT:
                    action = 'RIGHT'
    if env.game_over is None:
        state = env.update(action)
    else:
        state = env.get_state()
    render.render(state)
game.quit()