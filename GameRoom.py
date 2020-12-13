import pygame
import pygame_menu
import tkinter as tk
from GameRoom2 import *

pygame.display.set_caption('Escape Room')
team_name = 'Hacker Squad'
next_room = False

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
            if clue == "Research Lab Access":
                global next_room
                next_room = True
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
lab = location(671,799,1,264)
body = location(130,531,416,595)
lab_coat = location(613,650,51,272)
phone = location(206,285,343,397)
toolbox = location(581,775,318,406)
wall_clock = location(258,306,19,114)
journal = location(321,482,133,167)
trash = location(204,294,236,316)


# main loop
def begin_room1(teamname):
    global team_name
    team_name = teamname
    pygame.init()
    gameDisplay = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Escape Room')
    clock = pygame.time.Clock()
    gameDisplay.blit(pygame.image.load("home_office.png"),(0,0))

    ending = False
    while not ending:

        mx, my = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ending = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lab.lx <= mx <= lab.rx and lab.ty <= my <= lab.by:
                    generate_popup("Research Lab Access",
                                   "\nIdentification Required.\n(LAST_NAME.ID_NUMBER)\n",
                                   "ANTHONY.275403",
                                   "\nAccess Granted.")
                    global next_room
                    if next_room:
                        begin_room2(team_name)
                    break
                if body.lx <= mx <= body.rx and body.ty <= my <= body.by:
                    generate_popup("Body",
                                   "\nResearcher who found coronavirus cure was murdered!\nFind the murderer and the cure before its too late.\nType 'help' for more info:\n",
                                   "help",
                                   "\nClick around the room to investigate clues.\nSolve puzzles and take notes along the way.\nHave fun!")
                    break
                if lab_coat.lx <= mx <= lab_coat.rx and lab_coat.ty <= my <= lab_coat.by:
                    generate_popup("Lab Coat",
                                   "\nIn the pockets you find:\nPAPERCLIP, GUM WRAPPER, PEN, ID CARD,\nNOTE to revise journal on desk\n",
                                   "ID Card",
                                   "\nHead Scientist at *smudge*\nName: S Anthony\nID NUM: *smudge*")
                    break
                if phone.lx <= mx <= phone.rx and phone.ty <= my <= phone.by:
                    generate_popup("Phone",
                                   "\nThe cell phone won't turn on.\nIt seems to be missing something...\n",
                                   "PHONE BATTERY",
                                   "\nI_: _ 7 5 _ 0 3\t_ f_u_d _h_ c_r_.\n_u_o_s _p_e_d _a_t _n_ t_i_ m_y _u_t _o_e _o_p_n_e_.\n_ j_s_ w_n_ t_ s_v_ l_v_s_ b_t _ f_a_ m_n_ i_ i_ d_n_e_.\n_t_y _a_e _n_ w_a_ a _a_k_ j_s_ i_ c_s_.")
                    break
                if toolbox.lx <= mx <= toolbox.rx and toolbox.ty <= my <= toolbox.by:
                    generate_popup("Toolbox",
                                   "\nThe toolbox is locked with a four-digit lock.\nTry a code:\n",
                                   "0529",
                                   "\nInside:\nCIPHER\nPHONE BATTERY\nMAGNIFYING GLASS")
                    break
                if wall_clock.lx <= mx <= wall_clock.rx and wall_clock.ty <= my <= wall_clock.by:
                    generate_popup("Clock",
                                   "\nTurn me on my side and I am everything.\nCut me in half and I am nothing.\nWhat am I?\n",
                                   "eight",
                                   "\nHuh that's strange.\nThe clock is stuck at 05:29")
                    break
                if journal.lx <= mx <= journal.rx and journal.ty <= my <= journal.by:
                    generate_popup("Journal",
                                   "Entry: Mrxuqdo, Lw'v rqh gdb vlqfh wkh glvfryhub.\nL kdg d vwudqjh ylvlw wrgdb iurp wkh FHR ri Crrp.\nWkhb vhhphg yhub dqjub dqg wkuhdwhqhg ph.\n\nIt seems to be encrypted. Done reading?\n",
                                   "yes",
                                   "\nMaybe the cipher to this message is in another room...\nshift 3")
                    break
                if trash.lx <= mx <= trash.rx and trash.ty <= my <= trash.by:
                    generate_popup("Trash",
                                   "\nWhat can you catch, but never throw?\nA  _ _ _ _\n",
                                   "cold",
                                   "\n_D_ 2 _ _ 4 _ _\tI _o_n_ t_e _u_e_\nR_m_r_ s_r_a_ f_s_ a_d _h_s _a_ h_r_ s_m_ c_m_a_i_s_\nI _u_t _a_t _o _a_e _i_e_, _u_ I _e_r _i_e _s _n _a_g_r_\nS_a_ s_f_ a_d _e_r _ m_s_, _u_t _n _a_e_")
                    break
                print(event)
        pygame.display.update()

    pygame.quit()
    quit()
