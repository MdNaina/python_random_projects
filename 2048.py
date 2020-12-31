import tkinter as tk
import color as c
import random

class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048 game")

        self.main_grid = tk.Frame(self, bg=c.GRID_COLOR, bd=3, width=600, height=600)
        self.main_grid.grid(pady=(100, 0))
        self.make_GUI()
        self.game_start()

        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)

        self.mainloop()


    def make_GUI(self):
        #make a grid
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg=c.EMPTY_CELL_COLOR,
                    width=150,
                    height=150
                )
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid, bg=c.EMPTY_CELL_COLOR)
                cell_number.grid(row=i, column=j)
                cell_data = {
                    "frame" : cell_frame,
                    "number" : cell_number,
                }
                row.append(cell_data)
            self.cells.append(row)
            # print(self.cells)
            #score view
        score_frame = tk.Frame(self)
        score_frame.place(relx=0.5, y=45, anchor="center")
        tk.Label(
            score_frame,
            text= "Score",
            font= c.SCORE_LABEL_FORT
        ).grid(row=0)
        self.score_label = tk.Label(score_frame, text="0", font=c.SCORE_FORT)
        self.score_label.grid(row=1)



    def game_start(self):
        self.matrix = [[0]*4 for _ in range(4)]

        # place 2 in random place 
        row = random.randint(0,3)
        col = random.randint(0,3)
        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg=c.CELL_COLOR[2])
        self.cells[row][col]["number"].configure(
            fg=c.CELL_NUMBER_COLOR[2],
            font=c.CELL_NUMBER_FORT[2],
            text="2",
        )

        while (self.matrix[row][col] != 0 ):
            row = random.randint(0,3)
            col = random.randint(0,3)
        
        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg=c.CELL_COLOR[2])
        self.cells[row][col]["number"].configure(
            fg=c.CELL_NUMBER_COLOR[2],
            font=c.CELL_NUMBER_FORT[2],
            text="2",
        )
        self.score = 0

    def stack(self):
        new_matrix = [[0]*4 for _ in range(4)]
        for i in range(4):
            fill_position = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    new_matrix[i][fill_position] = self.matrix[i][j]
                    fill_position += 1
        self.matrix = new_matrix
        # return self.matrix

    def combine(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j+1]:
                    self.matrix[i][j] *=2
                    self.matrix[i][j+1]= 0
                    self.score += self.matrix[i][j]
        # return self.matrix
               

    
    def reverse(self):
        new_matrix = [] 
        for i in range(4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3-j])
        self.matrix = new_matrix
        # return self.matrix


    
    def transpose(self):
        new_matrix = [[0]*4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_matrix[i][j] = self.matrix[j][i]        
        self.matrix = new_matrix
        # return self.matrix


    # add a new tile (new number)
    def add_new_tile(self):
        row = random.randint(0,3)
        col = random.randint(0,3)

        while (self.matrix[row][col] != 0):
            row = random.randint(0,3)
            col = random.randint(0,3)

        self.matrix[row][col] = 2
            
    #update GUI
    def update_GUI(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j]["frame"].configure(bg=c.EMPTY_CELL_COLOR)
                    self.cells[i][j]["number"].configure(bg=c.EMPTY_CELL_COLOR, text="")
                
                else:
                    self.cells[i][j]["frame"].configure(bg=c.CELL_COLOR[cell_value])
                    self.cells[i][j]["number"].configure(
                        bg=c.CELL_COLOR[cell_value], 
                        fg=c.CELL_NUMBER_COLOR[cell_value], 
                        font=c.CELL_NUMBER_FORT[cell_value],
                        text=str(cell_value)
                    )
        self.score_label.configure(text=self.score)
        self.update_idletasks()
    
    # control functions 
    def left(self, event):
        self.stack()
        self.combine()
        self.stack()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def right(self, event):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()


    def up(self, event):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    
    def down(self, event):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    # check for no box exist
    def horizontal_box_exist(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j+1]:
                    return True
        return False 

    def vertical_box_exist(self):
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i+1][j]:
                    return True
        return False

    
    # check for gameover or not 
    def game_over(self):
        if any(2048 in row for row in self.matrix):
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                game_over_frame,
                text="YOU WIN",
                bg=c.WINNER_BG,
                fg=c.GAME_OVER_FORT_COLOR,
                font=c.GAME_OVER_FORT,
            ).pack()
        
        elif not any(0 in row for row in self.matrix) and not self.horizontal_box_exist() and not self.vertical_box_exist():
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                game_over_frame,
                text="GAME OVER",
                bg=c.LOSER_BG,
                fg=c.GAME_OVER_FORT_COLOR,
                font=c.GAME_OVER_FORT,
            ).pack()


def main():
    Game()

if __name__ == '__main__':
    main()
