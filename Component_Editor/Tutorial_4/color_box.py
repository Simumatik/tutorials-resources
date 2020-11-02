if initialize:
    cube_color = [0, 0, 0, 1]
else:
    if is_pressed:
        red = float(numpy.random.random())
        green = float(numpy.random.random())
        blue = float(numpy.random.random())
        
        cube_color = [red, green, blue, 1]