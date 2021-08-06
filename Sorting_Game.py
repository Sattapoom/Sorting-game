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

    def display_board(self):
        for i in self.board:
            print(f"{i[0]} {i[1]} {i[2]} {i[3]}")
            
    def check_endgame(self):
        pass
    
    def move_character(self,c):
        pass

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
#game_sort = input_processor()
#print(game_sort.get_input())
