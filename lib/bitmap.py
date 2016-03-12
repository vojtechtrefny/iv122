from PIL import Image, ImageDraw


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PNG(object):

    def __init__(self, width=400, height=400):
        self.width = width
        self.height = height

        self.image = Image.new("RGBA", (self.width, self.height), (255, 255, 255, 255))

        self.draw = ImageDraw.Draw(self.image)

    def draw_line(self, start, end, color="black", width=1):
        self.draw.line(xy=(start.x, start.y, end.x, end.y), fill=color, width=width)

    def draw_pixel(self, point, color="black"):
        self.draw.point(xy=(point.x, point.y), fill=color)

    def draw_circle(self, center, radius, fill_color="black", outline_color="black"):
        bounds = (center.x - radius, center.y - radius,
                  center.x + radius, center.y + radius)
        self.draw.ellipse(bounds, fill=fill_color, outline=outline_color)

    def draw_rectangle(self, point, size, fill_color="black", outline_color="black"):
        bounds = (point.x, point.y,
                  point.x + size, point.y + size)
        self.draw.rectangle(bounds, fill=fill_color, outline=outline_color)

    def show(self):
        self.image.show()
