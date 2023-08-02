import tic_tac_toe_gui as ttg
import tkinter

# The object of the TicTacToeGUI class that renders the GUI.
# You can use this object to access the methods listed in the specification.
ttg.display_details()
    
#start game
answer = str(input("Would you like to play a game of Tic Tac Toe ? [y/n]: "))
while answer != "y" and answer != "n":
    answer = str(input("Would you like to play a game of Tic Tac Toe ? [y/n]: "))
if answer == "y":
    ttt = ttg.TicTacToeGUI(input("Enter your name: "))
if answer == "n":
    quit(0)

game_has_ended = False
while True:
# Add your game loop code here.
    if not game_has_ended:
        print("---------------------- START GAME ----------------------")
    while True:
        if ttg.check_win(ttt.slots,'X'):
            ttt.total_games += 1
            ttt.player_wins += 1
            print("--- Player wins! ---")
            ttg.display_game(ttt.slots)
            if(ttg.end_game() == "n"):
                game_has_ended = True
                ttg.display_static(ttt)
                
            ttt.increment_wins()
            break
        

        if ttg.check_win(ttt.slots,'O'):
            ttt.total_games += 1
            ttt.computer_wins += 1
            print("--- Computer wins! ---")
            ttg.display_game(ttt.slots)
            if(ttg.end_game() == "n"):
                game_has_ended = True
                ttg.display_static(ttt)
                
            ttt.increment_losses()
            break


        if not ttt.is_empty_found():
            ttt.total_games += 1
            ttt.draws += 1
            print("--- Draw! ---")
            ttg.display_game(ttt.slots)
            if(ttg.end_game() == "n"):
                game_has_ended = True
                ttg.display_static(ttt)
            ttt.draw()
            break
        

        if ttt.player_turn == False:
            ttg.move_computer(ttt)
            ttt.player_turn = True
        ttt.update_gui()

    # Updates the GUI. DO NOT REMOVE OR MODIFY!
        try:
            ttt.main_window.update()
        except (tkinter.TclError, KeyboardInterrupt):
            quit(0)


