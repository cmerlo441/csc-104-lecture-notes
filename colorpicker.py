#! /usr/bin/env python3

'''Choose an RGB Color.

Allow the user to click on red, green, and blue rectangles to generate
an RGB color.

Requires John Zelle's graphics.py module.
'''

__author__ = 'Christopher R. Merlo'
__copyright__ = 'Copyright 2019 Christopher R. Merlo.  Some rights reserved.'
__license__ = 'GPL'
__version__ = 1.0
__email__ = 'cmerlo@ncc.edu'
__status__ = 'Production'

from graphics import *

width, height = 1024, 768
title = 'Python Color Picker'

win = GraphWin(title, width, height)

# instructions

instructions = Text(
    Point(512, 40), 'Click inside the color boxes to change colors')
instructions.setSize(24)
instructions.draw(win)

# red rectangle

red_ul = Point(100, 75)
red_lr = Point(924, 175)
red_rect = Rectangle(red_ul, red_lr)
red_value = 255

red_rect.setFill(color_rgb(red_value, 0, 0))
red_rect.draw(win)

# text on red rectangle

red_text = Text(Point((red_rect.p1.x + red_rect.p2.x)/2,
                      (red_rect.p1.y + red_rect.p2.y)/2),
                red_value)
red_text.setFill('black')
red_text.setOutline('black')
red_text.setSize(32)
red_text.draw(win)

# green rectangle

green_ul = Point(100, 225)
green_lr = Point(924, 325)
green_rect = Rectangle(green_ul, green_lr)
green_value = 255

green_rect.setFill(color_rgb(0, green_value, 0))
green_rect.draw(win)

# text on green rectangle

green_text = Text(Point((green_rect.p1.x + green_rect.p2.x)/2,
                        (green_rect.p1.y + green_rect.p2.y)/2),
                  green_value)
green_text.setFill('black')
green_text.setOutline('black')
green_text.setSize(32)
green_text.draw(win)

# blue rectangle

blue_ul = Point(100, 375)
blue_lr = Point(924, 475)
blue_rect = Rectangle(blue_ul, blue_lr)
blue_value = 255

blue_rect.setFill(color_rgb(0, 0, blue_value))
blue_rect.draw(win)

# text on blue rectangle

blue_text = Text(Point((blue_rect.p1.x + blue_rect.p2.x)/2,
                       (blue_rect.p1.y + blue_rect.p2.y)/2),
                 blue_value)
blue_text.setFill('black')
blue_text.setOutline('black')
blue_text.setSize(32)
blue_text.draw(win)

# rgb rectangle

rgb_ul = Point(100, 525)
rgb_lr = Point(924, 625)
rgb_rect = Rectangle(rgb_ul, rgb_lr)
rgb_value = str(red_value) + ', ' + str(green_value) + ', ' + str(blue_value)

rgb_rect.setFill(color_rgb(red_value, green_value, blue_value))
rgb_rect.draw(win)

# text on rgb rectangle

rgb_text = Text(Point((rgb_rect.p1.x + rgb_rect.p2.x)/2,
                      (rgb_rect.p1.y + rgb_rect.p2.y)/2),
                rgb_value)
rgb_text.setFill('black')
rgb_text.setOutline('black')
rgb_text.setSize(32)
rgb_text.draw(win)

# exit button

exit_rect = Rectangle(Point(100, 675), Point(924, 725))
exit_rect.setFill('black')
exit_rect.draw(win)

exit_text = Text(Point((rgb_rect.p1.x + rgb_rect.p2.x)/2, 700),
                 'Click Here to Exit')
exit_text.setSize(32)
exit_text.setOutline('white')
exit_text.draw(win)


def inRect(p):
    if p.x >= red_rect.p1.x and p.x <= red_rect.p2.x and p.y >= red_rect.p1.y and p.y <= red_rect.p2.y:
        return 'red'
    elif p.x >= green_rect.p1.x and p.x <= green_rect.p2.x and p.y >= green_rect.p1.y and p.y <= green_rect.p2.y:
        return 'green'
    elif p.x >= blue_rect.p1.x and p.x <= blue_rect.p2.x and p.y >= blue_rect.p1.y and p.y <= blue_rect.p2.y:
        return 'blue'
    elif p.x >= exit_rect.p1.x and p.x <= exit_rect.p2.x and p.y >= exit_rect.p1.y and p.y <= exit_rect.p2.y:
        return 'exit'
    else:
        return 'no'

#####


exit = False
while not exit:
    m = win.getMouse()
    if inRect(m) == 'red':
        x = m.x
        red_value = round(
            ((m.x - 100) / (red_rect.p2.x - red_rect.p1.x)) * 255)
        red_rect.setFill(color_rgb(red_value, 0, 0))
        red_text.setText(red_value)
        if red_value < 128:
            red_text.setOutline('white')
        else:
            red_text.setOutline('black')

    elif inRect(m) == 'green':
        x = m.x
        green_value = round(
            ((m.x - 100) / (green_rect.p2.x - green_rect.p1.x)) * 255)
        green_rect.setFill(color_rgb(0, green_value, 0))
        green_text.setText(green_value)
        if green_value < 128:
            green_text.setOutline('white')
        else:
            green_text.setOutline('black')

    elif inRect(m) == 'blue':
        x = m.x
        blue_value = round(
            ((m.x - 100) / (blue_rect.p2.x - blue_rect.p1.x)) * 255)
        blue_rect.setFill(color_rgb(0, 0, blue_value))
        blue_text.setText(blue_value)
        if blue_value < 128:
            blue_text.setOutline('white')
        else:
            blue_text.setOutline('black')

    elif inRect(m) == 'exit':
        exit = True

    rgb_text.setText(str(red_value) + ', ' + str(green_value) +
                     ', ' + str(blue_value))
    rgb_rect.setFill(color_rgb(red_value, green_value, blue_value))
    if(red_value + green_value + blue_value < 128 * 3):
        rgb_text.setOutline('white')
    else:
        rgb_text.setOutline('black')

win.close()
