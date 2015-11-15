#Filename: CSTProject2.py
#Description: The second project will play a game that involves a race car that will dodge objects
#based on the user's input
#Date: 3/25/15
#Version: 1
#Compiler: Python 3.4


import pygame
#To be able to use Pygame

import time
#To be able to import the time module

import random
#To be able to use the random function

pygame.init() 
#To use all of pygames features

#Background music for the game in a wav format
pygame.mixer.music.load('C:\\Users\\Joseph Molina\\Desktop\\project2\\instrumental.wav')

#This is the crash sound that will play when the user crashes
crash_sound = pygame.mixer.Sound("C:\\Users\\Joseph Molina\\Desktop\\project2\\crash.wav")


#Setting the frame of the game
display_width = 975
display_height = 650

#Variable declarations for the colors with their RGB values
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
green = (0,200,0)
blue = (0,0, 255)
orange = (255,128,0)
gray = (128,128,128)
silver = (192,192,192)
light_blue = (137,207,140)

#Setting the color of the blocks
block_color = (128,128,128)

#The width of the car
car_width = 73

#Will display the frame of window and sets the size of display
gameDisplay = pygame.display.set_mode((display_width,display_height))

#This will set the title of the window to Semester 2 Project
pygame.display.set_caption('Semester 2 Project')

#The game will have its own specific time clock from the computer system
clock = pygame.time.Clock()

#This line of code is the pygame function to load a picture file into the program
carImg = pygame.image.load('racecar.png')


#This will change the icon from the pygame icon into the race car icon
pygame.display.set_icon(carImg)


#Pause is set to false at the beginning because the game cannot be paused
pause = False



#This function will be the counter that will be displayed on the left corner of the screen
#It will increase the count of the counter by 1 each time a block is dodged
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    
#This function is responsible for displaying the image of the car to the screen
def car(x,y):
    gameDisplay.blit(carImg,(x,y))


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    #the rectangle around the text will be used to position the text
    return textSurface, textSurface.get_rect()


def message_display(text):
    #will display the message in the font selected and with the size of 115
    #This line of code only selects the font and size
    largeText = pygame.font.Font('freesansbold.ttf',88)
    
   #return to us the text surface and the text rectangle
    TextSurf, TextRect = text_objects(text, largeText)

    #These lines of code will make the text in the center of the screen
    #To make the words in the center, the width and height are divided by two
    # and then the words are displayed according to those results
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
    
