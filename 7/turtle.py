import turtle


def draw_a_square(length, angle=90):
    for i in range(4):
        forward(length)
        right(angle)


draw_a_square(90, 90)
