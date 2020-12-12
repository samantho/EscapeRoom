import pygame
import pygame_menu
import tkinter as tk
from tkinter import messagebox


pygame.display.set_caption('Escape Room')

def generate_popup(clue, title, correct, unlocked):    
    # popup setup
    root = tk.Tk()
    root.title(clue)
    root.geometry("300x200")
    ans_var = tk.StringVar()

    # popup submission
    def submit():
        answer = ans_var.get()
        print("The answer submitted is : " + answer)
        if answer == correct:
            print("That's the answer!!!")
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
chair = location(388, 500, 518, 572)

# main loop
def start_tutorial():
    pygame.init()
    gameDisplay = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Escape Room')
    clock = pygame.time.Clock()
    gameDisplay.blit(pygame.image.load("library.png"),(0,0))

    ending = False
    while not ending:

        mx, my = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ending = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chair.lx <= mx <= chair.rx and chair.ty <= my <= chair.by:
                    generate_popup("Chair","This is the message\nrow 2\n", "1234", "\nCongrats")
                    pygame.time.wait(500)
                    break
            print(event)
        pygame.display.update()

    pygame.quit()
    quit()