#This function is for the crash that occurs throughout the game
#It is responsible for playing the crash sound of the game, for displaying
#the text that occurs when you crash, and for knowing when the crash actually occurs
def crash():


    pygame.mixer.music.stop()   #Will stop the background music
    pygame.mixer.Sound.play(crash_sound) #After the music is stoppped it will play the crash sound effect
    largeText = pygame.font.Font('freesansbold.ttf',80)
    TextSurf, TextRect = text_objects("You have crashed", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    
#to display the words in the font and with the width and height predetermined
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
        

        #This button will be used to loop through the game and will restart the game if clicked on
        #This button also highlights itself when the mouse is hovered over it
        button("PlayAgain",150,450,100,50,green,bright_green, game_loop)
        button("QUIT",550,450,100,50,red,bright_red, quitgame)

        
        pygame.display.update()

#The function will take in a message, a x and y coordinates, width and height, an interactive color, active color, and an action
def button(msg,x,y,w,h,ic,ac,action = None):
       #this will let the computer know where the mouse is on the screen
        mouse = pygame.mouse.get_pos()

        #will know when the mouse is clicked exactly
        click = pygame.mouse.get_pressed()

        
        #if the x coordinate and the width is greater than the mouse position
        # and the y location and the bottom of our box is greater than the y.
        if x+w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
            if click[0] ==1 and action != None:
                action()

        else:
             pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
             
        #will center the word go and dsiplay it into the button
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf,textRect = text_objects(msg, smallText)
        textRect.center = ((x +(w/2)),(y+(h/2)) )
        gameDisplay.blit(textSurf, textRect)

#This function will quit the game if called upon by clicking on the X.
def quitgame():
    pygame.quit()
    quit()

#This function will unpause the game and background music
def unpause():
    global pause
    #This line will stop the background from playing.
    pygame.mixer.music.unpause()
    pause = False
    
#This function will pause the game and the background music
def paused():
    
    pygame.mixer.music.pause()

    #This text will be shown to the display and will be centered
    largeText = pygame.font.Font('freesansbold.ttf',80)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #to display the words in the font and with the width and height predetermined    
        button("Continue",150,450,100,50,green,bright_green, unpause)
        button("QUIT",550,450,100,50,red,bright_red, quitgame)
        
        
        pygame.display.update()
        clock.tick(2)


#start menu for the user to see
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #to display the words in the font and with the width and height predetermined
                #This line will make the screen gray
        gameDisplay.fill(black)
        largeText = pygame.font.Font('freesansbold.ttf',80)
        TextSurf, TextRect = text_objects("Semester 2 Project", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        #To display my name in the game intro in the upper left hand corner
        smallText = pygame.font.Font('freesansbold.ttf',30)
        TextSurf, TextRect = text_objects("By:Joseph Molina", smallText)
        gameDisplay.blit(TextSurf, TextRect)


                                          

        #mediumText = pygame.font.Font('freesansbold.ttd',20)
        #TextSurf, TextRect = text_objects("Dodge the objects
                                    
    
        #These lines contain the code inside the buttons
        #The words being displayed on the button are "go" and will turn bright green when the mouse hovers over the button
        #The same goes for the quit button but instead will turn bright red when the mouse hovers over it.
        button("Go",150,450,100,50,green,bright_green, game_loop)
        button("QUIT",550,450,100,50,red,bright_red, quitgame)
        
        
        pygame.display.update()
        clock.tick(2)
    
def game_loop():
    global pause
    #An infinite loop for the background music to always play
    pygame.mixer.music.play(-1)
    
    #Will put the car in the center of the frame
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    
    #sets the position value of the car
    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thingCount = 1

    #The counter is initilized to 0
    dodged = 0

    gameExit = False
    
#The logic loop of events. Handles the events of the game
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: #if the left key is pressed x_change will be change which will cause the car to move to the left
                    x_change = -20
                if event.key == pygame.K_RIGHT: #if the right key is pressed x_change will be changed which will cause the car to move to the right
                    x_change = 20
                if event.key == pygame.K_SPACE: #if the space key is pressed the game will be paused
                    pause = True
                    paused()
                    
            #This loop is for when the key is released, the x_change will once again be 0 which will allow it to move again
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

                    
#Will change x which is the location of the car to the new location
        x += x_change

         #Will make the background of the frame white and the display the car with the given coordinates
        gameDisplay.fill(light_blue)

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)


        
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
        
#If the car goes over the screen it will cause a crash to occur and end the game
        if x > display_width - car_width or x < 0:
            crash()
            
#for the block to come into the screen and another one immideiately to show up
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
        #Will generate a random number from 0 to the size of the dispay which is 800
            thing_startx = random.randrange(0,display_width)
            dodged += 1
        
            
            #to increase the difficulty of the game
            thing_speed += .2
            thing_width += (dodged * .1)
            thing_height += (dodged * .2)
            
         #if statement to check if the incoming box has passed the racecar
        if y < thing_starty+thing_height:
            print('y crossover')
            
            #if statement for the crash
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()
                #If statements to display the current level the player is in
            if dodged == 0:
                largeText = pygame.font.Font('freesansbold.ttf',25)
                TextSurf, TextRect = text_objects("Level 1", largeText)
                TextRect.center = ((display_width/2), (display_height/2))
                gameDisplay.blit(TextSurf, TextRect)
                time.sleep(0.01)
                    
            if dodged == 12:
                largeText = pygame.font.Font('freesansbold.ttf',25)
                TextSurf, TextRect = text_objects("Entered Level 2", largeText)
                TextRect.center = ((display_width/2), (display_height/2))
                gameDisplay.blit(TextSurf, TextRect)
                time.sleep(0.01)
                
                
            if dodged == 25:
                largeText = pygame.font.Font('freesansbold.ttf',25)
                TextSurf, TextRect = text_objects("Entered Level 3", largeText)
                TextRect.center = ((display_width/2), (display_height/2))
                gameDisplay.blit(TextSurf, TextRect)
                time.sleep(0.01)
                
            if dodged == 35:
                largeText = pygame.font.Font('freesansbold.ttf',25)
                TextSurf, TextRect = text_objects("Entered Level 4", largeText)
                TextRect.center = ((display_width/2), (display_height/2))
                gameDisplay.blit(TextSurf, TextRect)
                time.sleep(0.01)

            if dodged == 45:
                largeText = pygame.font.Font('freesansbold.ttf',25)
                TextSurf, TextRect = text_objects("Entered Level 5", largeText)
                TextRect.center = ((display_width/2), (display_height/2))
                gameDisplay.blit(TextSurf, TextRect)
                time.sleep(0.01)
                
            if dodged == 55:
                largeText = pygame.font.Font('freesansbold.ttf',25)
                TextSurf, TextRect = text_objects("Entered Final Level", largeText)
                TextRect.center = ((display_width/2), (display_height/2))
                gameDisplay.blit(TextSurf, TextRect)
                time.sleep(0.01)
                
        #After painting the background and showing the car it will display the newly updated screen
        pygame.display.update()
         #Rate of times the frames will be refreshed
        clock.tick(60)


#Calling the functions that will initiate the game which are the game intro and the gameloop
game_intro()
game_loop()
#This line of code will quit the game if the user chooses to quit by closing the program or at the end of the game
pygame.quit()
quit()
