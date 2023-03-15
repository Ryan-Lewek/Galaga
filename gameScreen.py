# import player file
import Enemies as en
import EndScreen as es
import turtle as trtl
import bullets as bs 

def globalturts(wn,start,stop, image, Font, Score, Writer, Swriter,Life, Hscore, Hswriter):
  global screen, startbttn, stopbttn, font, BackgroundImage, score, life, writer, swriter, hscore, hswriter
  screen = wn
  startbttn = start
  stopbttn = stop
  font = Font
  BackgroundImage = image
  score = Score
  life = Life
  writer = Writer
  swriter = Swriter
  hscore = Hscore
  hswriter = Hswriter

def globalturts1(Life, Score, Hscore):
  global life, score, hscore
  life = Life
  score = Score
  hscore = Hscore

def gameSetup():
  globals()
  en.alien_creator()
  bs.player_setup()
  lifeWriter_setup(writer, life, font)
  scoreWriter_setup(swriter, score, font)
  screen.update()

def lifeWriter_setup(writer, life, font):
  writer.up()
  writer.ht()
  writer.goto(775,450)
  writer.color("white")
  writer.write("Lives: " + str(life), font=font)

def scoreWriter_setup(swriter, score, font):
  swriter.up()
  swriter.ht()
  swriter.goto(750,350)
  swriter.color("white")
  swriter.write("Score: " + str(score), font=font)

def scoreWriter(swriter, score, font):
  swriter.clear()
  swriter.write("Score: " + str(score), font=font)

def HighscoreWriter(hswriter, score, font):
  global hscore
  hswriter.clear()
  hswriter.up()
  hswriter.goto(-900,450)
  if score>hscore:
    hscore = score
  hswriter.write("High Score: " + str(hscore), font=font)
  
def lifeWriter(writer, life, font):
  writer.clear()
  writer.write("Lives: " + str(life), font=font)

def Game_On(writer, swriter):
  global life, score, hscore
  life = 3
  score = 0
  es.hideturts(screen)
  en.globalVariables(screen, life,score, hscore)
  gameSetup()
  screen.update()
  game_active = True
  while(game_active ==True):
    # enemy calls
    en.Zagging()
    en.Straight()
    en.DestroyAndRegenerate(writer, font, swriter)
    bs.move_bullet()
    screen.update()
    # player calls
    screen.onkeypress(bs.move_left, "Left")
    screen.onkeypress(bs.move_right, "Right")
    screen.onkeypress(bs.shoot_bullet, "space")
    if life <= 0:
      game_active = False
      writer.clear()
      swriter.clear()
      Game_Over()

def Game_Over():
  globals()
  screen.reset()
  screen.tracer(False)
  for turtle in screen.turtles():
    turtle.ht()
    turtle.up()
    turtle.goto(0,1000)
  HighscoreWriter(hswriter, score, font)
  
  if score >= 10:
    es.win(screen, startbttn, stopbttn)
  else:
    es.lose(screen, startbttn, stopbttn)

