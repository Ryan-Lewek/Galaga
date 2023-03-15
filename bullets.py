# Miguel Rimer-Surles

import turtle as trtl
import time
import Enemies as en
# global variables
font = "Arial", 30, "bold"



# title screen variables
#---------------------------------
game_active = False
#---------------------------------

def globalturts(wn, Player):
  global screen, laser_active, laser_inactive, player
  screen = wn
  wn.addshape("PlayerImage.gif")
  wn.addshape("playerLaser.gif")
  laser_active = []
  laser_inactive = []
  player = Player

def initial_player_setup():
  global player, laser_inactive
  player.up()
  player.goto(0,2000)
  for i in range(3):
    laser = trtl.Turtle()
    laser_inactive.append(laser)
    laser.up()
    laser.goto(player.xcor(),player.ycor()+50)

def move_left():
  if player.xcor()>-900:
    player.goto(player.xcor()-10,player.ycor())
def move_right():
  if player.xcor()<900:
    player.goto(player.xcor()+10,player.ycor())
def move_bullet():
  count = 0
  for laser in laser_active:
    laser.st()
    laser.goto(laser.xcor(),laser.ycor()+5)
    if laser.ycor()>=350:
      laser_inactive.append(laser)
      laser_active.pop(count)
      count +=1
  for laser in laser_inactive:
    laser.ht()
    laser.goto(player.xcor(),player.ycor())
    
def shoot_bullet():
  if len(laser_active)<3:
    laser_active.append(laser_inactive.pop())

def resetLaser(laser, count):
  laser.ht()
  laser.goto(player.xcor(), player.ycor())
  laser_inactive.append(laser_active.pop(count))


def player_setup():
  global player, laser_inactive
  player.up()
  player.goto(0,-400)
  player.shape("PlayerImage.gif")
  player.st()

  for laser in laser_inactive:
    laser.up()
    laser.goto(player.xcor(), player.ycor()+50)
    laser.shape("playerLaser.gif")
    laser.ht()

#---------------------------------

# function calls
