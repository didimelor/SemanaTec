"""
Snake game
Diana Karen Melo Reyes A01023785
Javier Perdomo Gonzalez A01026933
We will be adding features to the code retrieved from: http://www.grantjenks.com/docs/freegames/snake.html
Features added:
    - Randomized and changed snake and food colors on start.
    - Food changes place.
"""

from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
#Array to shuffle and set to the snake and food
colors = ['yellow', 'pink', 'green', 'purple', 'blue']
random.shuffle(colors)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        #Assign the snake the second color from the shuffled colors array
        square(body.x, body.y, 9, colors[1])
    #Move food
    move_food()
    #Assign the food the first color from the shuffled colors array
    square(food.x, food.y, 9, colors[0])
    update()
    ontimer(move, 100)

def move_food():
    "Food must randomly move one step at a time, without exiting boundaries"
    "New food position"
    new_food_pos_x = randrange(-1,1) * 10
    new_food_pos_y = randrange(-1,1) * 10
    "Check if food will leave boundaries"
    if (new_food_pos_x == -10) and (-140 < food.x):
        food.x = food.x + new_food_pos_x
    if (new_food_pos_x == 10) and (food.x < 140):
        food.x = food.x + new_food_pos_x
    if (new_food_pos_y == -10) and (-140 < food.y):
        food.y = food.y + new_food_pos_y
    if (new_food_pos_y == 10) and (food.y < 140):
        food.y = food.y + new_food_pos_y

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
