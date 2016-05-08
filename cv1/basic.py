from lib import bitmap, vector

def bitmap_img():
    img = bitmap.PNG()

    for i in range(255):
        for j in range(255):
            img.draw_pixel(bitmap.Point(i, 255 - j), color=(i, 0, 255 - j))

    img.show()


def vector_img(size=200):
    svg = vector.SVG(folder="cv1", name="vector")

    for i in range(0, size + 10, 10):
        svg.add_line(size, 2 * size - i, size - i, size)
        svg.add_line(size, 2 * size - i, size + i, size)

        svg.add_line(size, 0 + i, size - i, size)
        svg.add_line(size, 0 + i, size + i, size)

    svg.save()
