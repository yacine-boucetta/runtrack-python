import random


class Board:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.board = self.create_board()

    def create_board(self):
        return [['O' for _ in range(self.j)] for _ in range(self.i)]

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print(' '.join(str(x) for x in range(1, self.j + 1)))

    def play(self, col, color):
        player = 'J' if color == "jaune" else 'R'
        self.play_move(col - 1, player)

    def play_move(self, col, player):
        if col < 0 or col >= self.j:
            raise ValueError("Colonne invalide")

        for row in reversed(self.board):
            if row[col] == 'O':
                row[col] = player
                break
        else:
            raise ValueError("Colonne pleine")

    def check_winner(self, player):
        for row in range(self.i):
            for col in range(self.j):
                if self.board[row][col] == player:
                    if self.check_horizontal(row, col, player) or self.check_vertical(row, col, player) or self.check_diagonal(row, col, player):
                        return True
        return False

    def check_horizontal(self, row, col, player):
        if col + 4 > self.j:
            return False
        return all(self.board[row][c] == player for c in range(col, col + 4))


    def check_vertical(self, row, col, player):
        return any(self.board[r][col] == player for r in range(row, row + 4)) if row + 4 <= self.i else False

    def check_diagonal(self, row, col, player):
        if col + 4 <= self.j and row + 4 <= self.i:
            if all(self.board[row + r][col + r] == player for r in range(4)):
                return True

        if col - 3 >= 0 and row + 4 <= self.i:
            if all(self.board[row + r][col - r] == player for r in range(4)):
                return True
        return False




class AI_One:
    def think(self, board, color):
        available_columns = [col for col in range(board.j) if board.board[0][col] == 'O']
        return random.choice(available_columns) + 1  

def main():
    board = Board(6, 7)
    players = ["jaune", "rouge"]
    ai = AI_One()
    winner = None
    turn = 0

    while not winner:
        board.print_board()
        print("Tour du joueur", players[turn % 2])

        if players[turn % 2] == "jaune":  # Le joueur jaune est un joueur humain
            try:
                col = int(input("Entrez le numéro de colonne dans laquelle vous souhaitez insérer votre jeton: "))
            except ValueError:
                print("Veuillez entrer un nombre valide.")
                continue
        else:  # Le joueur rouge est AI_One
            col = ai.think(board, "rouge")
            print("AI_One a choisi la colonne", col)

        try:
            board.play(col, players[turn % 2])
            if board.check_winner('J' if players[turn % 2] == "jaune" else 'R'):
                winner = players[turn % 2]
            turn += 1
        except ValueError as e:
            print("Erreur:", e)
            print("Veuillez réessayer.")

    board.print_board()
    print("Le joueur", winner, "a gagné et remporte 100 000 euros!")

if __name__ == "__main__":
    main()
