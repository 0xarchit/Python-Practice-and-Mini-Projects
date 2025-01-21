import colorgram

rgb = []
colors = colorgram.extract('Self\Turtle\image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb.append((r,g,b))

print(rgb)