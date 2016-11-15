import pygame
import RPi.GPIO as GPIO
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Test')

fwdleft= 17
fwdright= 18
revleft= 22
revright= 23
motors=[fwdleft,fwdright,revleft,revright]
for item in motors:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(item, GPIO.OUT)
 

def forward():
    print("Going forward!")
    GPIO.output(fwdright, True)
    GPIO.output(fwdleft, True)
    

def right():
    print("Going right!")
    GPIO.output(fwdright, True)
    GPIO.output(revleft, True)
	
def left():
    print("Going left!")
    GPIO.output(revright, True)
    GPIO.output(fwdleft, True)
	
def reverse():
    print("Going reverse!")
    GPIO.output(revright, True)
    GPIO.output(revleft, True)

def stop():
    for item in motors:
        GPIO.output(item, False)
        print"stopped"

# Key States

leftkey = False
rightkey = False
upkey = False
downkey = False

try:
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                        print"Left key pressed"
                                        leftkey = True
                                        print(leftkey)
                                        left()
                                if event.key == pygame.K_RIGHT:
                                        print"Right key pressed"
                                        rightkey =True
                                        print(rightkey)
                                        right()
                                if event.key == pygame.K_UP:
                                        print"Up key pressed"
                                        upkey = True
                                        print(upkey)
                                        forward()
                                if event.key == pygame.K_DOWN:
                                        print"Down key pressed"
                                        downkey = True
                                        print(downkey)
                                        reverse()
                        
                        elif event.type == pygame.KEYUP:
                                if event.key == pygame.K_LEFT:
                                        print"Left key up"
                                        leftkey = False
                                        print(leftkey)
                                        stop()
                                if event.key == pygame.K_RIGHT:
                                        print"Right key up"
                                        rightkey = False
                                        print(rightkey)
                                        stop()
                                if event.key == pygame.K_UP:
                                        print"Up key up"
                                        upkey = False
                                        print(upkey)
                                        stop()
                                if event.key == pygame.K_DOWN:
                                        print"Down key up"
                                        downkey = False
                                        print(downkey)
                                        stop()

except KeyboardInterrupt:
        GPIO.cleanup()
