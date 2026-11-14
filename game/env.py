import random
class SnakeEnvironment:
    def __init__(self):
        self.WIDTH = 600
        self.HEIGHT =400
        self.CELL_SIZE = 20
        self.reset()
    def create_food(self):
        free_cell = [
                [x, y]
                for x in range(0, self.WIDTH, self.CELL_SIZE)
                for y in range(0, self.HEIGHT, self.CELL_SIZE)
                if [x, y] not in self.snake
            ]
        return random.choice(free_cell) if free_cell else None
    def reset(self):
        self.snake = [
            [120, 100],
            [100, 100],
            [80, 100]
        ]
        self.direction = (self.CELL_SIZE, 0)
        self.food = self.create_food()
        self.score = 0
        self.game_over = "won" if self.food is None else None
        return self.get_state()
    def update(self,action):
        if self.game_over is not None:
            return self.get_state()
        movement={
            'UP':(0,-self.CELL_SIZE),
            'DOWN':(0,self.CELL_SIZE),
            'RIGHT':(self.CELL_SIZE,0),
            'LEFT':(-self.CELL_SIZE,0)
        }
        if action not in movement:
            raise ValueError(f"Invalid action:{action}")
        if action == 'UP' and self.direction!=movement['DOWN']:
            self.direction=movement['UP']
        elif action == 'DOWN' and self.direction != movement['UP']:
            self.direction=movement['DOWN']
        elif action == 'LEFT' and self.direction != movement['RIGHT']:
            self.direction = movement['LEFT']
        elif action == 'RIGHT' and self.direction !=movement['LEFT']:
            self.direction=movement['RIGHT']
        new_head=[
                self.snake[0][0] + self.direction[0],
                self.snake[0][1] + self.direction[1]
            ]
        eating = new_head==self.food
        body = self.snake if eating else self.snake[:-1]
        if (
                new_head[0] < 0
                or new_head[0] >= self.WIDTH
                or new_head[1] < 0
                or new_head[1] >= self.HEIGHT
                or new_head in body
            ):
            self.game_over='lost'
            return self.get_state()
        self.snake.insert(0,new_head)
        if eating:
            self.score+=1
            self.food = self.create_food()
            if self.food is None:
                self.game_over='won'
        else:
            self.snake.pop()
        return self.get_state()
    def get_state(self):
        return {
            'snake':[segment.copy() for segment in self.snake],
            'food':self.food.copy() if self.food is not None else None,
            'direction' : self.direction,
            'score':self.score,
            'game_over':self.game_over
        }