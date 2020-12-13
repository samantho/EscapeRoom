import pygame
import pygame_menu
import tkinter as tk
from GameRoom import *

pygame.display.set_caption('Escape Room')
team_name = 'Hacker Squad'

def generate_popup(clue, title, correct, unlocked):    
    global team_name
    # popup setup
    root = tk.Tk()
    root.title(clue)
    root.geometry("300x200")
    ans_var = tk.StringVar()

    # popup submission
    def submit():
        answer = ans_var.get()
        print("The answer submitted is : " + answer)
        if answer.lower() == correct.lower():
            print("That's the answer!!!")
            ans_var.set(correct)
            display = tk.Label(root, text = unlocked)
            display.grid(row=5,column=1)
        else:
            ans_var.set("")

    # popup display
    message = tk.Label(root, text = title)
    ans_entry = tk.Entry(root, textvariable = ans_var, font = ('calibre',10,'normal'))
    sub_btn = tk.Button(root, text = 'Submit', command = submit)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(2, weight=1)
    message.grid(row=1, column=1)
    ans_entry.grid(row=2,column=1)
    sub_btn.grid(row=3,column=1)
    
    root.mainloop()

class location:
    def __init__(self, lx, rx, ty, by):
        self.lx = lx
        self.rx = rx
        self.ty = ty
        self.by = by
vials = location(270,401,383,551)
microscope = location(432,495,250,409)
lab_journal = location(435,529,425,465)
tablet = location(92,246,453,531)
pictures1 = location(385,440,109,193)
pictures2 = location(330,396,202,290)
papers = location(307,371,102,167)
lamp = location(16,154,210,446)

# main loop
def begin_room2(teamname):
    global team_name
    team_name = teamname
    pygame.init()
    gameDisplay = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Escape Room')
    clock = pygame.time.Clock()
    gameDisplay.blit(pygame.image.load("research_lab.png"),(0,0))

    ending = False
    while not ending:

        mx, my = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ending = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if vials.lx <= mx <= vials.rx and vials.ty <= my <= vials.by:
                    generate_popup("Vials",
                                   "\nWhat is the cure and who was the murderer??\nThe CEO of ____ murdered Dr. Anthony\nfor the ____ cure! (name, cure)\n",
                                   "Zoom, mRNA",
                                   "\nCongrats, " + teamname + "!\nYou Solved the Murder and Found the Cure!\nThe World Thanks You!")
                    break
                if microscope.lx <= mx <= microscope.rx and microscope.ty <= my <= microscope.by:
                    generate_popup("Microscope",
                                   "\nWhat do St. Patrick's Day, coronavirus lockdowns,\nand daylight savings time have in common?\n",
                                   "March",
                                   "\nThere are some interesting slides under the microscope...\nThis one shows the key ingredient to the cure is mRNA!")
                    break
                if lamp.lx <= mx <= lamp.rx and lamp.ty <= my <= lamp.by:
                    generate_popup("Journal",
                                   "Entry: Mrxuqdo, Lw'v rqh gdb vlqfh wkh glvfryhub.\nL kdg d vwudqjh ylvlw wrgdb iurp wkh FHR ri Crrp.\nWkhb vhhphg yhub dqjub dqg wkuhdwhqhg ph.\nWhich of your tools decodes messages?\n",
                                   "CIPHER",
                                   "\nEntry: Journal, It's one day since the discovery.\nI had a strange visit today from the CEO of Zoom.\nThey seemed very angry and threatened me.\n")
                    break
        pygame.display.update()

    pygame.quit()
    quit()
