import pygame, pygame_menu
import tkinter as tk

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
    pygame.display.set_caption('Escape Room') 
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
    pygame.display.set_caption('Escape Room')
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



chair = location(388, 500, 518, 572)
door = location(600,700,120,460)

# main loop
def start_tutorial(teamname):
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
                    generate_popup("Chair",
                                   "\nThere was a clue under the seat!\n\nThe more of this there is, the less you see.\nWhat is it?\n",
                                   "darkness",
                                   "\nOpen the door by saying OPEN")
                    pygame.time.wait(500)
                    break
                if door.lx <= mx <= door.rx and door.ty <= my <= door.by:
                    generate_popup("Door",
                                   "\nWhat's the password?\n",
                                   "OPEN",
                                   "\nCongrats, " + teamname + "!\nYou Win!")
                    break
            #print(event)
        pygame.display.update()

    pygame.quit()
    quit()




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
