import turtle
import random

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
paddle_a.shapesize(5,1)
paddle_a.goto(-380,0)
paddle_a.color("white")
paddle_a.penup()

paddle_b = turtle.Turtle("square")
paddle_b.speed(0)
paddle_b.shapesize(5,1)
paddle_b.goto(370, 0)
paddle_b.color("white")
paddle_b.penup()


pen = turtle.Turtle("square")
pen.hideturtle()
pen.speed(0)
pen.shapesize(3,5)
pen.goto(0, 250)
pen.color("white")
pen.write("player A: 0       player B: 0", font=("Arial", 20, "normal"), align="center")

score_a = 0
score_b = 0

window.listen()

def paddle_a_up():
	old_y_cor = paddle_a.ycor()
	if old_y_cor < 250:
		paddle_a.sety(old_y_cor + 10)

def paddle_a_down():
	old_y_cor = paddle_a.ycor()
	if old_y_cor > -250:
		paddle_a.sety(old_y_cor - 10)

def paddle_b_up():
	old_y_cor_b = paddle_b.ycor()
	if old_y_cor_b < 250:
		paddle_b.sety(old_y_cor_b + 10)

def paddle_b_down():
	old_y_cor_b = paddle_b.ycor()
	if old_y_cor_b > -250:
		paddle_b.sety(old_y_cor_b - 10)

window.onkey(paddle_a_up, "w")
window.onkey(paddle_a_down, "s")

window.onkey(paddle_b_up, "Up")
window.onkey(paddle_b_down, "Down")

ball_is_moving_up = True
ball_is_moving_left = True

while True: #repeat the following statement for forever
	window.update()

	if ball_is_moving_up == True: #moving ball up
		ball.sety(ball.ycor() + 3)
	else:
		ball.sety(ball.ycor() - 3)

	if ball_is_moving_left == True: #moving left
		ball.setx(ball.xcor() - 2)
	else:
		ball.setx(ball.xcor() + 2)

	if ball.ycor() == 300: #if we hit the top stop moving
		ball_is_moving_up = False

	if ball.ycor() == -300:
		ball_is_moving_up = True
	
	if ball.xcor() == paddle_a.xcor() and ball.ycor() >= paddle_a.ycor() - 50 and ball.ycor()<= paddle_a.ycor() + 50:
		ball_is_moving_left = False #if we hit paddle a, start moving right

	if ball.xcor() == paddle_b.xcor() and ball.ycor() >= paddle_b.ycor() - 50 and ball.ycor() <= paddle_b.ycor() + 50:
		ball_is_moving_left = True


	if ball.xcor() < -400:
		ball_is_moving_left = random.choice([False, True])
		ball.goto(0,0)
		score_b += 1 
		#score_b = score_b +1
		pen.clear()
		pen.write("player A: " + str(score_a) + "    player B: " + str(score_b), font=("Arial", 20, "normal"), align="center")


	if ball.xcor() > 400:
		ball_is_moving_left = random.choice([False, True])
		ball.goto(0,0)
		score_a += 1 
		#score_b = score_b +1
		pen.clear()
		pen.write("player A: " + str(score_a) + "    player B: " + str(score_b), font=("Arial", 20, "normal"), align="center")



	



