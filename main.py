#Tania Mouline
#Game Design with Python
#Period 2
#1/27/22
#This program is a game with a penguin that eats a fish

import pygame, sys, random

from pygame.locals import*

pygame.init()

#variables that do not change (colors, sizes)
SCREENWIDTH = 500
SCREENHEIGHT = 300
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
SKY = (199,243,255)
INFINITY = 99
FISHBOXX = 50
FISHBOXY = 50
PENGUINBOXX = 70
PENGUINBOXY = 65
PAUSEDURATION = 0

#defines most variables in the game and executes the methods
def game():
  global screen, level
  screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
  clock = pygame.time.Clock()
  fps = 70
  level = 0
  global penguinImage, penguinX, penguinY, penguinHitBox
  penguinImage = pygame.image.load("murderous.penguin.png")
  penguinImage = pygame.transform.scale(penguinImage,(PENGUINBOXX, PENGUINBOXY))
  penguinX = SCREENWIDTH - PENGUINBOXX
  penguinY = random.randint(0,SCREENHEIGHT - PENGUINBOXY)
  penguinHitBox = pygame.Rect(penguinX,penguinY,PENGUINBOXX,PENGUINBOXY)
  global fishImage, fishX, fishY, fishHitBox
  fishImage = pygame.image.load("fish.png")
  fishImage = pygame.transform.scale(fishImage,(FISHBOXX,FISHBOXY))
  #fishX = SCREENWIDTH - 60
  fishX = random.randint(0,SCREENWIDTH - FISHBOXX)
  fishY = random.randint(0,SCREENHEIGHT - FISHBOXY)
  fishHitBox = pygame.Rect(fishX,fishY,FISHBOXX,FISHBOXY)
  global fishSpeed, penguinSpeed, slope, direction
  fishSpeed = 2
  penguinSpeed = 2
  direction = -1
  global score
  score = 0
  slope = 1
  #x = 1
  drawScene()
  while True:
    if level == 0:
      #draw the screen
      #named the screen "business card"
      score = 0
      menu() 
      pickGameMode() 
      #update the game staticmethod
      pygame.display.update() 
      clock.tick(fps)
    if level == 1:
      #draw the screen
      #named the screen "business card"
      singlePlayer()
      reachScore()
      #update the game staticmethod
      pygame.display.update() 
      clock.tick(fps)
    if level == 2:
      #draw the screen
      #named the screen "business card"
      multiPlayer()
      #update the game staticmethod
      pygame.display.update() 
      clock.tick(fps)

def wait():
 while True:
  for event in pygame.event.get():
   if event.type == QUIT:
    pygame.quit()
    sys.exit()
   if event.type == KEYDOWN and event.key == K_x:
     return
#once score
def reachScore():
  global level, score
  if score >= 30:
    singleGameOver()
    level = 0

def singleGameOver():
  global screen, level
  drawScene()
  screen.fill(SKY)
  fontObj = pygame.font.SysFont('dejavusansmono', 30)
  textSurfaceObj = fontObj.render('GAME OVER', True, BLACK, SKY)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (250,90)
  screen.blit(textSurfaceObj, textRectObj)
  fontObj = pygame.font.SysFont('dejavusansmono', 20)
  textSurfaceObj = fontObj.render('press X to return to home screen', True, BLACK, SKY)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (250,150)
  screen.blit(textSurfaceObj, textRectObj)
  pygame.display.update()
 
  #clock.tick(fps)
  wait()
  #key = pygame.key.get_pressed()
  #while not key[pygame.K_x]:
    #key = pygame.key.get_pressed()
    #print (key)
  level = 0
   
