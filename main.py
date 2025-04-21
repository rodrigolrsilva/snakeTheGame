import time
from turtle import Turtle, Screen
from random import randint

from scoreboard import Scoreboard
from snake import Snake
from food import Food
import scoreboard

#screen.colormode(255)
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()#start listening for keystrokes
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_loop = True
# WIDTH = 20
# LENGTH = 20
# times_eaten = 1
# score_board = 0
#mudar de cor toda vez que snake cresce


#starting segments

#snake inicial
#tim.turtlesize(60, 60)
# segment_1.color("white")
# segment_2 = Turtle(shape="square")
# segment_3 = Turtle(shape="square")
# segment_2.penup()
# segment_3.penup()
# segment_2.setpos(-20, 0)
# segment_3.setpos(20,0)
# segment_2.color("white")
# segment_3.color("white")
def random_color():
    r = randint(1,255)
    g = randint(1, 255)
    b = randint(1, 255)
    color = (r, g, b)
    return color
# def grow_snake(tim):
#     segment_1.turtlesize(WIDTH * times_eaten, LENGTH * times_eaten)
#     segment_1.color(random_color())
#
# def eats():
#     if segment_1.pos() == food_object.pos():
#         global times_eaten
#         global score_board
#         score_board += 1
#         times_eaten += 1
#         segment_1.grow_snake()
#         return True
#     else:
#         return False

# def movement_control(key):
#     if key == "Up":
#         screen.onkeypress(tim.forward(20), "Up")
#     elif key == "Left":
#         c
#     elif key == "Down":
#         b
#     elif key == "Right":
#         a
#
while game_loop:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(20)

    # screen.listen()
    # screen.onkeypress()
    #if tim.eats():
    #score automatically updates
    #move snake
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15: #circle is 10x10 so if the snake head is 15px from the food consider it the border
        score.current_score += 1
        score.write_score()
        food.refresh()
        snake.extend()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_loop = False

    #Detect collision with tail
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_loop = False
            score.game_over()
screen.exitonclick()
#1. create a snake body 2.move the snake 3.control the snake 4.detect collision with food
#5. create a scoreboard 6. detect collission with wall(if snake.pos() == x | y = 250)
#7. detect collision with snake body