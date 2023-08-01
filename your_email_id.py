import tic_tac_toe_gui 
import tkinter

# The object of the TicTacToeGUI class that renders the GUI.
# You can use this object to access the methods listed in the specification.


# Main game loop.
def display_details():
        print("File      : tic_tac_toe.py")
        print("Author    : Vy Dao Tuong Truong _ Kady ")
        print("Student ID: 44661")
        print("Email ID  : ")
        print("This is my own work as defined by the University's Academic Misconduct Policy\n ")
display_details()

#enter player name
answer = input("Would you like to play tic tac toe? (y/n): ")
while answer != "y" and answer != "n": 
    answer = input("Enter your answer again (y/n): ")
if answer == "y":
    ttt = tic_tac_toe_gui.TicTacToeGUI(input("Enter Playername:"))
if answer == "n":
    quit(0)


#start game
ttt.play_button_clicked()
while True:
# Add your game loop code here.
       
    empty_slots_found : bool = ttt.is_empty_found()
    if empty_slots_found == False:
        ttt.draw()
        ttt.update_gui()
    
    player_won : bool = ttt.is_player_won()
    if player_won == True:
        ttt.increment_wins()
        ttt.get_wins()
        ttt.update_gui()
        
    computer_won : bool = ttt.is_computer_won() 
    if computer_won == True:
        ttt.increment_losses()
        ttt.get_losses()
        ttt.update_gui()

    
    # Updates the GUI. DO NOT REMOVE OR MODIFY!
    try:
        ttt.main_window.update()
    except (tkinter.TclError, KeyboardInterrupt):
        quit(0)

    