def menu():
  global screen
  drawScene()
  pygame.display.set_caption('Hungry Penguin')
  #renders title
  fontObj = pygame.font.SysFont('dejavusansmono', 30)
  textSurfaceObj = fontObj.render('Welcome to Hungry Penguin!', True, BLACK, SKY)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (250,30)
  screen.blit(textSurfaceObj, textRectObj)
  #renders options
  fontObj = pygame.font.SysFont('dejavusansmono', 20)
  textSurfaceObj = fontObj.render('for singleplayer mode: press 1', True, BLACK,SKY)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (250,90)
  screen.blit(textSurfaceObj, textRectObj)
 
  fontObj = pygame.font.SysFont('dejavusansmono', 20)
  textSurfaceObj = fontObj.render('for multiplayer mode: press 2', True, BLACK,SKY)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (250,150)
  screen.blit(textSurfaceObj, textRectObj)
  
  fontObj = pygame.font.SysFont('dejavusansmono', 15)
  textSurfaceObj = fontObj.render('to control penguin, use arrow keys', True, BLACK,SKY)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (250,210)
  screen.blit(textSurfaceObj, textRectObj)

  fontObj = pygame.font.SysFont('dejavusansmono', 15)
  textSurfaceObj = fontObj.render('to control fish, use W A S D', True, BLACK,WHITE)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (250,270)
  screen.blit(textSurfaceObj, textRectObj)
 #draws blue sky and snow
def drawScene():
  global screen
  screen.fill(SKY)
  pygame.draw.rect(screen,WHITE,(0,SCREENHEIGHT -50,SCREENWIDTH,50),0)

#draws the penguin and gives it a hitbox
def drawPenguin():
  global penguinImage, penguinX, penguinY, penguinHitBox
  screen.blit(penguinImage,(penguinX,penguinY))
  penguinHitBox = pygame.Rect(penguinX,penguinY,PENGUINBOXX, PENGUINBOXY-8)
  #pygame.draw.rect(screen,RED,penguinHitBox,1)

#draws the fish and gives it a hitbox
def drawFish():
  global fishImage, fishX, fishY, fishHitBox  
  screen.blit(fishImage,(fishX,fishY))
  fishHitBox = pygame.Rect(fishX,fishY,FISHBOXX, FISHBOXY)
  #pygame.draw.rect(screen,RED,fishHitBox,1)

#lets you use the up, down, left, and right keys to move the penguin
def handlePenguinKeyboardEvents():
  global penguinX, penguinY, fishX, fishY, penguinSpeed, level
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  # when keys are pressed, they make the penguin move in assigned diresctions, O and P change the Penguin's speed
  key = pygame.key.get_pressed()
  if key[pygame.K_DOWN] and penguinY + PENGUINBOXY< SCREENHEIGHT:
    penguinY = penguinY + penguinSpeed
  if key[pygame.K_UP] and penguinY > 0:
    penguinY = penguinY - penguinSpeed
  if key[pygame.K_LEFT] and penguinX > 0:
    penguinX = penguinX - penguinSpeed
  if key[pygame.K_RIGHT] and penguinX + PENGUINBOXX  < SCREENWIDTH:
    penguinX = penguinX + penguinSpeed
  if key[pygame.K_o]:
    penguinSpeed = penguinSpeed + 1
  if key[pygame.K_p]:
    penguinSpeed = max(penguinSpeed - 1,1)
  if key[pygame.K_x]:
    level = 0

#lets a second player use W, A, S, and D to move the fish
def handleFishKeyboardEvents():
  global penguinX, penguinY, fishX, fishY, fishSpeed
  #fish penguin keyboard events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  # when keys are pressed, they make the fish move in assigned diresctions
  key = pygame.key.get_pressed()
  if key[pygame.K_w] and fishY > 0:
    fishY = fishY - fishSpeed
  if key[pygame.K_s] and fishY + FISHBOXX< SCREENHEIGHT:
    fishY = fishY + fishSpeed
  if key[pygame.K_a] and fishX > 0:
    fishX = fishX - fishSpeed
  if key[pygame.K_d] and fishX + FISHBOXX  < SCREENWIDTH:
    fishX = fishX + fishSpeed

