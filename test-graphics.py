#! /usr/bin/env python3

'''Test the graphics module.

Type this code in and run it to make sure you have
correctly installed the graphics module.
'''

__author__  = 'Your Name'
__section__ = 'Your Section'
__email__   = 'N00xxxxxx@students.ncc.edu'

from graphics import *

win = GraphWin('Testing the Graphics Module', 250, 250)

p = Point(125, 125)
c = Circle(p, 50)
c.setOutline('black')
c.setFill('red')
c.draw(win)

# Make the user have to click the mouse in
# the window before exiting
win.getMouse()
win.close()