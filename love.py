import turtle

# Setup layar
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Love by fthrdev | ThurZ")  # Judul di title bar window

# Buat turtle untuk teks header
header = turtle.Turtle()
header.hideturtle()
header.color("white")
header.penup()
header.goto(0, 250)  # Atur posisi teks di atas
header.write("Author : fthrdev | ThurZ", align="center", font=("Arial", 16, "bold"))

# Buat turtle untuk menggambar love
love = turtle.Turtle()
love.color("red")
love.begin_fill()
love.speed(1)

# Gambar love
love.penup()
love.goto(0, -200)
love.pendown()
love.begin_fill()
love.left(140)
love.forward(224)
for _ in range(200):
    love.right(1)
    love.forward(2)
love.left(120)
for _ in range(200):
    love.right(1)
    love.forward(2)
love.forward(224)
love.end_fill()

love.hideturtle()

# Biarkan layar tetap terbuka
turtle.done()
