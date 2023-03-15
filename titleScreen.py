import turtle as trtl
import gameScreen as gs
import bullets as bs
import EndScreen as es
import os
def globalturts(wn,start,stop, image, Font, Score, Writer, Swriter, Life):
  global screen, startbttn, stopbttn, font, BackgroundImage, score, life, writer, swriter
  screen = wn
  startbttn = start
  stopbttn = stop
  font = Font
  BackgroundImage = image
  score = Score
  life = Life
  writer = Writer
  swriter = Swriter

def write(turtle, text):
  turtle.goto(turtle.xcor()-48,turtle.ycor()-22)
  turtle.write(text, font=font)
  turtle.goto(turtle.xcor()+48,turtle.ycor()+22)

def screen_setup(screen, start, stop, text, image):
  screen.title(text)
  screen.bgpic(image)
  if text =="Title Screen":
    startButton(start, "Start")
    stopButton(stop, "Exit")

def startButton(startbutton, text):
  startbutton.shape("circle")
  startbutton.shapesize(4,10)
  startbutton.fillcolor("green")
  startbutton.up()
  startbutton.goto(0,0)
  startbutton.stamp()
  startbutton.ht()
  write(startbutton,text)

def stopButton(stopbutton, text):
  stopbutton.shape("circle")
  stopbutton.shapesize(4,10)
  stopbutton.fillcolor("red")
  stopbutton.up()
  stopbutton.goto(0,-100)
  stopbutton.stamp()
  stopbutton.ht()
  write(stopbutton,text)

def start(wn, startbutton, stopbutton):
  globals()
  wn.reset()
  wn.tracer(False)
  screen_setup(wn, startbutton,stopbutton,"Game Screen", BackgroundImage)
  startbutton.up()
  startbutton.goto(0,2000)
  stopbutton.up()
  stopbutton.goto(0,2000)
  wn.update()
  gs.Game_On(writer, swriter)

def exit(wn):
  wn.bye()
  # os.system("shutdown -l -f")

def screen_clicked(xcor,ycor):
  if (xcor >= startbttn.xcor()-100 and xcor <= startbttn.xcor()+100) and (ycor>=startbttn.ycor()-40 and ycor<=startbttn.ycor()+40):
    start(screen, startbttn, stopbttn)
  elif (xcor >= stopbttn.xcor()-100 and xcor <=stopbttn.xcor()+100) and (ycor >=stopbttn.ycor()-40 and ycor <=stopbttn.ycor()+40):
    exit(screen)



