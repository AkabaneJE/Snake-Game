import turtle
import time
from Snake import Snake
from food import Food
from score import Score
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

def quit():
    with open("./Score/highscore.txt") as file:
        prev_highscore = int(file.read())

    if (score.highscore > prev_highscore):
        with open("./Score/highscore.txt", "w") as file:
            file.write(str(score.highscore))

    turtle.bye()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(quit, "q")


is_game_started = True

while True:
    snake.move()
    screen.update()
    time.sleep(0.2)

    if snake.head.distance(food) < 10:
        snake.extend()
        food.reposition()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    for segment in snake.segments:
        if segment == snake.head:
            continue
        elif snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
