import turtle

window = turtle.Screen()
window._root.attributes('-topmost', 1)
window._root.attributes('-topmost', 0)
#bg is background
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

ball = turtle.Turtle("circle")
ball.speed(0)
ball.penup()
ball.goto(0, 0)
ball.color("white")

paddle_a = turtle.Turtle("square")
paddle_a.speed(0)
paddle_a.goto(-380,0)
paddle_a.color("white")
paddle_a.penup()

paddle_b = turtle.Turtle("square")
paddle_b.speed(0)
paddle_b.goto(370, 0)
paddle_b.color("white")
paddle_b.penup()

window.listen()

def paddle_a_up():
	old_y_cor = paddle_a.ycor()
	paddle_a.sety(old_y_cor + 10)

def paddle_a_down():
	old_y_cor = paddle_a.ycor()
	paddle_a.sety(old_y_cor - 10)

def paddle_b_up():
	old_y_cor_b = paddle_b.ycor()
	paddle_b.sety(old_y_cor_b + 10)

def paddle_b_down():
	old_y_cor_b = paddle_b.ycor()
	paddle_b.sety(old_y_cor_b - 10)

window.onkey(paddle_a_up, "w")
window.onkey(paddle_a_down, "s")

window.onkey(paddle_b_up, "Up")
window.onkey(paddle_b_down, "Down")

ball_is_moving_up = True
ball_is_moving_left = True

while True: 
	window.update()

	if ball_is_moving_up == True:
		ball.sety(ball.ycor() + 3)

	if ball_is_moving_left == True:
		ball.setx(ball.xcor() - 3)

	# if ball.ycor() == 300:


	



