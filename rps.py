# File created by: kasdan blattman

# Source: Pygame.org

# import libraries
from time import sleep
from random import randint
import pygame as pg
import os

choices = ["rock","paper","scissors"]

def RESULT(computer, player):
    if player == computer:
        return("We chose the same thing, We have tied")
    # lines 17-33 are all the winning-losing scenarios of the game, pretty much telling the computer how to play the game    
    elif player == "rock":
        if computer == "scissors":
            return("You chose rock, computer chose scissors; you win")
        elif computer == "paper":
            return("You chose rock, computer chose paper; you lose")
    elif player == "scissors":
        if computer == "paper":
            return("You chose scissors, computer chose paper; you win")
        elif computer == "rock":
            return("You chose scissors, computer chose rock; you lose")
    elif player == "paper":
        if computer == "rock":
            return("You chose paper, computer chose rock; you win")
        elif computer == "scissors":
            return("You chose paper, computer chose scissors; you lose")                  
    else:
        return "Error"

def guess():
    result = choices[randint(0,2)]
    return result  

def render_message(text): 
    m = font.render(text, True, BLACK)
    m_rect = m.get_rect()
    m_rect.top = screen_rect.bottom - (m_rect.bottom - m_rect.top)
    return (m, m_rect)

# setup asset folders - images and sounds
game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 1100
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (255, 255, 255)
BLUE = (255, 255, 255)

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen_rect = screen.get_rect()

pg.display.set_caption("Rock Paper Scissors...")
clock = pg.time.Clock()

# # sounds
#scissors_sound = pg.mixer.Sound(os.path.join(game_folder, "scissors.wav"))

rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
# creates transparency 
rock_image.set_colorkey(GREEN)
paper_image.set_colorkey(GREEN)
scissors_image.set_colorkey(GREEN)

# gets the shape of the image
rock_rect = rock_image.get_rect()
paper_rect = paper_image.get_rect()
# places the images next to each other
scissors_rect = scissors_image.get_rect()
paper_rect.left = rock_rect.right
scissors_rect.left = paper_rect.right

font = pg.font.SysFont(None,48)
(message, message_rect) = render_message("Select rock paper or scissors!!!")

#Computer guess is variable that returns 1 of 3 possible guesses of rock, paper, scissors
computer_guess = guess()

#if game is running, do this...
running = True
while running:
    clock.tick(FPS)
   
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            mouse_coords = pg.mouse.get_pos()
            # print(mouse_coords)
            # print(mouse_coords[0])
            # print(mouse_coords[1])
            if rock_rect.collidepoint(mouse_coords):
                #calls function to compare computer choice and user choice (RESULT)
                result = RESULT(computer_guess, "rock")
                # returns the message and the rect (location) of the text, 
                # then displays the result of comparing user choice and computer choice
                (message, message_rect) = render_message(result)  
                #returning rock, paper, or scissors: selects the next computer guess
                computer_guess = guess()
            elif paper_rect.collidepoint(mouse_coords):
                result = RESULT(computer_guess, "paper")
                (message, message_rect) = render_message(result)  
                computer_guess = guess()              
            elif scissors_rect.collidepoint(mouse_coords):
                result = RESULT(computer_guess, "scissors")
                (message, message_rect) = render_message(result)  
                computer_guess = guess()              
               

           
            # if mouse_coords[0] <= 300 and mouse_coords[1] <= 300:
            # # if mouse_coords == pg.mouse.get_pos():
            #     print("I clicked on the rock...")
    
    # get input from player...

    # update
    # rock_rect.y += 1
    # paper_rect.y += 1
    # scissors_rect.x += 1
    # scissors_rect.y += 1
    
    # screen fill "resets" the screen, blit is drawing the images on the screen
    screen.fill(WHITE)
    screen.blit(scissors_image, scissors_rect)
    screen.blit(paper_image, paper_rect)
    screen.blit(rock_image, rock_rect)
    screen.blit(message, message_rect)
    

    pg.display.flip()

pg.quit()
