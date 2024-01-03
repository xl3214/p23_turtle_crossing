import time
import turtle as t
from player import Player
from car_manager import CarManager
from score_board import ScoreBoard


screen = t.Screen()
screen.setup(600, 600)
screen.title("Kristal's First Turtle Crossing Game")
screen.tracer(0)
score_board = ScoreBoard()
tim = Player()

KEYS = {"Up": tim.move}
screen.listen()
for key in KEYS:
    screen.onkey(key="Up", fun=KEYS[key])

cars = []
loop_counter = 0

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    # Every 6th loop, create a new car
    if loop_counter % 6 == 0:
        new_car = CarManager()
        cars.append(new_car)

    for car in cars:
        car.move()
        if tim.distance(car) <= 20:
            game_on = False
            score_board.game_over()
            break  # Exit the for loop immediately after collision is detected

    if tim.has_restarted:
        score_board.increase_score()
        for car in cars:
            car.speed_up()
        tim.has_restarted = False

    loop_counter += 1


screen.exitonclick()
