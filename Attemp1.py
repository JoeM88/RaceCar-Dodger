import pygame
#To be able to use Pygame
import time
#To be able to import the time module
import random
#To be able to use the random function

pygame.init() 
#To use all of pygames features

pygame.mixer.music.load('BackGround')

#Setting the frame of the game
display_width = 800
display_height = 600
#Variable declarations for the colors with their RGB values
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
green = (0,200,0)
blue = (0,0, 255)
orange = (255,128,0)

block_color = (53,115,255)

car_width = 73

#Will display the frame of window and sets the size of display
gameDisplay = pygame.display.set_mode((display_width,display_height))

#This will set the title of the window A bit Racey
pygame.display.set_caption('Semester 2 Project')

#The game will have its own specific time clock from the computer system
clock = pygame.time.Clock()

#This line of code is the pygame function to load a picture file into the program
carImg = pygame.image.load('racecar.png')


#This will change the icon from the pygame icon into the race car icon
pygame.display.set_icon(carImg)



pause = False
#crash = True


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    #the rectangle around the text will be used to position the text
    return textSurface, textSurface.get_rect()

def message_display(text):
    #will display the message in the font selected and with the size of 115
    #This line of code only selects the font and size
    largeText = pygame.font.Font('freesansbold.ttf',88)
    
   #return to us the text surface and the text rectangle
    TextSurf, TextRect = text_objects(text, largeText)

    #will make the text in the center of the screen
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
    

def crash():

    largeText = pygame.font.Font('freesansbold.ttf',80)
    TextSurf, TextRect = text_objects("You have crashed", largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #to display the words in the font and with the width and height predetermined
        #gameDisplay.fill(white)
        

        
        button("Play Again",150,450,100,50,green,bright_green, game_loop)
        button("QUIT",550,450,100,50,red,bright_red, quitgame)
        

        #pygame.draw.rect(gameDisplay, red, (550,450,100,50))
        
        pygame.display.update()

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
##                if action == "play":
##                    game_loop()
##                elif action == "quit":
##                    pygame.quit()
##                    quit()
        else:
             pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
             
        #will center the word go and dsiplay it into the button
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf,textRect = text_objects(msg, smallText)
        textRect.center = ((x +(w/2)),(y+(h/2)) )
        gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False

def paused():

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
        #gameDisplay.fill(white)
        

        
        button("Continue",150,450,100,50,green,bright_green, unpause)
        button("QUIT",550,450,100,50,red,bright_red, quitgame)
        

        #pygame.draw.rect(gameDisplay, red, (550,450,100,50))
        
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
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',80)
        TextSurf, TextRect = text_objects("Semester 2 Project", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        
        button("Go",150,450,100,50,green,bright_green, game_loop)
        button("QUIT",550,450,100,50,red,bright_red, quitgame)
        

        #pygame.draw.rect(gameDisplay, red, (550,450,100,50))
        
        pygame.display.update()
        clock.tick(2)
    
def game_loop():
    global pause
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
                    x_change = -5
                if event.key == pygame.K_RIGHT: #if the right key is pressed x_change will be changed which will cause the car to move to the right
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                    
            #This loop is for when the key is released, the x_change will once again be 0 which will allow it to move again
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

                    
#Will change x which is the location of the car to the new location
        x += x_change

         #Will make the background of the frame white and the display the car with the given coordinates
        gameDisplay.fill(white)

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
            thing_speed += 1
            thing_width += (dodged * 1.2)
            
         #if statement to check if the incoming box has passed the racecar
        if y < thing_starty+thing_height:
            print('y crossover')
            
            #if statement for the crash
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()
        #After painting the background and showing the car it will display the newly updated screen
        pygame.display.update()
         #Rate of times the frames will be refreshed
        clock.tick(60)
#This line of code will quit the game if the user chooses to quit by closing the program or at the end of the game
game_intro()
game_loop()
pygame.quit()
quit()
