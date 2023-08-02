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


win_print = tkinter.Label(ttt.main_window, text="---Player win!---")
lose_print = tkinter.Label(ttt.main_window, text="---Computer win!---")
draw_print = tkinter.Label(ttt.main_window, text="---Draw!---")

#start game
while True:
# Add your game loop code here.
    if(ttt.is_player_win()):
        ttt.increment_wins()
        ttt.clear_slots()
        win_print.pack()
        ttt.update_gui()

    if(ttt.is_computer_win()):
        ttt.increment_losses()
        ttt.clear_slots()
        lose_print.pack()
        ttt.update_gui()

    if(not ttt.is_empty_found()):
        ttt.draw()
        draw_print.pack()
        ttt.update_gui()

    

    
    
    

    
    # Updates the GUI. DO NOT REMOVE OR MODIFY!
    try:
        ttt.main_window.update()
    except (tkinter.TclError, KeyboardInterrupt):
        quit(0)

    