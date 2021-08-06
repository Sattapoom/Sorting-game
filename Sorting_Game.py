# -------------------- GAME --------------------- #
class Sorting_game():
    def __init__(self):
        self.board = [["A","B","C","D"], ["E","F","G","H"], ["I","J","K"," "]]
        self.index_space = [2,3]
    
    def random_board_start(self):
        from random import choice
        char_remember = [None]*3
        for ran in range(choice([num for num in range(50,250)])):
            char_able = list()
            for i in [-1,1]:
                ht_letter = [self.index_space[0],self.index_space[1]+i]
                vc_letter = [self.index_space[0]+i,self.index_space[1]]
                if 0<= ht_letter[1] <=3:
                    char_able.append(self.board[ht_letter[0]][ht_letter[1]])
                if 0<= vc_letter[0] <=2:
                    char_able.append(self.board[vc_letter[0]][vc_letter[1]])
            moving_char = choice(char_able)
            if moving_char not in char_remember:
                self.move_character(moving_char)
            if choice([True,False]) :
                char_remember[ran%3] = moving_char
        #perfect random

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

    '''def EZ_board_start(self):
        self.board = [["A","B","C","D"], ["E","F","G","H"], [" ","I","J","K"]]
        for i in range(len(self.board)):
            if " " in self.board[i]:
                self.index_space[0] = i
                self.index_space[1] = self.board[i].index(" ")'''

# --------------- INPUT PROCESSOR --------------- #
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
    #game.EZ_board_start()
    game.random_board_start()
    game.display_board()
    while not game.check_endgame():
        INPUT = input_processor()
        game.move_character(INPUT.get_input())
        game.display_board()
    print("WIN")