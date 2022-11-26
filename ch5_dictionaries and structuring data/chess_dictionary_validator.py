'''
Write a function named isValidChessBoard() that takes a dictionary argument
and returns True or False depending on if the board is valid.
'''

def main():

    board = {'1a': 'bking','2a': 'bqueen','3a': 'brook','4a': 'brook',
    '5a': 'bknight','6a': 'bknight','7a':'bbishop','8a': 'bbishop',
    '1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b':'bpawn',
    '5b': 'bpawn','6b': 'bpawn','7b': 'bpawn','8b': 'bpawn',
    '1c': 'wking','2c': 'wqueen','3c': 'wrook','4c': 'wrook',
    '5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c':'wknight',
    '1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn',
    '5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn',}
    #'1f': '','2f': '','3f': '','4f': '','5f': '','6f': '','7f': '','8f': '',
    #'1g': '','2g': '','3g': '','4g': '','5g': '','6g': '','7g': '','8g': '',
    #'1h': '','2h': '','3h': '','4h': '','5h': '','6h': '','7h': '','8h': '',}

    print(isValidChessBoard(board))


def isValidChessBoard(board: dict) -> bool:
    counter = 0

    # Exactly one black king and exactly one white king
    if list(board.values()).count("bking") == 1\
        and list(board.values()).count("wking") == 1:
        counter += 1
    else:
        print("KingError")
        return False
    
    # Each player can only have at most 16 pieces
    black = 0
    white = 0
    for v in board.values():
        if v[0] == "b":
            black += 1
        if v[0] == "w":
            white += 1
    if black < 17 and white < 17:
        counter += 1
    else:
        print("MaximumPiecesError")
        return False

    # At most 8 pawns
    bp = 0
    wp = 0
    for v in board.values():
        if v == "bpawn":
            bp += 1
        if v == "wpawn":
            wp += 1
    if bp < 9 and wp < 9:
        counter += 1
    else:
        print("PawnError")
        return False
    
    # All pieces must be on a valid space from '1a' to '8h'
    num = list(range(1, 9)) # num = [1,2,3,4,5,6,7,8]
    alpha = []              # alpha = ["a","b","c","d","e","f","g","h"]
    for i in range(97, 105):
        alpha.append(chr(i))
    
    num_pieces = 0
    for n in num:
        for alp in alpha:
            if f"{n}{alp}" in board:
                num_pieces += 1

    if num_pieces == len(list(board)):
        counter += 1
    else:
        print("ValidSpaceError")
        return False

    # The piece names begin with either a 'w' or 'b' to represent white or black,
    # followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'
    prefix = ["w", "b"]
    piece_name = ["pawn", "knight", "bishop", "rook", "queen", "king"]
    full_name = []
    for pre in prefix:
        for piece in piece_name:
            full_name.append(f"{pre}{piece}")

    num_pieces_2 = 0

    for v in board.values():
        if v in full_name:
                num_pieces_2 += 1

    if num_pieces_2 == len(list(board)):
        counter += 1
    else:
        print("NameError")
        return False


    # Valid chess board if counter is 5
    if counter == 5:
        return True


if __name__ == "__main__":
    main()