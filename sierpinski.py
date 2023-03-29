import turtle

def sierpinski_triangle(t, iterations, length, shortening_factor, angle):
    if iterations == 0:
        t.forward(length)
    else:
        iterations = iterations - 1
        length = length / shortening_factor
        sierpinski_triangle(t, iterations, length, shortening_factor, angle)
        t.left(angle)
        sierpinski_triangle(t, iterations, length, shortening_factor, angle)
        t.right(angle)
        sierpinski_triangle(t, iterations, length, shortening_factor, angle)
        t.right(angle)
        sierpinski_triangle(t, iterations, length, shortening_factor, angle)
        t.left(angle)
        sierpinski_triangle(t, iterations, length, shortening_factor, angle)
        

if __name__ =="__main__":
    t = turtle.Turtle()
    t.hideturtle()
    
    sierpinski_triangle(t, 3, 100, 2, 120)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
      