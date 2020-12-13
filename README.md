# EscapeRoom
 
## A researcher has found the cure to COVID-19! However, they were tragically found murdered last night! Find out who killed the scientist and find the cure... BEFORE IT'S TOO LATE!

### Creators: 
Samantha Anthony and Nick Anthony
### Code: 
This game is made entirely with python. Packages required are pygame, pygame_menu, and tkinter.
### Controls: 
Click around the rooms to investigate certain items. Follow the popup boxes, find clues, and make sure to take notes along the way! Happy sleuthing!

### Explanation:
This escape room is a self-timed puzzle adventure. The goal is to figure out who murdered the researcher and continue their research to find the coronavirus cure. 

When the game is run, a menu will pop up with options
- Team Name: input your escape room team's names
- Difficulty: Easy will take you to a tutorial room, Hard will take you to the real room
- Enter Room: starts the game with the options displayed
- Quit: exit the game

### Tips and Tricks
- Uppercase items may be important to remember because they are tools that could - be used in later locations.
- Take notes along the way!
- There are two rooms in the hard game, so move quickly!
- Walkthroughs for both rooms are below for if you get stuck, so spoiler alert for the rest of the page!


### Tutorial Walkthrough:
Clickable objects: right chair, door
1. Click on the bottom area of the right chair between the chair and the seat cushion
2. A box will pop up that says, "There was a clue under the seat! The more of this there is, the less you see. What is it?"
3. Type "darkness" in the input box and press submit
4. A clue reveals that says "Open the door by saying OPEN"
5. Click on the Door in the bookshelf
6. A box will pop up that says "What's the password?"
7. Use the clue from step 4 by typing "OPEN" into the input box and pressing submit
8. You should see a message that says "Congrats, [Team Name]! You Win!"

### Main Game Walkthrough:
##### Murder Room
Clickable objects: lab door, body outline, lab coats, phone, toolbox, wall clock, desk journal, and trash
- body outline: gives info on the murder, can submit 'help' for more info
- desk journal: gives encoded message that is not needed until the next room, can submit 'yes' when done reading for more info, can solve before next room for fun with the shift 3 decoder clue
- lab coats: lists items in pockets, submit 'ID CARD' to obtain the researcher's LAST NAME
- wall clock: riddle answer is 8, submit 'eight' to get the four-digit number 0529
- toolbox: submit '0529'' from the wall clock clue to unlock the box, lists items in box such as CIPHER and PHONE BATTERY
- phone: submit 'PHONE BATTERY' to make the phone work and get a 1/2 PUZZLE
- trash: riddle answer is a cold, submit 'cold' to get a 1/2 PUZZLE
- lab door: get last name from lab coats, get id number from combining the puzzles in trash and phone, submit 'Anthony.275403' to get access, moves to new room when popup is exited

##### Research Lab
Clickable objects: lit lamp and desk, microscope, vials
- lamp and desk: displays journal entry from before, submit 'CIPHER' to decode, get info that the murderer is the CEO of Zoom
- microscope: riddle answer is the month of March, submit 'March' to get info that the cure ingredient is mRNA
- vials: the murderer was the CEO of Zoom and the cure uses mRNA technology, submit 'Zoom, mRNA' to win!
