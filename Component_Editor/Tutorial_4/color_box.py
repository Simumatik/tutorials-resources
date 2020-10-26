if initialize:
    cube_color = [0, 0, 0, 1]
else:
    if is_pressed:
        red = float(numpy.random())
        green = float(numpy.random())
        blue = float(numpy.random())
        
        cube_color = [red, green, blue, 1]