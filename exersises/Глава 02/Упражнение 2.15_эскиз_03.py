# Эскиз 3

import turtle

# Именованные константы
TOP_SQUARE_TOP_LEFT_X = -100
TOP_SQUARE_TOP_LEFT_Y = 100
TOP_SQUARE_TOP_RIGHT_X = 0
TOP_SQUARE_TOP_RIGHT_Y = 100
TOP_SQUARE_BOTTOM_LEFT_X = -100
TOP_SQUARE_BOTTOM_LEFT_Y = 0
TOP_SQUARE_BOTTOM_RIGHT_X = 0
TOP_SQUARE_BOTTOM_RIGHT_Y = 0

BOTTOM_SQUARE_TOP_LEFT_X = 0
BOTTOM_SQUARE_TOP_LEFT_Y = 0
BOTTOM_SQUARE_TOP_RIGHT_X = 100
BOTTOM_SQUARE_TOP_RIGHT_Y = 0
BOTTOM_SQUARE_BOTTOM_RIGHT_X = 100
BOTTOM_SQUARE_BOTTOM_RIGHT_Y = -100
BOTTOM_SQUARE_BOTTOM_LEFT_X = 0
BOTTOM_SQUARE_BOTTOM_LEFT_Y = -100

# Спрятать черепаху и поднять перо.
turtle.hideturtle()
turtle.penup()

# Начертить самый верхний квадрат
turtle.goto(TOP_SQUARE_BOTTOM_RIGHT_X, TOP_SQUARE_BOTTOM_RIGHT_Y)
turtle.pendown()
turtle.goto(TOP_SQUARE_TOP_RIGHT_X, TOP_SQUARE_TOP_RIGHT_Y)
turtle.goto(TOP_SQUARE_TOP_LEFT_X, TOP_SQUARE_TOP_LEFT_Y)
turtle.goto(TOP_SQUARE_BOTTOM_LEFT_X, TOP_SQUARE_BOTTOM_LEFT_Y)
turtle.goto(TOP_SQUARE_BOTTOM_RIGHT_X, TOP_SQUARE_BOTTOM_RIGHT_Y)
turtle.penup()

# Начертить нижний квадрат
turtle.goto(BOTTOM_SQUARE_BOTTOM_RIGHT_X, BOTTOM_SQUARE_BOTTOM_RIGHT_Y)
turtle.pendown()
turtle.goto(BOTTOM_SQUARE_TOP_RIGHT_X, BOTTOM_SQUARE_TOP_RIGHT_Y)
turtle.goto(BOTTOM_SQUARE_TOP_LEFT_X, BOTTOM_SQUARE_TOP_LEFT_Y)
turtle.goto(BOTTOM_SQUARE_BOTTOM_LEFT_X, BOTTOM_SQUARE_BOTTOM_LEFT_Y)
turtle.goto(BOTTOM_SQUARE_BOTTOM_RIGHT_X, BOTTOM_SQUARE_BOTTOM_RIGHT_Y)
turtle.penup()

# Соединить углы
turtle.goto(BOTTOM_SQUARE_BOTTOM_RIGHT_X, BOTTOM_SQUARE_BOTTOM_RIGHT_Y)
turtle.pendown()
turtle.goto(TOP_SQUARE_TOP_LEFT_X, TOP_SQUARE_TOP_LEFT_Y)
turtle.penup()
turtle.goto(BOTTOM_SQUARE_TOP_RIGHT_X, BOTTOM_SQUARE_TOP_RIGHT_Y)
turtle.pendown()
turtle.goto(TOP_SQUARE_TOP_RIGHT_X, TOP_SQUARE_TOP_RIGHT_Y)
turtle.penup()
turtle.goto(BOTTOM_SQUARE_BOTTOM_LEFT_X, BOTTOM_SQUARE_BOTTOM_LEFT_Y)
turtle.pendown()
turtle.goto(TOP_SQUARE_BOTTOM_LEFT_X, TOP_SQUARE_BOTTOM_LEFT_Y)