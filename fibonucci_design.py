import turtle

def fibnuacci_generator(n):
    fib_x = 1
    fib_next = 1

    if n <= 2:
        fib_n = 1
    else:
        i = 3
        while i <= n:
            i += 1
            fib_temp = fib_x + fib_next
            fib_x = fib_next
            fib_next = fib_temp
        fib_n = fib_next
    return fib_n

turtle.speed(1)
turtle.left(180)

for num in range(1,8):
    m=fibnuacci_generator(num)
    for i in range(4):
        turtle.forward(20*m)
        turtle.right(90)
    turtle.circle(-20*m,90)
turtle.exitonclick()
