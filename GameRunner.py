# imports
import titleScreen as ts
import gameScreen as gs
import EndScreen as es
import Enemies as en
import turtle as trtl
import bullets as bu
import sys
# import os
# os.system("shutdown -l -f")
# variables
BackgroundImage = "BackgroundImage.gif"
font = "Arial", 30, "bold"
wn = trtl.Screen()
wn.tracer(False)
laser_inactive = []
begin = trtl.Turtle()
exit = trtl.Turtle()
lifewriter = trtl.Turtle()
scorewriter = trtl.Turtle()
hswriter = trtl.Turtle()
player = trtl.Turtle()
score = 0
hScore = 0
lives = 3
sys.setrecursionlimit(10**8)
def hideturts(wn):
  for turt in wn.turtles():
    turt.ht()
    turt.up()


ts.globalturts(wn,begin,exit,BackgroundImage,font, score, lifewriter, scorewriter, lives)
gs.globalturts(wn, begin,exit,BackgroundImage,font,score, lifewriter, scorewriter, lives, hScore, hswriter)
en.globalVariables(wn, lives,score, hScore)
bu.globalturts(wn, player)
bu.initial_player_setup()
ts.screen_setup(wn, begin, exit, "Title Screen", BackgroundImage)
hideturts(wn)
wn.onclick(ts.screen_clicked) 
wn.update()

hideturts(wn)


wn.listen()
wn.mainloop()