# Pong 게임 구현_2023.02.25
# 참고 : https://www.freecodecamp.org/news/how-to-code-pong-in-python/
import turtle

# Setup 게임 스크린
# turtle.speed(0)
turtle.setup(800, 600)
turtle.bgcolor("black")
turtle.title("Pong by @Youmin")

# 왼쪽 패들
left = turtle.Turtle()
left.shape("square")
left.color("red")
left.shapesize(stretch_wid=5, stretch_len=1)
left.penup()
left.goto(-350, 0)
left.dy = 0     # left의 y 좌표 이동 방향
left.dx = 0

# 오른쪽 패들
right = turtle.Turtle()
right.shape("square")
right.color("blue")
right.shapesize(stretch_wid=5, stretch_len=1)
right.penup()
right.goto(350, 0)
right.dy = 0
right.dx = 0

# 공
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 10 # 방향, 간격 : 2px 씩 올라감 (+: 오른쪽방향, -:왼쪽 방향)
ball.dy = 2 # 2 픽셀 방향(+: 위쪽 방향, -:아래쪽 방향)

# 게임 규칙
game_over = False
winner = None
points = {
    "player1" : 0,
    "player2" : 0
}
game_rules = {
    "max_points":3,
    "ball_speed":0
}

# 점수 디스플레이
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player 1: 0, Player 2:0", align="center", font=("Arial", 24, "normal"))

# left Up 버튼
def left_up():
    left.sety(left.ycor() + 20)

# left Down 버튼
def left_down():
    left.sety(left.ycor() - 20)

# left Left 버튼
def left_left():
    if left.xcor() <= -350:
        return
    left.setx(left.xcor() - 20)

# left Right 버튼ㅁㅁ
def left_right():
    if left.xcor() >= -10:
        return
    left.setx(left.xcor() + 20)

# right Up 버튼
def right_up():
    right.sety(right.ycor() + 20)

# right Down 버튼
def right_down():
    right.sety(right.ycor() - 20)

# right Left 버튼
def right_left():
    if right.xcor() < 10:
        return
    right.setx(right.xcor() - 20)

# right Right 버튼
def right_right():
    if right.xcor() >= 350:
        return
    right.setx(right.xcor() + 20)

# Set up keyboard bindings
turtle.listen()
turtle.onkeypress(left_up, "w")
turtle.onkeypress(left_down, "s")
turtle.onkeypress(left_left, "a")
turtle.onkeypress(left_right, "d")

turtle.onkeypress(right_up, "Up")
turtle.onkeypress(right_down, "Down")
turtle.onkeypress(right_left, "Left")
turtle.onkeypress(right_right, "Right")

while True:
    turtle.update()
    # 공이동
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)    # 대각선 이동

    # 게임 오버 조건인지 확인 : 먼저 max_points 도달한 사람이 winner
    if points["player1"] == game_rules["max_points"]:
        game_over = True
        winner = "player1"
    elif points["player2"] == game_rules["max_points"]:
        game_over = True
        winner = "player2"
    # 패들과 공의 충돌 감지
    # right에 충돌했는지 감지
    if (ball.xcor() > right.xcor() - 10 and ball.xcor() < right.xcor() + 10) and (ball.ycor() < right.ycor() + 50 and ball.ycor() > right.ycor() - 50):
        ball.setx(0)
        ball.dx *= -1       # 공의 방향 바꾸기
    # left에 충돌했는지 감지
    if (ball.xcor() > left.xcor() - 10 and ball.xcor() < left.xcor() + 10) and (ball.ycor() < left.ycor() + 50 and ball.ycor() > left.ycor() - 50):
        ball.setx(0)
        ball.dx *= -1       # 공의 방향 바꾸기

    # 공이 스크린 밖으로 나갔는지 확인
    if ball.xcor() > 390:   # 오른쪽으로 나간 경우 - 왼쪽이 점수 get
        ball.goto(0, 0)     # 화면 중앙으로 재설정
        ball.dx *= -1       # 공의 방향 바꾸기
        points["player1"] += 1
    elif ball.xcor() < -390:    # 왼쪽으로 나간 경우 - 오른쪽이 점수 get
        ball.goto(0, 0)         
        ball.dx *= -1           
        points["player2"] += 1

    # 맨위나 바닥에 닿은 경우
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1           # 공의 방향 바꾸기
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # 점수 업데이트
    score_display.clear()
    score_display.write("Player 1: {}, Player 2:{}".format(points["player1"], points["player2"]), align="center", font=("Arial", 24, "normal"))
    if game_over:    
        # Game over screen
        game_over_display = turtle.Turtle()
        game_over_display.color("white")
        game_over_display.penup()
        game_over_display.hideturtle()
        game_over_display.goto(0, 0)
        game_over_display.write("Game Over! {} wins!".format(winner), align="center", font=("Arial", 36, "normal"))
