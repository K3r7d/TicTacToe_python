import TicTacToe_python.tic_tac_toe_gui as tic_tac_toe_gui
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

def check_win(slots,letter):
    #hàng ngang
    if slots[1] == letter and slots[2] == letter and slots[3] == letter:
        return True
    elif  slots[4] == letter and slots[5] == letter and slots[6] == letter:
        return True
    elif slots[7] == letter and slots[8] == letter and slots[9] == letter:
        return True
    #hàng dọc 
    if slots[1] == letter and slots[4] == letter and slots[7] == letter:
        return True
    elif slots[2] == letter and slots[5] == letter and slots[8] == letter:
        return True
    elif slots[3] == letter and slots[6] == letter and slots[9] == letter:
        return True
    #duong cheo 
    if slots[1] == letter and slots[5] == letter and slots[9] == letter:
        return True
    if slots[3] == letter and slots[5] == letter and slots[7] == letter:
        return True

    return False


while True:
# Add your game loop code here.
    
    # Updates the GUI. DO NOT REMOVE OR MODIFY!
    try:
        ttt.main_window.update()
    except (tkinter.TclError, KeyboardInterrupt):
        quit(0)

    