from turtle import Turtle


def fractal_image(name, angle, seed, rules, iterations=5):
    curve = seed

    for i in range(iterations):
        replaced_curve = ""

        for char in curve:
            if char in rules.keys():
                replaced_curve += rules[char]
            else:
                replaced_curve += char

        curve = replaced_curve

    t = Turtle(name=name)

    for step in curve:
        if step == "F":
            t.forward(10)
        elif step == "-":
            t.left(angle)
        elif step == "+":
            t.right(angle)
        elif step == "|":
            t.left(180)

    t.write_svg()


# koch snowflake
fractal_image(name="koch", angle=60, seed="F++F++F", rules={"F" : "F-F++F-F"})

# hilbert curve
fractal_image(name="hilbert", angle=90, seed="L", rules={"L" : "+RF-LFL-FR+", "R" : "-LF+RFR+FL-"})

# sierpinski triangle
fractal_image(name="sierpinski", angle=60, seed="FXF++FF++FF", rules={"F" : "FF", "X" : "++FXF--FXF--FXF++"})

# pentagons
fractal_image(name="pentagons", angle=36, seed="F++F++F++F++F", rules={"F" : "F++F++F|F-F++F"})
