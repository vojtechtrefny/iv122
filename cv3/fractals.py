import copy
import colorsys

from turtle import Turtle


def fractal_image(name, angle, seed, rules, iterations=5, color=True):
    stack = []
    curve = seed

    for i in range(iterations):
        replaced_curve = ""

        for char in curve:
            if char in rules.keys():
                replaced_curve += rules[char]
            else:
                replaced_curve += char

        curve = replaced_curve

    if color:
        name += "_color"

    t = Turtle(name=name)

    for idx, step in enumerate(curve):
        if step in ("F", "G"):
            if color:
                hsv_color = ((idx + 1) / len(curve), 0.75, 0.75)
                rgb_color = [int(255 * i) for i in colorsys.hsv_to_rgb(*hsv_color)]
                t.forward(10, color="rgb(%d, %d, %d" % (rgb_color[0], rgb_color[1], rgb_color[2]))
            else:
                t.forward(10)
        elif step == "f":
            t.penup()
            t.forward(10)
            t.pendown()
        elif step == "-":
            t.left(angle)
        elif step == "+":
            t.right(angle)
        elif step == "|":
            t.left(180)
        elif step == "[":
            t.push()
        elif step == "]":
            t.pop()

    t.write_svg()


# koch snowflake
fractal_image(name="koch", angle=60, seed="F++F++F", rules={"F" : "F-F++F-F"})

# hilbert curve
fractal_image(name="hilbert", angle=90, seed="L", rules={"L" : "+RF-LFL-FR+", "R" : "-LF+RFR+FL-"})

# hilbert curve
fractal_image(name="hilbert2", angle=95, seed="L", rules={"L" : "+RF-LFL-FR+", "R" : "-LF+RFR+FL-"})

# sierpinski triangle
fractal_image(name="sierpinski", angle=60, seed="FXF++FF++FF", rules={"F" : "FF", "X" : "++FXF--FXF--FXF++"})

# sierpinski triangle
fractal_image(name="sierpinski2", angle=60, seed="F", rules={"F" : "+G-F-G+", "G" : "-F+G+F-"}, iterations=6)

# pentagons
fractal_image(name="pentagons", angle=36, seed="F++F++F++F++F", rules={"F" : "F++F++F|F-F++F"})

# plant
fractal_image(name="plant", angle=25, seed="X", rules={"X" : "F-[[X]+X]+F[+FX]-X", "F" : "FF"})

# islands and lakes
fractal_image(name="islands", angle=90, seed="F+F+F+F", rules={"F" : "F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF", "f" : "ffffff"}, iterations=2)

# gosper
fractal_image(name="gosper", angle=60, seed="F", rules={"F" : "F+G++G-F--FF-G+", "G" : "-F+GG++G+F--F-G"}, iterations=4)
