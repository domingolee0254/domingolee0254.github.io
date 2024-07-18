import sys

def main(board):
    i = 0
    while i < len(board):

        if board[i] == "X":
            if board[i:i+4] == "XXXX":
                board = board[:i] + "AAAA" + board[i+4:]
            elif board[i:i+2] == "XX":
                board = board[:i] + "BB" + board[i+2:]
            else:
                return -1   
        i += 1
    return board

if __name__=="__main__":
    input = sys.stdin.readline
    board = input().strip()
    ret = main(board)
    print(ret)