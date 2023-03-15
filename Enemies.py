import turtle as trtl
import random as rand
import gameScreen as gs
import bullets as bs



def globalVariables(wn, Life, Score, Hscore):
  global numbZagging, angle, DirectShape, indirectShape, activeDirectList, activeIndirectList, inactiveDirectList, inactiveIndirectList, gameactive, alienKilled, screen, life, score, hscore
  numbZagging = 0
  angle = 325
  score = Score
  screen = wn
  DirectShape = "Direct.gif"
  screen.addshape(DirectShape)
  indirectShape = "indirect.gif"
  screen.addshape(indirectShape)
  life = Life
  hscore = Hscore
  activeDirectList = []
  activeIndirectList = []
  inactiveDirectList = []
  inactiveIndirectList = []

  gameactive = True
  alienKilled = False

def alien_creator():
  global numbZagging, angle, DirectShape, indirectShape, activeDirectList, activeIndirectList, inactiveDirectList, inactiveIndirectList, gameactive, alienKilled, screen
  num = 0

  for aliens in range(8):
    alienCreature = trtl.Turtle()
    alienCreature.penup()
    alienCreature.goto(rand.randrange(-750, 750), 350)
    alienCreature.seth(270)
    alienCreature.speed(2)

    if num < 4:
      alienCreature.shape(DirectShape)
      alienCreature.ht()
      inactiveDirectList.append(alienCreature)
    else:
      alienCreature.shape(indirectShape)
      alienCreature.ht()
      inactiveIndirectList.append(alienCreature)

    num += 1

  randomAlienNum = rand.randrange(0,4)
  for aliens in range(randomAlienNum):
    alienCreature = inactiveDirectList.pop()
    activeDirectList.append(alienCreature)
    alienCreature.st()

  for aliens in range(4 - randomAlienNum):
    alienCreature = inactiveIndirectList.pop()
    activeIndirectList.append(alienCreature)
    alienCreature.st()
  screen.update() 

def DestroyAndRegenerate(writer, font, swriter):
  global numbZagging, angle, DirectShape, indirectShape, activeDirectList, activeIndirectList, inactiveDirectList, inactiveIndirectList, gameactive, alienKilled, screen, life, score, hscore
  gs.globalturts1(life, score, hscore)
  # direct aliens
  aliencount = 0
  for alienCreature in activeDirectList:
    count = 0
    if (alienCreature.ycor() < -350):
      alienCreature.goto(rand.randrange(-750, 750), 350)
      inactiveDirectList.append(activeDirectList.pop(aliencount))
      alienCreature.ht()
      life-=1
    for laser in bs.laser_active:
      alienDeath(laser, count, aliencount, 0)
      count +=1

      if alienKilled==True:
        alienCreature.goto(rand.randrange(-750, 750), 350)
        inactiveDirectList.append(activeDirectList.pop(aliencount))
        alienCreature.ht()
        alienKilled = False
        continue
    aliencount+=1
    regen(alienCreature, activeDirectList,inactiveDirectList,activeIndirectList,inactiveIndirectList)  
    gs.lifeWriter(writer, life, font)
    gs.scoreWriter(swriter, score, font)
# indirect aliens
  alienCount = 0
  for alienCreature in activeIndirectList:
    count = 0
    if (alienCreature.ycor() < -350):
      alienCreature.goto(rand.randrange(-750, 750), 350)
      inactiveIndirectList.append(activeIndirectList.pop(alienCount))
      alienCreature.ht()
      life-=1
    for laser in bs.laser_active:
      alienDeath(laser, count, alienCount,1)
      count +=1

      if alienKilled==True:
        alienCreature.goto(rand.randrange(-750, 750), 350)
        inactiveIndirectList.append(activeIndirectList.pop(alienCount))
        alienCreature.ht()
        alienKilled = False
        continue
    alienCount+=1

    regen(alienCreature, activeDirectList,inactiveDirectList,activeIndirectList,inactiveIndirectList)  
  gs.lifeWriter(writer, life, font)
  gs.scoreWriter(swriter, score, font)

def regen(alienCreature, activeDirectList, inactiveDirectList, activeIndirectList, inactiveIndirectList):
  regen = rand.randrange(0,2)
  if (len(activeDirectList)+len(activeIndirectList) < 4):
    if (regen == 0) and (len(inactiveDirectList) > 0):
      alienCreature = inactiveDirectList.pop()
      activeDirectList.append(alienCreature)
      alienCreature.st()

    elif (regen == 1) and (len(inactiveIndirectList) > 0):
      alienCreature = inactiveIndirectList.pop()
      activeIndirectList.append(alienCreature)
      alienCreature.st()

def Zagging():
  global numbZagging, angle, DirectShape, indirectShape, activeDirectList, activeIndirectList, inactiveDirectList, inactiveIndirectList, gameactive, alienKilled, screen

  numbZagging += 1
  for alienCreature in activeIndirectList:
    alienCreature.seth(angle)
    alienCreature.forward(2)
    if numbZagging == 50:
      angle = 215
    elif numbZagging == 100:
      angle = 325
      numbZagging = 0
    
    if alienCreature.xcor() <= -750 or alienCreature.xcor() >= 750:
      if angle == 215:
        angle = 325
      elif angle == 325:
        angle = 215
      numbZagging = 0      

def Straight():
  global numbZagging, angle, DirectShape, indirectShape, activeDirectList, activeIndirectList, inactiveDirectList, inactiveIndirectList, gameactive, alienKilled, screen

  for alienCreature in activeDirectList:
    alienCreature.forward(1)

def alienDeath(player_laser,count, Index, num):
  global numbZagging, angle, DirectShape, indirectShape, activeDirectList, activeIndirectList, inactiveDirectList, inactiveIndirectList, gameactive, alienKilled, screen, score
  index = Index

  if num ==0 and len(activeDirectList)>Index:
    if abs(player_laser.xcor()-activeDirectList[index].xcor()) < 60 and abs(player_laser.ycor()-activeDirectList[index].ycor()) < 75:
      alienKilled = True 
      bs.resetLaser(player_laser, count)
      score+=1
  elif num ==1 and len(activeIndirectList)>index:
    if abs(player_laser.xcor()-activeIndirectList[index].xcor()) < 60 and abs(player_laser.ycor()-activeIndirectList[index].ycor()) < 75:
      alienKilled = True
      bs.resetLaser(player_laser, count)
      score +=1
  return score





#MARCEL HUCHWAJDA