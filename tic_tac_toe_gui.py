import tkinter


class TicTacToeGUI:
    """
    Represents a graphical user interface for a Tic Tac Toe game.
    Dynamic variables enable the updating of win and loss counts.
    """
    def __init__(self, name='<replace>'):
        """
        Constructor for creating the main window and initialising
        the layout and components.
        :param name: The player's name.
        """
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        self.name = tkinter.StringVar()                    # Player's name.
        self.name.set('Name: ' + name)
        self.wins_str = tkinter.StringVar()                # Dynamically updating win counter.
        self.wins_str.set('Wins: 0')
        self.losses_str = tkinter.StringVar()              # Dynamically updating loss counter.
        self.losses_str.set('Losses: 0')
        self.player_turn = True                            # Switch for player or computer turn.

        self.title_frame = tkinter.Frame(self.main_window)
        self.create_title_bar()

        self.slots = ['', '', '', '', '', '', '', '', '']  # Represents the nine possible squares.
        self.grid_coords = {                               # Represents the centre x and y values for each square.
            '0': (80, 80),
            '1': (220, 80),
            '2': (370, 80),
            '3': (80, 220),
            '4': (220, 220),
            '5': (370, 220),
            '6': (80, 370),
            '7': (220, 370),
            '8': (370, 370)
        }

        self.canvas_frame = tkinter.Frame(self.main_window)
        self.c = self.create_canvas()
        self.canvas_frame.pack()

        self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)
        self.quit_button.pack()

        #out of source code add
        self.play_button = tkinter.Button(self.main_window, text='Play', command=self.play_button_clicked)

    def is_player_win(self):   
        """
        Checks if the player has won.
        """
        return self.check_win('X')
    
    def is_computer_win(self):
        """
        Checks if the computer has won.
        """
        return self.check_win('O')

    def is_empty_found(self) -> bool:
        """
        Checks if there are any empty squares.
        """
        for slot in self.slots:
            if slot == '':
                return True
        return False

    def check_win(self, letter):
        """
        Checks if the player or computer has won.
        """
        for i in range(0, 9, 3):
            if self.slots[i] == self.slots[i + 1] == self.slots[i + 2] == letter:
                return True

        
        for i in range(3):
            if self.slots[i] == self.slots[i + 3] == self.slots[i + 6] == letter:
                return True

        
        if self.slots[0] == self.slots[4] == self.slots[8] == letter:
            return True
        if self.slots[2] == self.slots[4] == self.slots[6] == letter:
            return True

        return False


    def create_title_bar(self):
        """
        Generates the top, title bar.
        """
        # Creates and add the labels for holding text.
        name_label = tkinter.Label(self.title_frame, textvariable=self.name)
        win_label = tkinter.Label(self.title_frame, textvariable=self.wins_str)
        loss_label = tkinter.Label(self.title_frame, textvariable=self.losses_str)

        name_label.pack(side='left')
        win_label.pack(side='left')
        loss_label.pack(side='left')

        self.title_frame.pack()

    def register_click(self, event):
        """
        Listens for mouse clicks and updates the grid squares with player X.
        :param event: The event generated by the click
        """
        x = event.x
        y = event.y

        # Determine which grid generated event.
        if 20 < x < 147 and 20 < y < 147:
            self.__update_slot(0)
        elif 153 < x < 297 and 20 < y < 147:
            self.__update_slot(1)
        elif 303 < x < 447 and 20 < y < 147:
            self.__update_slot(2)
        elif 20 < x < 147 and 153 < y < 297:
            self.__update_slot(3)
        elif 153 < x < 297 and 153 < y < 297:
            self.__update_slot(4)
        elif 303 < x < 447 and 153 < y < 297:
            self.__update_slot(5)
        elif 20 < x < 147 and 303 < y < 447:
            self.__update_slot(6)
        elif 153 < x < 297 and 303 < y < 447:
            self.__update_slot(7)
        elif 303 < x < 447 and 303 < y < 447:
            self.__update_slot(8)

    def __update_slot(self, slot):
        """
        Private, helper method for drawing an X in a grid square.
        :param slot: The slot in which to draw the X
        """
        if self.slots[slot] == '' and self.player_turn:
            self.player_turn = False
            self.slots[slot] = 'X'
            self.c.create_line(self.grid_coords[str(slot)][0] - 45,
                               self.grid_coords[str(slot)][1] - 45,
                               self.grid_coords[str(slot)][0] + 45,
                               self.grid_coords[str(slot)][1] + 45,
                               width=4)
            self.c.create_line(self.grid_coords[str(slot)][0] + 45,
                               self.grid_coords[str(slot)][1] - 45,
                               self.grid_coords[str(slot)][0] - 45,
                               self.grid_coords[str(slot)][1] + 45,
                               width=4)

    def move_computer(self, slot):
        """
        Draws a O for the computer turn in the given grid square.
        :param slot: The slot in which to draw the O
        """
        if self.slots[slot] == '' and not self.player_turn:
            self.c.create_oval(self.grid_coords[str(slot)][0] - 45,
                               self.grid_coords[str(slot)][1] - 45,
                               self.grid_coords[str(slot)][0] + 45,
                               self.grid_coords[str(slot)][1] + 45,
                               width=4)
            self.player_turn = True
            self.slots[slot] = 'O'

    def create_canvas(self) -> tkinter.Canvas:
        """
        Generates the drawing canvas for the play area.
        """
        c = tkinter.Canvas(self.canvas_frame, width=450, height=450)
        # Adds callback function for mouse events
        c.bind('<Button-1>', self.register_click)
        c.pack()

        c.create_line(147, 20, 147, 440, width=6)
        c.create_line(297, 20, 297, 440, width=6)
        c.create_line(20, 147, 440, 147, width=6)
        c.create_line(20, 297, 440, 297, width=6)

        return c

    def increment_wins(self):
        """
        Updates the win counter by 1.
        """
        self.clear_slots()
        wins = int(self.wins_str.get().split()[1])
        self.wins_str.set('Wins: ' + str(wins + 1))
        self.player_turn = True

    def increment_losses(self):
        """
        Updates the loss counter by 1.
        """
        self.clear_slots()
        losses = int(self.losses_str.get().split()[1])
        self.losses_str.set('Losses: ' + str(losses + 1))
        self.player_turn = True

    def draw(self):
        """
        Calls the game a draw.
        """
        self.clear_slots()
        self.player_turn = True

    def clear_slots(self):
        """
        Refreshes the slot list back to empty strings and clears the grid for a new game.
        """
        self.slots = ['', '', '', '', '', '', '', '', '']
        self.c.destroy()
        self.c = self.create_canvas()

    def get_wins(self) -> int:
        """
        Returns the number of player wins.
        :return: Total player wins
        """
        return int(self.wins_str.get().split()[1])

    def get_losses(self) -> int:
        """
        Returns the number of player losses.
        :return: Total player losses
        """
        return int(self.losses_str.get().split()[1])

    def update_gui(self):
            # Cập nhật giao diện ở đây với trạng thái hiện tại của lưới tic-tac-toe
            for i, symbol in enumerate(self.slots):
                if symbol == 'X':
                    self.c.create_line(self.grid_coords[str(i)][0] - 45,
                                    self.grid_coords[str(i)][1] - 45,
                                    self.grid_coords[str(i)][0] + 45,
                                    self.grid_coords[str(i)][1] + 45,
                                    width=4)
                    self.c.create_line(self.grid_coords[str(i)][0] + 45,
                                    self.grid_coords[str(i)][1] - 45,
                                    self.grid_coords[str(i)][0] - 45,
                                    self.grid_coords[str(i)][1] + 45,
                                    width=4)
                elif symbol == 'O':
                    self.c.create_oval(self.grid_coords[str(i)][0] - 45,
                                    self.grid_coords[str(i)][1] - 45,
                                    self.grid_coords[str(i)][0] + 45,
                                    self.grid_coords[str(i)][1] + 45,
                                    width=4)

    def play_button_clicked(self):
        player_won = False  # Assume the player did not win to demonstrate the code.
        computer_won = False  # Assume the computer did not win to demonstrate the code.

        if player_won:
            self.increment_wins()
        elif computer_won:
            self.increment_losses()
        else:
            self.draw()

        self.update_gui()  # Update the GUI after each move
