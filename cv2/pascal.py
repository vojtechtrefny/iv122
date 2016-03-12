import math

from lib import bitmap

comb = lambda n, k: math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

colors = ["blue", "green", "cyan", "purple", "red", "brown", "orange", "pink", "yellow", "white"]


def pascal_triangle(n, d):
    triangle = []
    for level in range(n + 1):
        row = []

        for i in range(level + 1):
            elem = comb(level, i)
            row.append(elem % d)

        triangle.append(row)

    return triangle


def pascal_image(triangle):
    rect_size = 20
    image_size = len(triangle) * rect_size
    image = bitmap.PNG(width=image_size, height=image_size)

    pos = bitmap.Point(0, len(triangle) * rect_size)  # starting position for draw

    # build the image from bottom up
    for level, row in enumerate(reversed(triangle)):
        for num in row:
            image.draw_rectangle(point=pos, size=rect_size, fill_color=colors[num % len(colors)])
            pos.x += rect_size

        pos.y -= rect_size  # one level up
        pos.x = (rect_size / 2) * (level + 1)  # shift start position to the right

    image.show()


pascal_image(pascal_triangle(30, 5))