def singlePCollisions():
  global penguinHitBox, fishHitBox, fishX, fishY, score, slope
  #if the penguin and fish collide, then the fish will respawn at a random location
  if penguinHitBox.colliderect(fishHitBox):
   fishX = random.randint(0, SCREENWIDTH + FISHBOXX)
   fishY = random.randint(0, SCREENHEIGHT - FISHBOXY)
   fishHitBox = pygame.Rect(fishX, fishX, FISHBOXX, FISHBOXY)
   score = score + 1 
  fontObj = pygame.font.SysFont('dejavusansmono', 20)
  message = 'score = ' + str(score)
  
  textSurfaceObj = fontObj.render(message, True, SKY,BLACK) 
  #obtains rectangle object that represents the text
  textRectObj = textSurfaceObj.get_rect()
  #positions rectangle 
  textRectObj.center = (70,15)
  #shows the rectangle on the screen
  screen.blit(textSurfaceObj, textRectObj) 

#when the hitbox of the fish and penguin collide, the fish spawns in a new place and the score changes
def multiPCollisions():
  global penguinHitBox, fishHitBox, fishX, fishY, score, slope
  if penguinHitBox.colliderect(fishHitBox):
   fishX = random.randint(0, SCREENWIDTH + FISHBOXX)
   fishY = random.randint(0, SCREENHEIGHT - FISHBOXY)
   fishHitBox = pygame.Rect(fishX, fishX, FISHBOXX, FISHBOXY)
   score = score + 1 
  fontObj = pygame.font.SysFont('dejavusansmono', 20)
  message = 'score = ' + str(score)
  
  textSurfaceObj = fontObj.render(message, True, SKY,BLACK) 
  #obtains rectangle object that represents the text
  textRectObj = textSurfaceObj.get_rect()
  #positions rectangle 
  textRectObj.center = (55,15)
  #shows the rectangle on the screen
  screen.blit(textSurfaceObj, textRectObj) 

#when the fish hits any borders, the slope changes to go in a different direction
def moveFish():
  global fishX, fishY, fishSpeed, slope
  fishX = fishX + fishSpeed
  fishY = fishY + fishSpeed * slope
  if fishY < 0:
    slope = -slope
  if fishX < 0:
    slope = -slope
    fishX = 0
    fishSpeed = -fishSpeed
  if fishX + FISHBOXX >= SCREENWIDTH:
    slope = -slope
    fishX = SCREENWIDTH - FISHBOXX
    fishSpeed = -fishSpeed
  if fishY + FISHBOXY >= SCREENHEIGHT:
    slope = -slope

#when the fish hits the X axis borders, the fish goes around to the other side
def fishTeleport():
  global  penguinX, penguinY, fishX, fishY, fishSpeed
  key = pygame.key.get_pressed()
  if key[pygame.K_a]:
    if fishX > - FISHBOXX:
      fishX = fishX - fishSpeed
    else:
      fishX = SCREENWIDTH - FISHBOXX
  if key[pygame.K_d]:
    if fishX > SCREENWIDTH:
      fishX = 0
    else:
      fishX = fishX + fishSpeed

def countdown():
  global screen, font
  counter, text = 10, '10'.rjust(3)
  clock = pygame.time.Clock()
  pygame.time.set_timer(pygame.USEREVENT, 1000)
  fontObj = pygame.font.SysFont('dejavusansmono', 20)
  run = True
  while run:
      for e in pygame.event.get():
          if e.type == pygame.USEREVENT: 
              counter -= 1
              text = str(counter).rjust(3) if counter > 0 else 'boom!'
          if e.type == pygame.QUIT: 
              run = False
      screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
      pygame.display.flip()
      clock.tick(60)

def singlePlayer():
  drawScene() 
  drawPenguin() 
  drawFish() 
  handlePenguinKeyboardEvents() 
  singlePCollisions() 
  moveFish()

def multiPlayer():
  drawScene() 
  drawPenguin()
  drawFish() 
  handlePenguinKeyboardEvents()
  handleFishKeyboardEvents()
  multiPCollisions()
  fishTeleport()

def pickGameMode():
  global penguinX, penguinY, fishX, fishY, level
  #fish penguin keyboard events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  key = pygame.key.get_pressed()
  if key[pygame.K_x]:
    level = 0
  if key[pygame.K_1]:
    level = 1
  if key[pygame.K_2]:
    level = 2 
  if key[pygame.K_3]:
    level = 3 

#to do list:
# make a third gamemode for the fish teleport thing
# add fishspeed and 
game()