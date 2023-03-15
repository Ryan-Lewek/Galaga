# imports
import turtle as trtl
import titleScreen as ts

# images
winImage = "BolenApproval.gif"
loseImage = "BolenDisapproval.gif"


def hideturts(wn):
  for turt in wn.turtles():
    turt.ht()
    turt.up()


# get turtles/variables to use throughout the game
def globalturts(wn,start,stop, Font):
  global screen, startbttn, stopbttn, font, winImage, loseImage
  screen = wn
  startbttn = start
  stopbttn = stop
  font = Font

# win condition
def win(screen, startbttn, stopbttn):
  globals()
  screen.title("End Screen")
  screen.bgpic(winImage)
  hideturts(screen)
  next_steps(startbttn, stopbttn)
  screen.update()
  
# lose condition
def lose(screen, startbttn, stopbttn):
  globals()
  screen.title("End Screen")
  screen.bgpic(loseImage)
  hideturts(screen)
  next_steps(startbttn, stopbttn)
  screen.update()

# play again
def next_steps(startbttn, stopbttn):
  globals()
  ts.startButton(startbttn, "Replay")
  ts.stopButton(stopbttn, "Exit")

