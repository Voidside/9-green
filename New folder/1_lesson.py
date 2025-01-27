# print("Hello World !")
print(2+4*2)
# print(2345234+689898)

"""print("G'alaba")
print('G\'alaba')
"""
# print("u darsga keldi, \"bu juda yaxshi\"")
# 1 qatorli komment 
""" ko'p qatorli komment """   

""" O'zgruvchilar """
""" Biron bir ma'lumatni bir nomga boiriktirib qo'yisjh"""
""" O'zgaruvchi (variable) chunki ma'lumot istalgan vaqtda o'zgartirilishi mumkin 
    Faqat harf yoki (_) bilan boshlanishi kerak
    Raqam bilan boshlanishi mumkin emas 
    nomida faqat (a-z), (_) ishlatilishi mumkin 
    ISM, ism va Ism boshqa boshqa narsalar
    shuningdek (keyword)lar nom bo'la olmaydi:
    if, await, false4, true..."""

# print("Oydina")

# ism = "Oydina"
# print(ism)

# yosh = 56
# yosh = 5.6
# sinf = "9-Green"

# ism = "Ahmad"
# print(" Mening ismim " + ism)

# ism = 'Ahad'
# familiya = 'Qayum'
# print(ism + familiya)

# ism = 'Ahad'
# familiya = 'Qayum'
# print(ism + ' ' + familiya) # ikki o'zgaruvchi orasiga bo'sh joy qo'shamiz

# ism = "Ahad"
# familiya = 'Qayum'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.upper())

# ism = "Ahad"
# familiya = 'Qayum'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.upper())


# ism = "James"
# familiya = 'Bond'
# print( f"Salom mening ismim {familiya}. {ism} {familiya}! ")

# matn_1 = "Bu"
# matn_2 = " matn"
# matn_3 = matn_1 + matn_2
# print(matn_3)

# ""|"Bir vaqtni o'zida  ko'p o'zgaruvchi yaratish"""
# x,y,z = "olma", "banan", "olcha"
# print(x)
# print(y)
# print(z)

# """Birxil qiymatli o'zgaruvchilar"""
# x = y = z = "olma"
# print(x)
# print(y)
# print(z)

# print("Hello World!")
# print("Hello  \tWorld")
# print("Hello  \nWorld")

# x = 5 
# y = 10
# print(x + y)

# x = 5
# y = 10
# print(x , y)

# """Ma'lumot turlari"""
# son = 5      #butun son - integer
# son2 = 2.5   #o'nlik - float
# matn = "matn" #matn - string

# ismlar = ["Ali, Olim, Vali"]  #ro'yhat - list       
"{"""
# # 1
# print("olma")
# print("anor")
# print("banan")
# print("uzum")
# print("meva")
# # 2
# print("Iskandar")
# print("Abdulahad")
# print("Muhammad Ayyub")
# print("Rayhona")
# print("Sadbarxon")
# print("Rayona")
# # 3
# print("1")
# print("2")
# print("3")
# # 4
# ism = "Ism"
# print(ism)
# print(type(ism))

# familiya = "Familiya"
# print(familiya)
# print(type(familiya))

# son = "Son"
# print(son)
# print(type(son))

# # 5
# ism = "Abdulahad"
# familiya = "Ubaydullayev"
# yosh = "15"
# manzil = "Namangan"    



class ChessPiece:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def __str__(self):
        return f"{self.color} {self.name}"

class ChessBoard:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        # Initialize an 8x8 chessboard
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Place pawns
        for i in range(8):
            board[1][i] = ChessPiece('White', 'Pawn')
            board[6][i] = ChessPiece('Black', 'Pawn')

        # Place other pieces
        pieces = ['Rook', 'Knight', 'Bishop', 'Queen', 'King', 'Bishop', 'Knight', 'Rook']
        for i, piece in enumerate(pieces):
            board[0][i] = ChessPiece('White', piece)
            board[7][i] = ChessPiece('Black', piece)

        return board

    def display(self):
        for row in self.board:
            print(" | ".join(str(piece) if piece else " . " for piece in row))
            print("-" * 32)

class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.turn = 'White'

    def switch_turn(self):
        self.turn = 'Black' if self.turn == 'White' else 'White'

    def play(self):
        while True:
            self.board.display()
            print(f"{self.turn}'s turn. Enter move (e.g., e2 e4):")
            move = input()
            # Here, you would add code to validate and make the move
            self.switch_turn()

if __name__ == "__main__":
    game = ChessGame()
    game.play()