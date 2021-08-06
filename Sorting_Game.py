class Sorting_game():
    def __init__(self):
        self.board = [["A","B","C","D"], ["E","F","G","H"], ["I","J","K"," "]]
        self.index_space = [2,3]
    
    def random_board_start(self):
        from random import randint, shuffle

        shuffle(self.board)
        shuffle(self.board[0])
        shuffle(self.board[1])
        shuffle(self.board[2])

        for i in range(randint(0,4)):
            for j in range(12):
                index_ran1 = [randint(0,2) ,randint(0,3)]
                index_ran2 = [randint(0,2) ,randint(0,3)]
                self.board[index_ran1[0]][index_ran1[1]], self.board[index_ran2[0]][index_ran2[1]] = self.board[index_ran2[0]][index_ran2[1]], self.board[index_ran1[0]][index_ran1[1]]

        for i in range(len(self.board)):
            if " " in self.board[i]:
                self.index_space[0] = i
                self.index_space[1] = self.board[i].index(" ")

    def EZ_board_start(self):
        self.board = [["A","B","C","D"], ["E","F","G","H"], [" ","I","J","K"]]
        for i in range(len(self.board)):
            if " " in self.board[i]:
                self.index_space[0] = i
                self.index_space[1] = self.board[i].index(" ")

    def display_board(self):
        for i in self.board:
            print(f"{i[0]} {i[1]} {i[2]} {i[3]}")
        print("--------")
            
    def check_endgame(self):
        if self.board == [["A","B","C","D"], ["E","F","G","H"], ["I","J","K"," "]]:
            return True
        else:
            return False
    
    def move_character(self,c:str):
        # top check
        top_index = self.index_space[0] - 1
        if top_index >= 0:
            if self.board[top_index][self.index_space[1]] == c:
                self.board[top_index][self.index_space[1]] = " "
                self.board[self.index_space[0]][self.index_space[1]] = c
                self.index_space[0] = top_index
                return
        # bottom check
        bottom_index = self.index_space[0] + 1
        if bottom_index <= 2:
            if self.board[bottom_index][self.index_space[1]] == c:
                self.board[bottom_index][self.index_space[1]] = " "
                self.board[self.index_space[0]][self.index_space[1]] = c
                self.index_space[0] = bottom_index
                return
        # left check
        left_index = self.index_space[1] - 1
        if left_index >= 0:
            if self.board[self.index_space[0]][left_index] == c:
                self.board[self.index_space[0]][left_index] = " "
                self.board[self.index_space[0]][self.index_space[1]] = c
                self.index_space[1] = left_index
                return
        # right check
        right_index = self.index_space[1] + 1
        if right_index <= 3:
            if self.board[self.index_space[0]][right_index] == c:
                self.board[self.index_space[0]][right_index] = " "
                self.board[self.index_space[0]][self.index_space[1]] = c
                self.index_space[1] = right_index
                return
        print(f"Can not move : {c}")
class input_processor():
    def __init__(self):
        self.letter = ""
        self.checker = ["A","B","C","D","E","F","G","H","I","J","K"]
        self.check_input()
    def check_input(self):
        while True:
                input_letter = input("Input letter : ")
                if input_letter.upper() in self.checker:
                    self.letter = input_letter.upper()
                    break
                else:
                    print("Please Enter A-K")
    def get_input(self):
        return self.letter
if __name__ == '__main__':
    game = Sorting_game()
    game.EZ_board_start()
    # game.random_board_start()
    game.display_board()
    while not game.check_endgame():
        INPUT = input_processor()
        game.move_character(INPUT.get_input())
        game.display_board()
    print("WIN")