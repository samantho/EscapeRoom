import pygame, pygame_menu
from GameRoom import *
from TutorialGame import *

pygame.init()
surface = pygame.display.set_mode((800,600))

level = 'Hard'
teamname = 'Hacker Squad'

def team_name(name):
    global teamname
    teamname = name
    
def set_difficulty(value, difficulty):
    global level
    level = value[0]

def start_game():
    if level == 'Easy':
        print('Begin Tutorial Game')
        start_tutorial(teamname) # from TutorialGame
    if level == 'Hard':
        print('Begin Main Game')
        begin_room1(teamname) # from Room1

menu_theme = pygame_menu.themes.THEME_DARK.copy()
menu_theme.background_color = pygame_menu.baseimage.BaseImage(
    image_path="coding_menu.png",
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY
)

menu = pygame_menu.Menu(600, 800, 'Escape Room',
                       theme=menu_theme)

menu.add_text_input('Team Name : ', default=' Hacker Squad', onchange=team_name)
menu.add_selector('Difficulty : ', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add_button('Enter Room', start_game)
menu.add_button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
