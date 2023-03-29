import turtle

def dragon_curve1(t, iterations, length, shortening_factor, angle):
    if iterations == 0:
        t.forward(length)
    else:
        iterations = iterations - 1
        length = length / shortening_factor
        t.left(angle)
        dragon_curve1(t, iterations, length, shortening_factor, angle)
        t.right(angle * 2)
        dragon_curve2(t, iterations, length, shortening_factor, angle)
        t.left(angle)
        
def dragon_curve2(t, iterations, length, shortening_factor, angle):
    if iterations == 0:
        t.forward(length)
    else:
        iterations = iterations - 1
        length = length / shortening_factor
        t.right(angle)
        dragon_curve1(t, iterations, length, shortening_factor, angle)
        t.left(angle * 2)
        dragon_curve2(t, iterations, length, shortening_factor, angle)
        t.right(angle)

if __name__ =="__main__":
    t = turtle.Turtle()
    t.hideturtle()
    dragon_curve1(t, 10, 100, pow(2,0.5), 45)