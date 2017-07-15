import turtle

turtle.speed(8)

def square_draw(side_length):
  for i in range(4):
    turtle.forward(side_length)
    turtle.left(90)

count = 0

while count < 90:
  square_draw(100)
  turtle.right(4)
  count +=1

turtle.exitonclick()
